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
cursor.execute("SELECT Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalAmountSpent FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID GROUP BY Customers.CustomerID")

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()