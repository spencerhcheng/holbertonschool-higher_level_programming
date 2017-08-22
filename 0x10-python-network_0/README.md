## 0x10 Python - Network #0

![NETWORKING](https://i.pinimg.com/736x/43/6f/0a/436f0af56128621c9baf7739134db1db--python-script-send-message.jpg)

#### AUTHOR
Spencer Cheng: [github account](https://github.com/spencerhcheng), [twitter](https://twitter.com/spencerhcheng)

#### ENVIRONMENT
All files are written and compiles on `Ubuntu 14.04 LTS`. The first line of bash scripts will be exactly `#!/usr/bin/env bash`. Python scripts are verified with PEP8 style guidelines.

### OBJECTIVES
Learning points:
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level) 

#### 0. cURL body size
Takes in a URL, sends a request to that URL and displays the size of the body of the response. Size is displayed in bytes.

Example:

```
spencer@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
spencer@ubuntu:~/0x10$ 
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 0-body_size.sh

#### 1. cURL to the end
Takes in a URL, sends a GET request to the URL, and displays the body of the response. Displays only body of a `200` status code response.

Example:
```
spencer@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
spencer@ubuntu:~/0x10$ 
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 1-body.sh

#### 2. cURL Method
Sends a `DELETE` request to the URL passed as the first argument and displays the body of the response.

Example:
```
spencer@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
spencer@ubuntu:~/0x10$ 
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 2-delete.sh

#### 3. cURL only methods
Takes in a URL and displays all HTTP methods the server will accept.

Example:
```
spencer@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
spencer@ubuntu:~/0x10$ 
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 3-methods.sh

#### 4. cURL headers
Takes in a URl as an argument, sends a `GET` request to the URL, and displays the body of the response. The header variable `X-HolbertonSchool-User-Id` is sent with the value `98`.

Example:
```
spencer@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
spencer@ubuntu:~/0x10$
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 4-header.sh

#### 5. cURL POST parameters
Takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response. The variable `email` is sent with the value `hr@holbertonschool.com`.

The variable `subject` is sent with the value `I will always be here for PLD`.

Example:
```
spencer@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
spencer@ubuntu:~/0x10$ 
```

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x10-python-network_0
File: 5-post_params.sh
