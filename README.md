# Cyber Security Base 2022, Project I

## Software with security flaws

The objective of this project is to build a software with five or more [**OWASP Top Ten**](https://owasp.org/www-project-top-ten/) flaws. Once the faulty software has been built, instructions for fixing the flaws will be provided. 

More information about the course can be found here: https://cybersecuritybase.mooc.fi/module-3.1

## Installation

1. Open your terminal and cd to the folder where you want the software to be installed
2. (Assuming you have git installed) Execute the following command: <br/>
`git clone git@github.com:tonimobin/cyber-security-base-2022.git`
3. Step 3
4. Step 4
5. Step 5

## Flaw 1: A6:2017 - Security Misconfiguration

###### Problem: 
Security misconfiguration refers to a wide area of problems. Often related to improperly configured permissions, default settings, problematic error handling and out-of-date components. It is clear that many of the errors done in this area might go unnoticed, as even default settings may cause security issues in certain situations. 
In this app, the default settings are troublesome. The `SECRET_KEY` is left visible and `DEBUG`is `True` by default. Django itself warns about these issues as can be seen from the comments, but unfocused developers might forget to change these values. Secret keys should always be... secret. Debug is problematic in production, because it might reveal too much information about the inner workings of the system and simultaneously leak sensitive data or information.
The app also seemingly has password validation, but on closer inspection it is lacking. For example common passwords are not prevented and this makes the system suspectible to brute-force scripts that try to guess the password. The admin user has the password 'admin', which is extremely bad and should not be allowed.

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/b9ff5473027c61742334d2e0d3fbbaf14e8527ff/noteproject/noteproject/settings.py#L22-L26

###### Fix: 
Make sure you're aware of the default settings and their pitfalls - react accordingly, in this case turn debug off in production and hide the secret key. Proper error handling is also necessary in order to avoid leaking sensitive information about the system. In regards to the password validation, improvement could be achieved by various different ways. One could create a filter based on [popular passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords). This filter would block the use of common passwords. Django also has its own common password validator, which could be implemented by adding the following to the code snippet shown above:
`{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' }`


## Flaw 2: 

## Flaw 3: 

## Flaw 4: 

## Flaw 5: 


