import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r'C:\Users\my pc\Downloads\samplesuperstore.csv')
'''
print(data)
print(data.to_string())
print(data.head(5).to_string())
print(data.tail(5).to_string())
print(data.describe().to_string())
print(data.columns)
print(data[:5].to_string())
print(data[100:151].to_string())
print(data[-5:].to_string())
print(data.dtypes)
print(data[['Region','Sales','Profit']].to_string())

regionwisesale=data.groupby('Region')['Sales'].sum()
print(regionwisesale)
regionwisesale1=data.groupby('Region')[['Sales','Profit']].sum().reset_index()
print(regionwisesale1)
regionwisesale1.columns=['Region','Sum_of_sale','Sum_of_profit']
print(regionwisesale1)
plt.figure(figsize=(10,5))
plt.plot(regionwisesale1['Region'],regionwisesale1[['Sum_of_sale','Sum_of_profit']],marker='*',linestyle='-.',color='green')
plt.title('sttwisetotal')
plt.xlabel('Region')
plt.ylabel('Sum_of_sale')
plt.grid(True)
plt.show()'''
'''
regionwisesale=data.groupby('Region')['Sales'].sum()
regionwisesale.plot(kind='line')
plt.show()
regionwisesale1=data.groupby('Region')[['Sales','Profit']].sum().reset_index()
regionwisesale1.plot(kind='line')
plt.show()
regionwisesale1.plot.bar(subplots=True)
plt.show()
regionwisesale1.plot.barh(subplots=True)
plt.show()
'''

regionwiseinfo=data.groupby('Region')[['Sales','Profit','Quantity']].sum().reset_index()
print(regionwiseinfo)
regionwiseinfo.plot.bar(title='Region_Wise vs Sales''Region_Wise vs Profit',color=['green','blue','red'],subplots=True)
plt.show()

