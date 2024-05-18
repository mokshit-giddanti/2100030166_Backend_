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
cursor.execute("SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, Customers.Email FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID")

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()