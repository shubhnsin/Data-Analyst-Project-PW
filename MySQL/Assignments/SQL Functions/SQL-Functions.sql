-- ///// SECTION 1 : QUERIES ON WORLD DATABASE

-- Q1. Find the country with the highest population

SELECT
    Name,
    Population
FROM country
ORDER BY Population DESC
LIMIT 1;


-- Q2. Calculate total population of all cities for each country

SELECT
    c.Name AS country_name,
    SUM(ci.Population) AS total_city_population
FROM country AS c
INNER JOIN city AS ci
    ON c.Code = ci.CountryCode
GROUP BY c.Name;


-- Q3. Top 3 countries with the highest population density (Population per unit surface area)

SELECT
    Name,
    (Population / SurfaceArea) AS population_density
FROM country
WHERE SurfaceArea > 0
ORDER BY population_density DESC
LIMIT 3;


-- /////  SECTION 2 : QUERIES ON SAKILA DATABASE

-- Q4. Customer with the highest number of rentals

SELECT
    customer_id,
    COUNT(*) AS total_rentals
FROM rental
GROUP BY customer_id
ORDER BY total_rentals DESC
LIMIT 1;


-- Q5. Month that recorded the maximum number of rentals

SELECT
    MONTH(rental_date) AS rental_month,
    COUNT(*) AS total_rentals
FROM rental
GROUP BY rental_month
ORDER BY total_rentals DESC
LIMIT 1;


-- Q6. Total revenue generated on each day

SELECT
    DATE(payment_date) AS payment_day,
    SUM(amount) AS total_revenue
FROM payment
GROUP BY payment_day;


-- Q7. Store that generated the highest total revenue

SELECT
    s.store_id,
    SUM(p.amount) AS total_revenue
FROM store AS s
INNER JOIN staff AS st
    ON s.store_id = st.store_id
INNER JOIN payment AS p
    ON st.staff_id = p.staff_id
GROUP BY s.store_id
ORDER BY total_revenue DESC
LIMIT 1;


-- Q8. Number of customers who made exactly 5 payments
-- NOTE: In the standard Sakila dataset, this query returns 0 because no customer has exactly 5 payments.

SELECT
    COUNT(*) AS customers_with_5_payments
FROM (
    SELECT
        customer_id
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) = 5
) AS derived_table;


-- END OF FILE

