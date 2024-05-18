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
cursor.execute("SELECT DATE_FORMAT(Orders.OrderDate, '%Y-%m') AS Month, COUNT(Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSalesAmount FROM Orders JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE Orders.OrderDate BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY Month")

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()