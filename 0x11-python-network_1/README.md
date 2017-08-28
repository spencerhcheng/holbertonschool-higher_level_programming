## 0x10 Python - Network #1

![NETWORKING](https://caktus-website-production-2015.s3.amazonaws.com/media/blog-images/python-logo-3.6.gif)

#### AUTHOR
Spencer Cheng: [github account](https://github.com/spencerhcheng), [twitter](https://twitter.com/spencerhcheng)

#### ENVIRONMENT
All files are written and compiles on `Ubuntu 14.04 LTS`. The first line of bash scripts will be exactly `#!/usr/bin/python3`. Python scripts are checked using `PEP8` style guidelines.

### OBJECTIVES
Learning points:
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

#### 0. What's my status? #0
Python script that fetches [https://intranet.hbtn.io/status] using the package `urllib`.

Example:
```
spencer@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
spencer@ubuntu:~/0x11$
```

File: 0-hbtn_status.py

#### 1. Response header value #0
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response using `urllib` and `sys`.

Example:
```
spencer@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
spencer@ubuntu:~/0x11$ 
spencer@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
spencer@ubuntu:~/0x11$ 
```

File: 1-hbtn_header.py

#### 2. POST an email #0
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

Example:
```
spencer@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
spencer@ubuntu:~/0x11$ 
```

File: 2-post_email.py

#### 3. Error code #0
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). Manages `urllib.error.HTTPerror` exceiptions and prints the HTTP status code.

Example:
```
spencer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
spencer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
spencer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
spencer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
spencer@ubuntu:~/0x11$ 
```
#### 4. What's my status? #1
Python script that fetches https://intranet.hbtn.io/status

Example:
```
spencer@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
spencer@ubuntu:~/0x11$ 
```
File: 4-hbtn_status.py

#### 5. Response header value #1
Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.

Example:
```
spencer@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
spencer@ubuntu:~/0x11$ 
spencer@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
spencer@ubuntu:~/0x11$ 
```

File: 5-hbtn_header.py

#### 6. POST an email #1
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

Example:
```
spencer@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
spencer@ubuntu:~/0x11$
```
File: 6-post_email.py

#### 7. Error code #1
Python script that takes in a URL, sends a request to the URL and displays the body of the response.

Example:
```
spencer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
spencer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
spencer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
spencer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
spencer@ubuntu:~/0x11$ 
```

File: 7-error_code.py

#### 8. Search API
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

Example:
```
spencer@ubuntu:~/0x11$ ./8-json_api.py 
No result
spencer@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
spencer@ubuntu:~/0x11$ ./8-json_api.py 2
No result
spencer@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
spnecer@ubuntu:~/0x11$ 
```

File: 8-json_api.py

#### 9. Star Wars API #0
Python script that takes in a string and sends a search request to the Star Wars API.

Example:
```
spencer@ubuntu:~/0x11$ ./9-starwars.py r2
Number of result: 1
R2-D2
spencer@ubuntu:~/0x11$ ./9-starwars.py lu
Number of result: 2
Luke Skywalker
Luminara Unduli
guillaume@ubuntu:~/0x11$ ./9-starwars.py ju
Number of result: 0
spencer@ubuntu:~/0x11$ ./9-starwars.py g
Number of result: 16
Leia Organa
Biggs Darklighter
Greedo
Wedge Antilles
IG-88
Qui-Gon Jinn
Nute Gunray
Rugor Nass
Gasgano
Adi Gallia
spencer@ubuntu:~/0x11$
```

File: 9-starwars.py

#### 10. My Github!
Python script that takes my Github credentials (username and password) and uses the Github API to display my `id`.

Example:
```
spencer@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
spencer@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
spencer@ubuntu:~/0x11$ 
```

File: 10-my_github.py
