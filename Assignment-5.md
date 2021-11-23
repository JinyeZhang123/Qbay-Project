## XSS Security Report

### We did two rounds of scanning. Why the results are different? 
Because cookies are not covered in the first scan while the second scan uses the cookies. Without cookies, the user cannot access the obejcts in homepage.


### What is the purpose of adding in the session id?
Session ID is used to respond to user interactions during a web session.

### Are all the possible XSS (script injection) links/routes covered in the table above? (think about any links that will render user inputs, such as 
### URL paramer, cookies, flask flash calls). If not, are those link/pages vulnerable to XSS?
Not all possible XSS links are covered in the table. Those links are vulnerable to XSS.


### XSS table
|              | URL                                                              | Parameter | XSS successful? |
| ------------ | ---------------------------------------------------------------- | --------- | --------------- |
| Scan         | [http://127.0.0.1:8081/](http://127.0.0.1:8081/)                 | password  | Yes             |
| Scan         | [http://127.0.0.1:8081/](http://127.0.0.1:8081/)                 | password  | Yes             |
| Scan         | [http://127.0.0.1:8081/register](http://127.0.0.1:8081/register) | password  | Yes             |
| Scan         | [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login)       | password  | Yes             |
| Scan(cookie) | [http://127.0.0.1:8081/](http://127.0.0.1:8081/)                 | password  | Yes             |
| Scan(cookie) | [http://127.0.0.1:8081/](http://127.0.0.1:8081/)                 | password  | Yes             |
| Scan(cookie) | [http://127.0.0.1:8081/register](http://127.0.0.1:8081/register) | password  | Yes             |
| Scan(cookie) | [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login)       | password  | Yes             |




