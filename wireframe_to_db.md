- users
    - id
    - first name : varchar( 45 ) ( string)
    - last name : varchar( 45 ) ( string)
    - email : varchar ( 255 )

- orders 
    - user ( 1:many user:orders FK=Foreign Key)
    
- pizzas
    - toppings : M2M Relationship
    - size
    - crust
    - order ( 1:many order:pizzas FK=Foreign Key)

/* For bonus challenge */

- toppings
    - name : varchar(25)
    - blah: blah

- pizza_topping
    - pizza_id
    - topping_id

- queries
    - Build as you complete each needed table
    - add 2 users
    - add 3 pizzas
        - for Bonus challenge
            - add at least 2 toppings to each pizza using a many-to-many relationship
        - Skip toppings if you did not add the toppings and pizza_topings tables
    - create an order for one of the users
        - 2 pizzas