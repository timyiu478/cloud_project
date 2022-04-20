# Set Up Guide

 1.  Run ec2 instance
 
 1.  Create an empty directory and go to the directory 
 ```
 $ mkdir comp4442_project
 $ cd comp4442_project
 ```
 
 1.  Install the virtual environment
 ```
 $ pip3 install virtualenv
 ```
 
 1. Create a virtual environment
 ```
 $ virtualenv venv
 ```
 
 1. Activate the virtual environment
 ```
 source lab6/bin/activate
 ```
 
 1. Install python libraries
 ```
 $ pip3 install -r requirement.txt
 ```
 
 1. Run application.py, redis-server, and rq worker
 ```
 $ python3 application.py
 $ redis-server
 $ rq worker
 ```
 1. write driving data 
	1. modify the URL in the writeData.py
	1. run writeData.py
```
python3 writeData.py
```