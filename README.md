# Cyber Security Base 2022, Project I

## Software with security flaws

The objective of this project is to build a small application with five or more [**OWASP Top Ten**](https://owasp.org/www-project-top-ten/) flaws. Once the faulty software has been built, instructions for fixing the flaws will be provided. 

More information about the course can be found here: https://cybersecuritybase.mooc.fi/module-3.1
## Pictures of the software, a small note/task application with basic CRUD functionalities

![Screenshot 2022-03-14 at 15 31 28](https://user-images.githubusercontent.com/85210617/158183129-d7a6d047-d1b1-4259-8e51-721d6ad35424.png)

![Screenshot 2022-03-14 at 15 31 04](https://user-images.githubusercontent.com/85210617/158183156-62b158a2-9bca-414e-9e3b-0a33bda63491.png)

![Screenshot 2022-03-14 at 15 33 44](https://user-images.githubusercontent.com/85210617/158183216-37b21993-f10d-470d-9a67-e54bb796ec8e.png)

## Installation

1. Open your terminal and cd to the folder where you want the software to be installed
2. (Assuming you have git installed) Execute the following command: <br/>
`git clone git@github.com:tonimobin/cyber-security-base-2022.git`
3. (Assuming you have Django & Python installed) cd to the project folder and start the server with the following command: <br/>
`python manage.py runserver`
4. Go to 'localhost:8000' in your browser and the application should be running.
5. If you run into any issues, refer to the [Installation guide](https://cybersecuritybase.mooc.fi/installation-guide) - I've tried to explain the problems in such manner that running the project is not 100% required, in case you are not able to get it running.

## Flaw 1: A03:2017 - Sensitive Data Exposure

###### Problem: 
Sensitive Data Exposure (SDE) refers to situations, where sensitive data is not protected properly. Sensitive data could be passwords, corporate secrets, basically anything you wouldn't want 'outsiders' to get access to. It's common that some data may seem secure, but in one way or another it's leaking - maybe it's transported to the server in an insecure way and the data can be hijacked during the transportation. Maybe it's stored in plain text, which is something you do not want to do. Encryption of some sort is necessary.

In this application, during login process, the user data is transported without proper encryption (via HTTP) and the data contained in the POST method (username and password) can be hijacked. When the hijacker looks at the data, they'll see the username and password in plain text. In the picture below you can see a Wireshark capture, where the user 'Joe' logs in to the application. His password is 'JoePassword'. Both the username and the password can be seen in plain text.

![Screenshot 2022-03-14 at 11 00 34](https://user-images.githubusercontent.com/85210617/158142284-f1317501-dd92-42b8-a77f-1f4b9958240e.png)

###### Location: 

https://github.com/tonimobin/cyber-security-base-2022/blob/02c01a280607606b546ce522c0b2c61fef95b12a/noteproject/notes/templates/notes/login.html#L7-L14

###### Fix: 
It would be a good idea to use a more secure way of transportation, such as SSL or HTTPS. When using these, the data will be sent in encrypted format and if hijacked, the hijacker can't make sense of the data because they won't have the required key to decrypt the data. 


## Flaw 2: A07:2017 - Cross-Site Scripting(XSS):

###### Problem: 
Cross-site scripting (XSS) refers to a situation, where the attacker is able to place malicious code into a site, which is then executed on the victims machine. Situations like this may arise from differents sorts of inputs and search functionalities - basically anything where the user is able to enter input in some form and then this input isn't handled properly.

In this application, when creating a new note - the title field is not sanitized, which means it's possible to enter malicious code and have it execute when the new note is submitted. You could for example enter the following title and once you submit the note, an alert will pop up.

`Remember to buy pasta<script>alert('This could have been malicious code!');</script>.`


###### Location: 

https://github.com/tonimobin/cyber-security-base-2022/blob/f242ef460efcb9bd3b992c3df1ca015a1e4a63a3/noteproject/notes/templates/notes/note_list.html#L36-L39

###### Fix: 
Using Django provided templates should protect you quite well, in this example the vulnerability was induced by the use of the safe-keyword. So be careful, if you use it. In this case, you can simply remove the safe pipe from line 38 and after the removal, the script will be processed as a string when submitted and thus no longer executable.

## Flaw 3: A05:2017 - Broken Access Control

###### Problem: 
Broken access control refers to situations where resources on the server are accessible when they shouldn't be. Situations like this may arise from various different events, but are often related to loose specification of user rights or functions which can be executed without adequate rights. 

In this application, it's currently possible to access notes of different users via url modification. This is not desirable as if the data is sensitive, surely you wouldn't want random people accessing it.

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/0e73413559813884a99abe660a96d20542f62dd5/noteproject/notes/views.py#L24-L27


###### Fix: 
To fix broken access control related issues, extra attention should be paid towards testing different views and making sure sensitive data is accessible only by suitable user groups. To fix the BAC issue in this software, you can restrict accessibility of the individual notes by, in this case, adding a `LoginRequiredMixin` to the class associated with the vulnerability - in this case the NoteDetail. After the edit, the class definition would look like this:

`class NoteDetail(LoginRequiredMixin, DetailView)`

This will limit the accessibility of the notes to authenticated users only.

## Flaw 4: A06:2017 - Security Misconfiguration

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


## Flaw 5: A10:2017 - Insufficient Logging & Monitoring

###### Problem: 
When your software becomes a target of an attack, it is extremely important to become aware of this attack before the system is breached. Logging plays a major role in preventing breaches by alerting the system administrator of suspicious activity. If there is no logging, the attacker is essentially given a peaceful environment to hone their attack further.

In this software the logging has been disabled as can be seen below. If there was an attack such as the one described in Flaw #1 (a brute-force script that guesses passwords), there would be thousands if not hunders of thousands of logging attempts. When there is no logging, the system administrator is not aware of these logging attempts. If they became aware of these attempts, they'd know that they are under an attack and could then act accordingly. 

###### Location: 
https://github.com/tonimobin/cyber-security-base-2022/blob/14b9cc93bba3b94b96cec5c680a838df3a90dc0b/noteproject/noteproject/settings.py#L123-L135


###### Fix: 
In this software you could simply turn the `disable_existing_loggers` from `True` to `False` and you'd get some basic logging. Building a robust logging system is a more complex task that should be kept in mind throughout the development life cycle. Some core concepts that should kept in mind are unmodifiability of the logs, the intruder should not be able to modify the logs. Time stamps are vital as well, because with their aid it's possible to re-construct events and thus understand the causes and effects of different actions that have happened in the system. 
