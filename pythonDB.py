# import libraries
import pandas as pd
import mysql.connector


# Connect Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fluxbyte@7",
    database="ExcelData",

)
mycursor = mydb.cursor()

# Create Database
# mycursor.execute("CREATE DATABASE ExcelData")

# CSV File Data
data = pd.read_csv(
    r"C:\Users\fluxb\OneDrive\Desktop\Hitesh\Python-Task\data\gujarat_covid.csv")
data_covid = pd.DataFrame(data)
print('data_covid: ', data_covid)


# Create table
# mycursor.execute("CREATE TABLE Covid_Data (id INT AUTO_INCREMENT PRIMARY KEY, District VARCHAR(255), Active_Cases integer, Cases_Tested_for_COVID19 integer, Patients_Recovered integer)")

# Insert column
# mycursor.execute("ALTER TABLE  Covid_Data ADD (People_Under_Quarantine integer)")
# mycursor.execute("ALTER TABLE  Covid_Data ADD (Total_Deaths integer)")


# Insert data
value = ""
for row in data_covid.itertuples():
    value = value + \
        f"('{row.District}',{row.Active_Cases},{row.Cases_Tested_for_COVID19},{row.Patients_Recovered},{row.People_Under_Quarantine},{row.Total_Deaths}),"
mycursor.execute(
    f"""INSERT into Covid_Data (District,Active_Cases,Cases_Tested_for_COVID19,Patients_Recovered,People_Under_Quarantine,Total_Deaths)  VALUES {value[:-1]}""")

mydb.commit()
