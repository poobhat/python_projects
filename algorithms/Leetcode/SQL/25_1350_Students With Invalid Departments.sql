Table: Departments
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key of this table.
The table has information about the id of each department of a university.

Table: Students
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
| department_id | int     |
+---------------+---------+
id is the primary key of this table.
The table has information about the id of each student at a university and the id of the
department he/she studies at.

Write an SQL query to find the id and the name of all students who are enrolled in departments
that no longer exist.
Return the result table in any order.

The query result format is in the following example.
Example 1:
Input:
Departments table:
+------+--------------------------+
| id   | name                     |
+------+--------------------------+
| 1    | Electrical Engineering   |
| 7    | Computer Engineering     |
| 13   | Bussiness Administration |
+------+--------------------------+
Students table:
+------+----------+---------------+
| id   | name     | department_id |
+------+----------+---------------+
| 23   | Alice    | 1             |
| 1    | Bob      | 7             |
| 5    | Jennifer | 13            |
| 2    | John     | 14            |
| 4    | Jasmine  | 77            |
| 3    | Steve    | 74            |
| 6    | Luis     | 1             |
| 8    | Jonathan | 7             |
| 7    | Daiana   | 33            |
| 11   | Madelynn | 1             |
+------+----------+---------------+
Output:
+------+----------+
| id   | name     |
+------+----------+
| 2    | John     |
| 7    | Daiana   |
| 4    | Jasmine  |
| 3    | Steve    |
+------+----------+
Explanation:
John, Daiana, Steve, and Jasmine are enrolled in departments 14, 33, 74, and 77 respectively.
department 14, 33, 74, and 77 do not exist in the Departments table.
---------------------------------------------------------------------------------------------
-- Runtime: 706 ms, faster than 65.30%
select s.id, s.name from Students s
left join Departments d on s.department_id = d.id
where d.id is null

--Runtime: 643 ms, faster than 85.87%
select id, name from Students where department_id not in (select id from Departments);

--If the datasets are huge, this query might be slower than usual left join.
--NOT IN is a very expensive operation in SQL because every value should be sequentially
--checked against all values from the inner select query. In the given example,
--each department_id will be checked against each id from Departments table.