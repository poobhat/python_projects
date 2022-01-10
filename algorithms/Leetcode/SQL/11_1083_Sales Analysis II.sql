Write an SQL query that reports the buyers who have bought S8 but not iPhone.
Note that S8 and iPhone are products present in the Product table.

Example 1:

Input:
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 1          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 3        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
Output:
+-------------+
| buyer_id    |
+-------------+
| 1           |
+-------------+
Explanation: The buyer with id 1 bought an S8 but did not buy an iPhone.
The buyer with id 3 bought both.

---------------------------------------------------------------------------
--Runtime: 1214 ms, faster than 35.12%
with temp as(
select
	s.buyer_id,
	p.product_name
from sales s
right join product p
on	p.product_id = s.product_id)

select distinct buyer_id
from temp
where
	product_name = 'S8'
	and buyer_id not in (
	select buyer_id
	from temp
	where product_name = 'iPhone');

--Runtime: 1579 ms, faster than 9.43%
select s.buyer_id
from
sales s join product p
on p.product_id = s.product_id
group by s.buyer_id
having sum(case when p.product_name = 'S8' then 1 else 0 end) > 0
and sum(case when p.product_name='iPhone' then 1 else 0 end) = 0;