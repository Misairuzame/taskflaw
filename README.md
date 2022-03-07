# Cyber Security Base 2022, Project I

## Software with security flaws

The objective of this project is to build a software with five or more **OWASP Top Ten** flaws. Once the faulty software has been built, instructions for fixing the flaws will be provided. 

More information about the course can be found here: https://cybersecuritybase.mooc.fi/module-3.1

## Flaw 1: A6:2017 - Security Misconfiguration

###### Problem: 
Security misconfiguration refers to a wide area of problems. Often related to improperly configured permissions, default settings, problematic error handling and out-of-date components. It is clear that many of the errors done in this area might go unnoticed, as even default settings may cause security issues in certain situations. 
In this app, the default settings are troublesome. The `SECRET_KEY` is left visible and `DEBUG`is `True` by default. Django itself warns about these issues as can be seen from the comments, but unfocused developers might forget to change these values. Secret keys should always be... secret. Debug is problematic in production, because it might reveal too much information about the inner workings of the system and simultaneously leak sensitive data or information.

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/b9ff5473027c61742334d2e0d3fbbaf14e8527ff/noteproject/noteproject/settings.py#L22-L26

###### Fix: Make sure you're aware of the default settings and their pitfalls - react accordingly, in this case turn debug off in production and hide the secret key. Proper error handling is also necessary in order to avoid leaking sensitive information about the system. 

## Flaw 2: 

## Flaw 3: 

## Flaw 4: 

## Flaw 5: 

Software with security flaws, as a part of the course "Cyber Security Base 2022, Project I", which can be found here: https://cybersecuritybase.mooc.fi/module-3.1


