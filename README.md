# Automation Testing in Django

---
## Software Requirements
- python : 3.5
- django : 2.2.6


---
## Test Case Report in CMD Prompt [gif img]
	- Ubuntu Terminal 
	- => python3 manage.py test --keepdb login.tests.api.v1.test_login_user
<kbd><img src="/imgs-readme/tc-in-cmd_v1-1.gif" alt="django_default-page_v1-1" title="django_default-page"></img></kbd>

```
(venv) ashish@ashish-Vostro-3478:projdemo$ python3 manage.py test --keepdb login.tests.api.v1.test_login_user
Using existing test database for alias 'default'...
System check identified no issues (0 silenced).
POST, URL =  http://localhost:8001/login/api/v1/login-user/
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| Test  | Test  | Test  | Test  | Metho |  URL  | Test  | Expec | Actua | Stat |
| Case  | Scena | Case  | Suite |   d   |       | Data  | ted R | l Res |  us  |
|  ID   |  rio  |       |       |       |       |       | esult |  ult  |      |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+======+
| 1.1.1 | Login | Login | Check | POST  | login | param | 200   | 200   | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | valid | se st |       | gin-  |       |       |       |      |
|       |       | usern | atus  |       | user/ |       |       |       |      |
|       |       | ame & | code. |       |       |       |       |       |      |
|       |       | passw |       |       |       |       |       |       |      |
|       |       | ord.  |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.1.2 | Login | Login | Check | POST  | login | param | succe | succe | PASS |
|       | user  | user  | api r |       | /api/ | s     | ss    | ss    |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | valid | se st |       | gin-  |       |       |       |      |
|       |       | usern | atus. |       | user/ |       |       |       |      |
|       |       | ame & |       |       |       |       |       |       |      |
|       |       | passw |       |       |       |       |       |       |      |
|       |       | ord.  |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.1.3 | Login | Login | Check | POST  | login | param | ['You | ['You | PASS |
|       | user  | user  | api r |       | /api/ | s     | are s | are s |      |
|       | modul | with  | espon |       | v1/lo |       | ucces | ucces |      |
|       | e.    | valid | se me |       | gin-  |       | sfull | sfull |      |
|       |       | usern | ssage |       | user/ |       | y log | y log |      |
|       |       | ame & | .     |       |       |       | ged   | ged   |      |
|       |       | passw |       |       |       |       | in.'] | in.'] |      |
|       |       | ord.  |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.1.4 | Login | Login | Check | POST  | login | param | [{'to | [{'to | PASS |
|       | user  | user  | api r |       | /api/ | s     | ken': | ken': |      |
|       | modul | with  | espon |       | v1/lo |       | '1ff4 | '1ff4 |      |
|       | e.    | valid | se    |       | gin-  |       | 1d4ed | 1d4ed |      |
|       |       | usern | data. |       | user/ |       | a7953 | a7953 |      |
|       |       | ame & |       |       |       |       | e8633 | e8633 |      |
|       |       | passw |       |       |       |       | 05b2a | 05b2a |      |
|       |       | ord.  |       |       |       |       | 0a25c | 0a25c |      |
|       |       |       |       |       |       |       | 541b5 | 541b5 |      |
|       |       |       |       |       |       |       | 4c058 | 4c058 |      |
|       |       |       |       |       |       |       | b'}]  | b'}]  |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.2.1 | Login | Login | Check | POST  | login | param | 404   | 404   | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | inval | se st |       | gin-  |       |       |       |      |
|       |       | id us | atus  |       | user/ |       |       |       |      |
|       |       | ernam | code. |       |       |       |       |       |      |
|       |       | e & p |       |       |       |       |       |       |      |
|       |       | asswo |       |       |       |       |       |       |      |
|       |       | rd.   |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.2.2 | Login | Login | Check | POST  | login | param | error | error | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | inval | se st |       | gin-  |       |       |       |      |
|       |       | id us | atus. |       | user/ |       |       |       |      |
|       |       | ernam |       |       |       |       |       |       |      |
|       |       | e & p |       |       |       |       |       |       |      |
|       |       | asswo |       |       |       |       |       |       |      |
|       |       | rd.   |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.2.3 | Login | Login | Check | POST  | login | param | ['Inv | ['Inv | PASS |
|       | user  | user  | api r |       | /api/ | s     | alid  | alid  |      |
|       | modul | with  | espon |       | v1/lo |       | crede | crede |      |
|       | e.    | inval | se me |       | gin-  |       | ntial | ntial |      |
|       |       | id us | ssage |       | user/ |       | s!']  | s!']  |      |
|       |       | ernam | .     |       |       |       |       |       |      |
|       |       | e & p |       |       |       |       |       |       |      |
|       |       | asswo |       |       |       |       |       |       |      |
|       |       | rd.   |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.2.4 | Login | Login | Check | POST  | login | param | None  | None  | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | inval | se    |       | gin-  |       |       |       |      |
|       |       | id us | data. |       | user/ |       |       |       |      |
|       |       | ernam |       |       |       |       |       |       |      |
|       |       | e & p |       |       |       |       |       |       |      |
|       |       | asswo |       |       |       |       |       |       |      |
|       |       | rd.   |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.3.1 | Login | Login | Check | POST  | login | param | 400   | 400   | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | usern | se st |       | gin-  |       |       |       |      |
|       |       | ame & | atus  |       | user/ |       |       |       |      |
|       |       | witho | code. |       |       |       |       |       |      |
|       |       | ut pa |       |       |       |       |       |       |      |
|       |       | sswor |       |       |       |       |       |       |      |
|       |       | d.    |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.3.2 | Login | Login | Check | POST  | login | param | error | error | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | usern | se st |       | gin-  |       |       |       |      |
|       |       | ame & | atus. |       | user/ |       |       |       |      |
|       |       | witho |       |       |       |       |       |       |      |
|       |       | ut pa |       |       |       |       |       |       |      |
|       |       | sswor |       |       |       |       |       |       |      |
|       |       | d.    |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.3.3 | Login | Login | Check | POST  | login | param | ['Ple | ['Ple | PASS |
|       | user  | user  | api r |       | /api/ | s     | ase p | ase p |      |
|       | modul | with  | espon |       | v1/lo |       | rovid | rovid |      |
|       | e.    | usern | se me |       | gin-  |       | e     | e     |      |
|       |       | ame & | ssage |       | user/ |       | both  | both  |      |
|       |       | witho | .     |       |       |       | usern | usern |      |
|       |       | ut pa |       |       |       |       | ame   | ame   |      |
|       |       | sswor |       |       |       |       | and p | and p |      |
|       |       | d.    |       |       |       |       | asswo | asswo |      |
|       |       |       |       |       |       |       | rd!'] | rd!'] |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
| 1.3.4 | Login | Login | Check | POST  | login | param | None  | None  | PASS |
|       | user  | user  | api r |       | /api/ | s     |       |       |      |
|       | modul | with  | espon |       | v1/lo |       |       |       |      |
|       | e.    | usern | se    |       | gin-  |       |       |       |      |
|       |       | ame & | data. |       | user/ |       |       |       |      |
|       |       | witho |       |       |       |       |       |       |      |
|       |       | ut pa |       |       |       |       |       |       |      |
|       |       | sswor |       |       |       |       |       |       |      |
|       |       | d.    |       |       |       |       |       |       |      |
+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+
filename =  media/testcase/login/tests/api/v1/TestCaseReport_TestLoginUser.csv
.
----------------------------------------------------------------------
Ran 1 test in 0.308s

OK
Preserving test database for alias 'default'...

```


---
## TestCaseReport_TestLoginUser.csv
	- file open in LibreOffice Calc
<kbd><img src="/imgs-readme/screenshot-from-2019-10-20-22-54-00.png" alt="django_default-page_v1-1" title="django_default-page"></img></kbd>


---
## Postman Collection Link
- https://www.getpostman.com/collections/1b078e77e78bfb33876b

---
## Medium Article Link
- https://medium.com/@sondagarashish/8235fedfc61