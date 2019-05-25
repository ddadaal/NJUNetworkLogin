
# Login and Logout Scripts for NJU Network

This repo provides various ways to login to NJU Network with ease. They can be used to automate your workflow.

## PowerShell

Since PowerShell is open source and the default terminal in Windows, using PowerShell cmdlet to login to NJU network seems to be excellent.

### Usage

1. Edit login.ps1 and input your username and password in the specified place
2. execute `./login.ps1` under `./powershell`


### Register PowerShell Login Script Globally

It is so convenient and time-saving if you can just `njulogin` in your terminal and your device automatically login to NJU network.

Follow the steps:

- Open a PowerShell console
- If you have not created a PowerShell profile (find it out by executing `Test-Path $profile`), execute `New-Item -path $profile -type file –force` to create one
- Open your profile file (find its path by executing `$profile`)
- Copy content in `login.ps1` except the last line (`njulogin`) into it
- Set your username and password
- And that's all! You can just type `njulogin` and you are logged in.

Notes:

- Do these steps in a standalone PowerShell terminal. Don't do it in VSCode Integrated Console! It has different profile.



## Python

Prerequisites: Python 3 and requests

Written in Python 3, these scripts provide a more convenient and cross-platform way to login and logout to NJU's Network. 

Configure your username and password by editing the login.py itself before executing it or you'll get a warning message and exit.

```python
	username=""
	password="" 
```


# Details

The way to login and logout is simple. 

To login, just post to URL: "http://p.nju.edu.cn/portal_io/login" with data formed as 
	
```
username=*username*&password=*password*	
```

and the response is a JSON string including some messages like reply\_code, real name, balance, total time online and more.

The names in this JSON are so explicit that I don't think it's necessary to explain them. But some of possible reply\_code s are listed here.

| Code | Description             |
| ---- | ----------------------- |
| 1    | Successfully Logged in. |
| 3    | Password is invalid.    |
| 6    | Have logged in before.  |

-----------------------------------------------------------------------------

To log out, get "http://p.nju.edu.cn/portal_io/logout" directly and done.

The response includes reply\_code 101 and message "已登出" but who cares.


------------------------------------------

By the way, as I see, most NJU's network systems submit our username and password **without encrypting them**, not to mention that **they are still using HTTP**. This includes [p.nju.edu.cn](http://p.nju.edu.cn) and [jw.nju.edu.cn](http://jw.nju.edu.cn), the latter of which is important to us. Any one can capture one's username and password with ease.

So, for our security, please avoid logging in in a public network.

