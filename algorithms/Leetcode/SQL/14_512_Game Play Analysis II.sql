Write an SQL query to report the device that is first logged in for each player.
Return the result table in any order.
The query result format is in the following example.
Example 1:
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+
--Runtime: 443 ms, faster than 95.12%
select
	a.player_id,
	a.device_id
from
	activity a
join (
	select
		player_id,
		min(event_date) as event_date
	from
		Activity
	group by
		player_id) as temp
on
	a.event_date = temp.event_date
	and a.player_id = temp.player_id;

--Runtime: 739 ms, faster than 14.83%
select distinct player_id
, first_value(device_id) over (partition by player_id order by event_date) device_id
from activity