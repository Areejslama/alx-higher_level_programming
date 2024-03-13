-- this script  lists all cities contained in the database
-- this script list all cities
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
