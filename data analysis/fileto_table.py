import pandas as pd
from sqlalchemy import create_engine
connection_string = 'mysql+pymysql://root:suresh@localhost:3306/pandasexample1r'
engine = create_engine(connection_string)
files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']
for file in files:
    pat = rf"C:\Users\my pc\PycharmProjects\suresh\data analysis\famous_paintings\{file}.csv"
    df = pd.read_csv(pat)
    df.to_sql(file, con=conne ction_string, if_exists='replace', index=False)