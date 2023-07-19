/*
    C - Create
    R - Read
    U - Update
    D - Delete
*/

/* create */

INSERT INTO
	users
    
( first_name, last_name, email_address )

VALUES
("Wilma", "Flinststone", "wilma@bedrock.com"),
("Baney", "Rubble", "barney@bedrock.com")

;

SELECT
	last_name,
    email_address
FROM
 users
 
WHERE
	last_name = 'Flinststone'
    
ORDER BY
	email_address DESC
    ;

SELECT
	last_name,
    email_address
FROM
 users
 
WHERE
	last_name = 'Flinststone'
    
ORDER BY
	email_address DESC -- DESCending  ASCending

;

UPDATE
	users
SET
	email_address="freddo@bedrock.com"
    
WHERE
	users.id = 2

    ;

DELETE FROM
	users
    
WHERE
	users.id = 4
    
    ;

SELECT
	*
FROM
  users
  
LEFT JOIN  cars ON cars.user_id = users.id
  
WHERE
	users.id = 2

    ;