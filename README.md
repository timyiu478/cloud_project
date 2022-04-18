# Set Up Guide

 1.  Run ec2 instance
 
 2.  Create an empty directory and go to the directory 
 ```
 $ mkdir comp4442_project
 $ cd comp4442_project
 ```
 
 3.  Install the virtual environment
 ```
 $ pip3 install virtualenv
 ```
 
 4. Create a virtual environment
 ```
 $ virtualenv venv
 ```
 
 5. Activate the virtual environment
 ```
 $ source lab6/bin/activate
 ```
 
 6. Install python libraries
 ```
 $ pip3 install -r requirement.txt
 ```
 
 7. Run application.py, redis-server, and rq worker
 ```
 $ python3 application.py
 $ redis-server
 $ rq worker
 ```
 8. write driving data 
	1. modify the URL in the writeData.py
	1. run writeData.py
```
$ python3 writeData.py
```