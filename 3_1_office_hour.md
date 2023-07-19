- users
    - id
    - first name : varchar( 45 ) ( string)
    - last name : varchar( 45 ) ( string)
    - email : varchar ( 255 )
    - address : varchar ()
        - parts
    - CC Number : char (16)



- orders ( 1:many )
    - size
    
- pizzas
    - toppings : Relationship
    - sizes
    - crust

- toppings
    - name : varchar(25)
    - blah: blah


- size
- 

1:many
many:many

one pizza many toppings