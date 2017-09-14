#SELECT sum(amount) FROM billing

/*
SELECT sum(amount)
FROM billing
WHERE client_id = 2
*/

/*
SELECT count(created_datetime) FROM sites
WHERE client_id = 1

SELECT count(created_datetime) FROM sites
WHERE client_id = 20
*/

/*
SELECT * FROM leads
WHERE DATE(registered_datetime) >= '2011-01-01' AND DATE(registered_datetime) <= '2011-02-15';
*/

/*
SELECT concat(first_name, ' ', last_name), count(site_id) FROM clients
JOIN sites ON clients.client_id = sites.client_id 
GROUP BY sites.client_id
*/

SELECT concat(clients.first_name, ' ', clients.last_name) AS client_name, sum(amount), billing.charged_datetime 
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, YEAR(billing.charged_datetime), MONTH(billing.charged_datetime)
