/* 1)
SELECT * FROM languages WHERE language = 'Slovene' order by percentage desc;

/* 2)
SELECT countries.name, COUNT(cities.id)
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name order by count(country_id) desc
*/

/* 3)
SELECT * FROM cities
WHERE country_code = 'Mex' AND population > 500000
*/

/* 4)
SELECT * FROM languages
WHERE percentage > 89
order by percentage desc
*/

/* 5)
SELECT name, surface_area, population FROM countries
where surface_area < 501 and population < 100000
*/

/* 6)
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75
*/

/* 7)
SELECT countries.name, cities.name, district, cities.population FROM countries
JOIN cities ON countries.code = cities.country_code
WHERE country_code = 'ARG' and district = 'Buenos Aires' and cities.population > 500000
*/

/* 8)
SELECT region, count(name) AS countries FROM countries
group by region
order by countries desc
*/