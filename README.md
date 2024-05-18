# 2100030166_Backend (18-05-2024)

## Task_1 List all customers.
SQL Query:
```sql
SELECT * FROM Customers;
```
![alt text](/images/image.png)

## Task_2 Find all orders placed in January 2023.
---
SQL Query:
```sql
SELECT * FROM Orders WHERE OrderDate BETWEEN '2023-01-01' AND '2023-01-31';
```
![alt text](/images/image1.png)

## Task_3 Get the details of each order, including the customer name and email
SQL Query:
```sql
SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, Customers.Email
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```
![alt text](/images/image2.png)

## Task_4 List the products purchased in a specific order (e.g., OrderID = 1)
SQL Query:
```sql
SELECT Products.ProductName
FROM OrderItems
JOIN Products ON OrderItems.ProductID = Products.ProductID
WHERE OrderItems.OrderID = 1;
```
![alt text](/images/image3.png)

## Task_5 Calculate the total amount spent by each customer
SQL Query:
```sql
SELECT Customers.FirstName, Customers.LastName, SUM(Products.Price * OrderItems.Quantity) AS TotalAmountSpent
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Products ON OrderItems.ProductID = Products.ProductID
GROUP BY Customers.CustomerID;
```
![alt text](/images/image4.png)

## Task_6 Find the most popular product (the one that has been ordered the most)
SQL Query:
```sql
SELECT Products.ProductName, COUNT(OrderItems.OrderItemID) AS TotalOrders
FROM Products
JOIN OrderItems ON Products.ProductID = OrderItems.ProductID
GROUP BY Products.ProductID
ORDER BY TotalOrders DESC
LIMIT 1; 
```
![alt text](/images/image5.png)

## Task_7 Get the total number of orders and the total sales amount for each month in 2023
SQL Query:
```sql
SELECT DATE_FORMAT(Orders.OrderDate, '%Y-%m') AS Month, COUNT(Orders.OrderID) AS TotalOrders, SUM(Products.Price * OrderItems.Quantity) AS TotalSalesAmount FROM Orders JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID JOIN Products ON OrderItems.ProductID = Products.ProductID WHERE Orders.OrderDate BETWEEN '2023-01-01' AND '2023-12-31' GROUP BY Month
```
![alt text](/images/image6.png)

## Task_8 Find customers who have spent more than $1000.
SQL Query:
```sql
SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
JOIN Products ON OrderItems.ProductID = Products.ProductID
GROUP BY Customers.CustomerID
HAVING SUM(Products.Price * OrderItems.Quantity) > 1000;
```
![alt text](/images/image7.png)

