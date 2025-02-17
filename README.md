# b12840c5-0324-41e8-acc4-a2e9f981ade0

Write a Bash script to extract and count the number of successful and failed login attempts from an authentication log (./auth.log) and save the results to ***ssh_login_report.log***

The output should have the following format

```
SSH Login Report
================

[Failed Logins]
[INFO] 10.0.0.1 - 1 failed login attempt(s)
[INFO] 192.168.1.100 - 2 failed login attempt(s)

[Successful Logins]
[INFO] 10.0.0.2 - 1 successful login attempt(s)
[INFO] 192.168.1.200 - 1 successful login attempt(s)
```

