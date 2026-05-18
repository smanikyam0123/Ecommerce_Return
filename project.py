import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sara1289",
    database="ecommers_return"
)

print("Connected Successfully!")


query = "SELECT * FROM orders"

df = pd.read_sql(query, conn)

print(df)

df.to_csv("data.csv", index=False)

conn.close()