/*
SELECT * FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE city_id = 312
*/

/*
SELECT title, description, release_year, rating, special_features, name AS genre FROM film_category
JOIN film ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE name = 'Comedy'
*/

/*
select film_actor.actor_id, first_name, last_name, title, release_year, description from film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 5
*/

/*
select concat(first_name, ' ' , last_name) AS Name, email, address FROM customer
JOIN address ON address.address_id = customer.address_id
WHERE city_id in (1, 42, 312, 459) and store_id = 1
*/

/*
SELECT * FROM film
JOIN actor on actor_id = actor.actor_id
WHERE actor_id = 15 and rating = 'G' and special_features LIKE '%Behind%'
*/

/*
SELECT film.film_id, title, first_name, last_name FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id = 369
*/

/*
SELECT title, description, release_year, rating, special_features, name AS genre FROM film
JOIN category on category_id = category.category_id
WHERE rental_rate = 2.99 and name = 'Drama'
*/

/*
SELECT title, description, release_year, rating, special_features, name AS genre, concat(first_name, ' ', last_name) FROM film
JOIN category on category_id = category.category_id
JOIN actor ON actor_id = actor.actor_id
WHERE last_name='KILMER' and first_name = 'SANDRA' and name = 'Action'
*/
