## Register_test: CISIC-CMPE-327_GROUP23/qbay_test/frontend/register_test.py/

### Input Coverage 
1. Success. All the inputs are valid.
2. Fail. Invalid inputs.
    * Invalid email (uncorrect email format) 
    * Invalid name (name length has to be longer then 2)
    * Invalid password (password has to match)

### Output Coverage
1. Success. All the inputs are valid. Output ture.
2. Fail. Invalid email. Output false.

### Functionality Covergae
Similar with output coverage.
Functionality: registertion.

1. Success. All the inputs are valid. register successfully.
2. Fail. Invalid email. register failed.



## login_test: CISIC-CMPE-327_GROUP23/qbay_test/frontend/login_test.py/

### Input Coverage 
1. Success. All the inputs are valid.
2. Fail. Invalid inputs.
    * Invalid email (email has to follow email format) 
    * Invalid password (wrong password)

### Output Coverage
1. Success. All the inputs are valid. Output ture.
2. Fail. Invalid password. Output false.

### Functionality Covergae
Similar with output coverage.
Functionality: login.

1. Success. All the inputs are valid. login successfully.
2. Fail. Invalid password. Update failed.


## update_user_profile_test: CISIC-CMPE-327_GROUP23/qbay_test/frontend/update_user_profile_test.py/

### Input Coverage 
1. Success. All the inputs are valid.
2. Fail. Invalid inputs.
    * Invalid email (email has to follow email format) 
    * Invalid name (username length has to be greater then 2)
    * Invalid address (address have to follow address format)
    * Invalid postcode (postcode have to follow canada postcode format)

### Output Coverage
1. Success. All the inputs are valid. Output ture.
2. Fail. Invalid postcode. Output false.

### Functionality Covergae
Similar with output coverage.
Functionality: update user profile.

1. Success. All the inputs are valid. login successfully.
2. Fail. Invalid postcode. Update failed.


## create_product_test: CISIC-CMPE-327_GROUP23/qbay_test/frontend/create_product_test.py/

### Input Coverage 
1. Success. All the inputs are valid.
2. Fail. Invalid inputs.
    * Invalid title (title must be alphanumeric) 
    * Invalid description (description must be longer than title)
    * Invalid price (price must be higher than 10)
    * Invalid date (date must not be further than 2025)
    * Invalid owner email (email must follow the requirements)

### Output Coverage
1. Success. All the inputs are valid. Output ture.
2. Fail. Invalid price. Output false.

### Functionality Covergae
Similar with output coverage.
Functionality: create product.

1. Success. All the inputs are valid. Create product successfully.
2. Fail. Invalid price. Creation failed.



## update_product_test: CISIC-CMPE-327_GROUP23/qbay_test/frontend/update_product_test.py/

### Input Coverage 
1. Success. All the inputs are valid.
2. Fail. Invalid inputs.
    * Invalid title (title must be alphanumeric) 
    * Invalid description (description must be longer than title)
    * Invalid price (price must be higher than 10)

### Output Coverage
1. Success. All the inputs are valid. Output ture.
2. Fail. Invalid title. Output false.

### Functionality Covergae
Similar with output coverage.
Functionality: update product.

1. Success. All the inputs are valid. Update product successfully.
2. Fail. Invalid title. Update failed.
