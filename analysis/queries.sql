-- queries
select *
from constructors;


select *
from drivers;


select d.given_name || ' ' || d.family_name as name,
    sum(points) as totPoints
from results r
    join drivers d on r.driver_id = d.driver_id
GROUP by r.driver_id
order by 2 desc;


select c.name as name,
    sum(points) as totPoints
from results r
    join constructors c on r.constructor_id = c.constructor_id
GROUP by r.constructor_id
order by 2 desc;


select driver_id,
    round(avg(position), 2) as avgPos
from results
where status != 'Did not start'
GROUP BY driver_id
having count(*) >= 10
ORDER BY avgPos;