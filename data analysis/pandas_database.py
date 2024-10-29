import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
config = {
    'user': 'root',
    'password': 'suresh',
    'host': 'localhost',
    'database': 'classicmodels'
}
cnx = mysql.connector.connect(**config)
sqlquery="""select b.*,
a.orderdate,a.status,c.*
from orders a 
inner join 
orderdetails b 
on a.ordernumber=b.ordernumber
inner join customers c on a.customernumber=c.customernumber
"""
dataframe=pd.read_sql(sqlquery,cnx)
print(dataframe)
print(dataframe.shape)
dataframe['amount']=dataframe['quantityOrdered']*dataframe['priceEach']
print(dataframe)
orderwise=dataframe.groupby('orderNumber')['amount'].sum()
print(orderwise)
orderwise.plot(kind='bar')
plt.show()
