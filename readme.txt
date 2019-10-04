### default is served by Flask’s built in web server, good for development and debugging needs
### and not recommended in production environment. Let’s install uWSGI and configure Nginx to do the heavy lifting.
### to use nginx as server,

sudo apt-get install build-essential python python-dev
$ pip install uwsgi

$ sudo apt-get install nginx
$ sudo /etc/init.d/nginx start


### follow aws tutorial, create a new box with ubuntu linux,
### in aws ubuntu box: assume python3 installed already
$ sudo apt-get update
$ sudo apt-get install -y python3-pip
# above -y means automatic yes to promots
### to get the original rep url:
$ git config --get remote.origin.url
### in project,to create requirements.txt, to do this:
$ git clone https://github.com/xxx/demo.git demo
$ cd demo
$ pip3 free > requirements.txt
### then to install all dependencies,
$ pip3 install -r requirements.txt
### for connexion, if swagger-ui needed(usually), need to do this:
$ pip3 uninstall connexion
$ pip3 install connexion[swagger-ui]

### to run app in a seperate window, do this:
# install screen:
$ sudo apt-get install screen
# Screen usage:
$ screen -list
# enter a screen named myapp
$ screen -r myapp
# to exit the current screen
$ Ctrl A + Ctrl D
# to create a new screen named "myapp"
$ screen -S myapp
# to kill a screen named "myapp"
$ screen -S myapp -X kill


### to enable the port used in flask, for example 8831, in aws:
### open the security group which assigned to the aws instance, add the inbound rule with port 8831 and save

to set python3.6 as default if both 3.4 and 3.6 installed, to do the following:
$ sudo update-alternatives --config python
### Will show you an error:
$ update-alternatives: error: no alternatives for python3
### You need to update your update-alternatives , then you will be able to set your default python version.
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
### Then run :
$ sudo update-alternatives --config python
### Set python3.6 as default.
### Or use the following command to set python3.6 as default:
$ sudo update-alternatives  --set python /usr/bin/python3.6




##01. upgrade python2 to python3 in to aws linux box
#connect to box, do yum update
$ sudo yum update
#check python
$ python --version
#if version 3 not installed, do it
$ sudo yum install python3 -y
$ sudo apt install python3
#use the which command to confirm that the install was successful.
$ which python3
#in order to use the github to deploy, need to install the git tools
$ sudo yum install git

##install virtualenv and create the python3 environment
#Install virtualenv for the current user using pip3.
$ pip3 install --user virtualenv
# Create a directory to hold your virtualenv environments
$ pwd
$ mkdir venv
$ cd venv
$ pwd
# Use the virtualenv command to create the python3 environment.
$ virtualenv -p /usr/bin/python3 python3
##Activate the environment and install Boto 3
$ source /home/ec2-user/venv/python3/bin/activate
#Use the which command to verify that you are now referencing the new environment.
$ which python
# Use the pip3 command to install Boto 3 from within the python3 environment.
$ pip3 install

# now type python and canimport boto3, finally, to deactivate the python3 environment
$  deactivate

 #Run the which command to confirm that you are using the default environment.
$ which python
/usr/bin/python

###02. To activate the python3 environment automatically when you log in, add it to your .bashrc file.
$ echo "source /home/ec2-user/venv/python3/bin/activate" >> /home/ec2-user/.bashrc


# after activate the desired python environment
#install numpy
$ pip install numpy

#install nlopt
$ pip install nlopt

# then we can open the test_run.py and test the example

###03. to run restful service example, need to install connexion
$ pip3 install connexion[swagger-ui]

###ohter dependencies
$ pip install python-dateutil