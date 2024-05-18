import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)

# Create a cursor object
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31'")

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
print(rows)

# Close the connection
conn.close()