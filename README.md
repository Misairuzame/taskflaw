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

https://github.com/tonimobin/cyber-security-base-2022/blob/4f16cb171f7628d3640bf5c6ea6f5c1c615b473f/noteproject/noteproject/settings.py#L85-L98

###### Fix: 
Make sure you're aware of the default settings and their pitfalls - react accordingly, in this case turn debug off in production and hide the secret key. Proper error handling is also necessary in order to avoid leaking sensitive information about the system. 

In regards to the password validation, improvement could be achieved by various different ways. One could create a filter based on [popular passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords). This filter would block the use of common passwords. Django also has its own common password validator, which could be implemented by adding the following to the code snippet shown above:

`{ 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' }`


## Flaw 2: A10:2017 - Insufficient Logging & Monitoring

###### Problem: 
When your software becomes a target of an attack, it is extremely important to become aware of this attack before the system is breached. Logging plays a major role in preventing breaches by alerting the system administrator of suspicious activity. If there is no logging, the attacker is essentially given a peaceful environment to hone their attack further.

In this software the logging has been disabled as can be seen below. If there was an attack such as the one described in Flaw #1 (a brute-force script that guesses passwords), there would be thousands if not hunders of thousands of logging attempts. When there is no logging, the system administrator is not aware of these logging attempts. If they became aware of these attempts, they'd know that they are under an attack and could then act accordingly. 

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/14b9cc93bba3b94b96cec5c680a838df3a90dc0b/noteproject/noteproject/settings.py#L123-L135


###### Fix: 
In this software you could simply turn the `disable_existing_loggers` from `True` to `False` and you'd get some basic logging. Building a robust logging system is a more complex task that should be kept in mind throughout the development life cycle. Some core concepts that should kept in mind are unmodifiability of the logs, the intruder should not be able to modify the logs. Time stamps are vital as well, because with their aid it's possible to re-construct events and thus understand the causes and effects of different actions that have happened in the system. 

## Flaw 3: A5:2017 - Broken Access Control

###### Problem: 
Broken access control refers to situations where resources on the server are accessible when they shouldn't be. Situations like this may arise from various different events, but are often related to loose specification of user rights or functions which can be executed without adequate rights. 

In this application, it's currently possible to access notes of different users via url modification. This is not desirable as if the data is sensitive, surely you wouldn't want random people accessing it.

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/0e73413559813884a99abe660a96d20542f62dd5/noteproject/notes/views.py#L24-L27


###### Fix: 
To fix broken access control related issues, extra attention should be paid towards testing different views and making sure sensitive data is accessible only by suitable user groups. To fix the BAC issue in this software, you can restrict accessibility of the individual notes by, in this case, adding a `LoginRequiredMixin` to the class associated with the vulnerability - in this case the NoteDetail. After the edit, the class definition would look like this:

`class NoteDetail(LoginRequiredMixin, DetailView)`

This will limit the accessability of the notes to authenticated users only.
## Flaw 4: A3:2017 - Sensitive Data Exposure

###### Problem: 
Sensitive Data Exposure (SDE) refers to situations, where sensitive data is not protected properly. Sensitive data could be passwords, corporate secrets, basically anything you wouldn't want 'outsiders' to get access to. It's common that some data may seem secure, but in one way or another it's leaking - maybe it's transported to the server in an insecure way and the data can be hijacked during the transportation. Maybe it's stored in plain text, which is something you do not want to do. Encryption of some sort is necessary.

In this application, during login process, the user data is transported without proper encryption (via HTTP) and the data contained in the POST method (username and password) can be hijacked. When the hijacker looks at the data, they'll see the username and password in plain text.

###### Location: 

###### Fix: 
It would be a good idea to use a more secure way of transportation, such as SSL or HTTPS. When using these, the data will be sent in encrypted format and if hijacked, the hijacker can't make sense of the data because they won't have the required key to decrypt the data. 


## Flaw 5: 


