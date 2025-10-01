use retail_mysql -- Using Retail database
 select * from customers_data
-- Earliest And Latest date of an Order
select min(OrderDate), max(OrderDate) from orders_data;


-- Top 10 Customers ( By total spending )
select c.CustomerID, c.Name,sum(o.Quantity * p.Price) as total_spent
from orders_data o
join customers_data c on c.CustomerID = o.CustomerID
join product_data p on p.ProductID = o.ProductID
group by c.CustomerID,c.Name
order by total_spent desc
limit 10; 


-- The customer who never orders anything...
select c.CustomerID , c.Name from customers_data c
left join orders_data o on  c.CustomerID = o.CustomerID
where OrderID is null;


-- Top 5 Sold Product ( By Quantity )
select p.ProductName, sum(o.quantity) as total_sold
from orders_data o
join product_data p on p.ProductID = o.OrderID
group by p.ProductID,p.ProductName
order by total_sold desc
limit 5;


-- Products that are never ordered
select p.ProductID, p.ProductName from product_data p
left join orders_data o on p.ProductID = o.ProductID
where o.OrderID is null;


-- Monthly Revenue
select year(o.OrderDate) as Year, month(o.OrderDate) as Month, sum(o.Quantity * p.Price) as Revenue
from orders_data o
join product_data p on p.ProductID = o.ProductID
group by year(o.OrderDate),month(o.OrderDate)
order by Year,Month;

-- Total Discount Given
SELECT SUM(o.Quantity * p.Price * o.Discount) AS total_discount
FROM orders_data o
JOIN product_data p ON o.ProductID = p.ProductID;


-- Top Three Products which Contributes Most Revenue 
select p.Category,sum(o.Quantity * p.Price) as Revenue
from product_data p
join orders_data o on o.ProductID = p.ProductID
group by p.Category
order by Revenue desc
limit 3;





