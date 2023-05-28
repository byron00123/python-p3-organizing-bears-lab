# lib/sql_queries.py

# Test 1
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        sex = 'F';
"""

# Test 2
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM
        bears
    ORDER BY
        name ASC;
"""

# Test 3
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM
        bears
    WHERE
        alive = true
    ORDER BY
        age ASC;
"""

# Test 4
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    ORDER BY
        age DESC
    LIMIT 1;
"""

# Test 5
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM
        bears
    ORDER BY
        age ASC
    LIMIT 1;
"""
