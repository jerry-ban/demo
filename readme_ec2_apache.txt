Prerequisites to Deploy a New Flask app on AWS Elastic Beanstalk
https://medium.com/elucidata/deploying-a-flask-application-to-aws-elastic-beanstalk-61e425d8881e

1. Your code files should contain a file application.py which will serve as the entry point of the whole application and is needed by Beanstalk to run the App.
2. The application object that Flask uses should be named application and not app.
3. All the python dependencies should be placed in a file requirements.txt placed in the root folder of your code repository.
4. You can include a .ebextensions folder in the root folder of your code repository and let it remain empty for the time being.

