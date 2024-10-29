# pandas are divided into two tpes they are series and dataframe
#series-only have row index
#dataframe as row and column index
#1,from csv,2.manually,3.from databse
import pandas as pd
import matplotlib.pyplot as plt
series1=pd.Series([1,2,3,4,5])
print(series1)
print(series1.values)
print(series1.index)
series2=pd.Series([1,2,4,5,6],index=[4,5,6,7,8])
print(series2,series2.values,series2.index)
series2.index=['a','b','c','e','f']
print(series1)
print(series1.values)
print(series1.index)
print(series2,series2.values,series2.index)
print()

dict1={'apple':50,'orange':20,'grapes':10,'mango':10,'banana':5}
series3=pd.Series(dict1)
print(series3)
newindex=['apple','orange','grapes','mango','banana','kiwi']
series4=pd.Series(dict1,index=newindex)
print(series4)
print('apple' in series3)#it will print whether the element is there in the dictionary
print(series2)
print(series2[3])
print(series2+3)
print()

st=[[1,'abc'],[2,'xyz'],[3,'def']]
print(st)
stdataframe=pd.DataFrame(st)
print(stdataframe)
stdataframe1=pd.DataFrame(st,columns=['s.no','s.name'])
print(stdataframe1)
stdataframe2=pd.DataFrame(st,columns=['s.no','s.name'],index=['a','b','c'])
print(stdataframe2)

student=[[1,'a',10,20,25],[2,'b',9,17,15],[3,'c',8,25,30],[4,'d',7,18,19],[5,'e',8,19,16]]
print(student)
stdf=pd.DataFrame(student,columns=['s.np','name','m1','m2','m3'])
print(stdf)
stdf['total']=stdf['m1']+stdf['m2']+stdf['m3']
print(stdf)
stdf['avg']=stdf['total']/3
print(stdf)

def gradecalculations(total):
    if total>=65:
        return 'A'
    elif total>=55:
        return 'B'
    elif total>=44:
        return'C'
    else:
        return 'D'
stdf['grade']=stdf['total'].apply(gradecalculations)
print(stdf)
#plt.figure(figure=(10,5))
# plt.plot(stdf['s.np'],stdf['total'],marker='*',linestyle='-.',color='black')
# plt.title('sttwisetotal')
# plt.xlabel('student')
# plt.ylabel('total')
# plt.grid(True)
# plt.show()
stdf.plot(x='s.np',y='total',kind='bar',color='blue',figsize=(10,5))
plt.title('sttwisetotal')
plt.xlabel('student')
plt.ylabel('total')
# plt.grid(True)
plt.show()
