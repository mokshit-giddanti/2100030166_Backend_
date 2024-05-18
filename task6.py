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
cursor.execute("SELECT Products.ProductName, COUNT(OrderItems.OrderItemID) AS TotalOrders FROM Products JOIN OrderItems ON Products.ProductID = OrderItems.ProductID GROUP BY Products.ProductID ORDER BY TotalOrders DESC LIMIT 1")

# Fetch the row
row = cursor.fetchone()

# Print the result
print(row)

# Close the connection
conn.close()