# SecondOrder-SQLi
Second Order SQL Injection Detection and Mitigation using proxy servers

# Original Paper
REFERENCES
[1] Ping, C. (2017). A second-order sql injection detection method. In 2017
IEEE 2nd Information Technology, Networking, Electronic and Automa-
tion Control Conference (ITNEC), (pp. 1792–1796).


# Problem Definition
Second-order SQL injection occurs when an application stores user-supplied data and later incorporates it into SQL queries in an unsafe way. Second-order SQL injection is a serious threat to Web applications and is more difficult to detect than first-order SQL injection. The attack payload of second-order SQL injection is from untrusted user input and stored in a database or file system, the SQL statement submitted by a web application is usually dynamically assembled by a trusted constant string in the program and untrusted user input, and the DBMS is unable to distinguish the trusted and untrusted part of a SQL statement.

# Detection Mechanism
The research suggests a second-order SQL injection threat detection method based on I.S.R. (Instruction Set Randomization). To build new SQL instruction sets instantly, the strategy inserts a proxy server before DBMS and randomly generates the trusted SQL keywords in Web applications. The proxy determines whether the supplied SQL command contains common keywords to recognize attack behavior. Experimental results show that this system can efficiently detect second-order. Attacks using SQL injection are frequent, and they process quickly.
