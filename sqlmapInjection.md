###SQL Injection Test Report

###1. Are all the user input fields in your application covered in all the test cases above? Any successful exploit?
All the fields defined in our model has been tested and all the test cases have passed successfully. There is no exploit.

###2. We did two rounds of scanning. Why the results are different? What is the purpose of adding in the session id?
The second test is tested through cookies (session ID), so there include more injections. Adding session ID so that the testing protocol can interact with 
more modules (accessible after logging in).

###3. Summarize the injection payload used based on the logs, and briefly discuss the purpose.
All the injections have 2 trials, such that the testing is sufficient enough to exploit all vulnerabilities and is time efficient at the same time.


###SQL Injection Test Table
|               | Route/URL                                                                                | Parameter    | 2 | Number of Successful Trials |
| ------------- | ---------------------------------------------------------------------------------------- | ------------ | - | --------------------------- |
| Scan          | [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login)                               | email        | 2 | 2                           |
| Scan          | [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login)                               | password     | 2 | 2                           |
| Scan          | [http://127.0.0.1:8081/register](http://127.0.0.1:8081/register)                         | email        | 2 | 2                           |
| Scan          | [http://127.0.0.1:8082/register](http://127.0.0.1:8081/register)                         | name         | 2 | 2                           |
| Scan          | [http://127.0.0.1:8083/register](http://127.0.0.1:8081/register)                         | password     | 2 | 2                           |
| Scan          | [http://127.0.0.1:8084/register](http://127.0.0.1:8081/register)                         | password2    | 2 | 2                           |
| Scan (cookie) | http://127.0.0.1:8081/create\_product                                                    | title        | 2 | 2                           |
| Scan (cookie) | http://127.0.0.1:8082/create\_product                                                    | description  | 2 | 2                           |
| Scan (cookie) | http://127.0.0.1:8083/create\_product                                                    | price        | 2 | 2                           |
| Scan (cookie) | http://127.0.0.1:8084/create\_product                                                    | date         | 2 | 2                           |
| Scan (cookie) | http://127.0.0.1:8085/create\_product                                                    | owner\_email | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8081/update\_product](http://127.0.0.1:8081/update_product)            | title        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8082/update\_product](http://127.0.0.1:8081/update_product)            | new\_title   | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8083/update\_product](http://127.0.0.1:8081/update_product)            | description  | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8084/update\_product](http://127.0.0.1:8081/update_product)            | price        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8080/](http://127.0.0.1:8081/)                                         | email        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8081/](http://127.0.0.1:8081/)                                         | password     | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8081/update\_user\_profile](http://127.0.0.1:8081/update_user_profile) | email        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8082/update\_user\_profile](http://127.0.0.1:8081/update_user_profile) | name         | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8083/update\_user\_profile](http://127.0.0.1:8081/update_user_profile) | address      | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8084/update\_user\_profile](http://127.0.0.1:8081/update_user_profile) | postcode     | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8081/register](http://127.0.0.1:8081/register)                         | email        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8082/register](http://127.0.0.1:8081/register)                         | name         | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8083/register](http://127.0.0.1:8081/register)                         | password     | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8084/register](http://127.0.0.1:8081/register)                         | password2    | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login)                               | email        | 2 | 2                           |
| Scan (cookie) | [http://127.0.0.1:8082/login](http://127.0.0.1:8081/login)                               | password     | 2 | 2                           |


