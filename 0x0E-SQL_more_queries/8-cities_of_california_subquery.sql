-- this script list all cities
USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
