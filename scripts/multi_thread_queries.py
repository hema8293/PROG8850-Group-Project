import threading
import mysql.connector
import time

# Database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=Root@1234,
  database="project_db"
)

cursor = db.cursor()

# Insert Query
def insert_data():
    for i in range(5):
        sql = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES (%s, %s, %s, %s, %s)"
        val = ("Location" + str(i), "2024-04-01", 25.5+i, 12.0+i, 75.0+i)
        cursor.execute(sql, val)
        db.commit()
        time.sleep(1)

# Select Query
def select_data():
    for i in range(5):
        cursor.execute("SELECT * FROM ClimateData WHERE temperature > 0")
        result = cursor.fetchall()
        print(result)
        time.sleep(1)

# Update Query
def update_data():
    for i in range(5):
        cursor.execute("UPDATE ClimateData SET humidity = humidity + 1 WHERE location LIKE 'Toronto%'")
        db.commit()
        time.sleep(1)

# Creating Threads
t1 = threading.Thread(target=insert_data)
t2 = threading.Thread(target=select_data)
t3 = threading.Thread(target=update_data)

# Start Threads
t1.start()
t2.start()
t3.start()

# Join Threads
t1.join()
t2.join()
t3.join()

print("Multi-thread Queries Executed Successfully")
