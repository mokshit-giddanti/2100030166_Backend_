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
cursor.execute("SELECT Products.ProductName FROM OrderItems JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE OrderItems.OrderID = 1")

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()