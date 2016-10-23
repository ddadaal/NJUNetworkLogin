
#Login and Logout Scripts for NJU Network#

Written in Python 3, these scripts provide a more convenient and cross-platform way to login and logout to NJU's Network. 

Configure your username and password by editing the login.py itself before executing it or you'll get a warning message and exit.

	username=""
	password="" 

----------------------------------------
Details:

The way to login and logout is simple. 

To login, we just post to URL: "http://p.nju.edu.cn/portal_io/login" with data formed as 
	
	username=*username*&password=*password*	

and the response is a JSON string including the following message:

1. reply\_code: Indicates the status of this login attempt. Some of them is listed here.

| Code | Description            |
|------|------------------------|
|1     | Successfully Logged in.|
|3     | Password is invalid.   |
|6     | Have logged in before. |



------------------------------------------

By the way, as I see, most NJU's network systems submit our username and password **without encrypting them**, not to mention that **they are still using HTTP**. This includes [p.nju.edu.cn](http://p.nju.edu.cn) and [jw.nju.edu.cn](http://jw.nju.edu.cn), the latter of which is important to us. Any one can capture one's username and password with ease.

So, for our security, please avoid logging in in a public network.

