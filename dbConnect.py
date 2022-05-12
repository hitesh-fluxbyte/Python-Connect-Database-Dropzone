# import libraries
import pandas as pd
import mysql.connector


# Connect Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fluxbyte@7",
    database="mydatabase",
)
mycursor = mydb.cursor()

# Create Table Employee
mycursor.execute(
    "CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# Insert Data into Employee
sql = "INSERT INTO Employee (name, address) VALUES (%s, %s)"
val = [("Hitesh Zala", "Mahemdavad"),
       ("Shubham Patel", "Ahmedavad")
       ]
mycursor.executemany(sql, val)

# CSV File Data
data = pd.read_csv(
    r"C:\Users\fluxb\OneDrive\Desktop\Hitesh\Python-Task\data\sample.csv")
df = pd.DataFrame(data)

# Create SampleCSV Table
mycursor.execute(
    "CREATE TABLE SampleCSV (Game_Number VARCHAR(255), Game_Length VARCHAR(255))")


# Insert Data into SQL
value = ""
for row in df.itertuples():
    value = value + f"( {row.num1},{row.num2}),"
mycursor.execute(
    f"""INSERT into SampleCSV (Game_Number,Game_Length)  VALUES {value[:-1]}""")

mydb.commit()
