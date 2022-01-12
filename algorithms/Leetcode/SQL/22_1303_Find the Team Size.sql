Table: Employee
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id is the primary key for this table.
Each row of this table contains the ID of each employee and their respective team.

Write an SQL query to find the team size of each of the employees.
Return result table in any order.

The query result format is in the following example.
Example 1:
Input:
Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Output:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
Explanation:
Employees with Id 1,2,3 are part of a team with team_id = 8.
Employee with Id 4 is part of a team with team_id = 7.
Employees with Id 5,6 are part of a team with team_id = 9.
---------------------------------------------------------------------------------------------

--Runtime: 403 ms, faster than 12.85%
select
	employee_id,
	team_size
from
	Employee t1
left join
(
	select
		team_id,
		count(distinct employee_id) as team_size
	from
		Employee
	group by
		team_id) t2 on
	t1.team_id = t2.team_id
--Runtime: 380 ms, faster than 16.42%
select employee_id, count(team_id) over(partition by team_id) as team_size from Employee