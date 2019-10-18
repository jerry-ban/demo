# run an app server
import connexion
import os
import logging
from logging.handlers import RotatingFileHandler
import shutil

log_file_name = "/var/log/demo_rest.log"


# uid = pwd.getpwnam("nobody").pw_uid
# gid = grp.getgrnam("nogroup").gr_gid
# os.chown(log_file_name, uid, gid)


### logging.basicConfig(level=logging.INFO,filename = log_file_name)
logging.basicConfig(level=logging.INFO)
#shutil.chown(log_file_name, user="ubuntu")
#logging.basicConfig(level=logging.INFO, filename="demo_rest.log")
#new_log_handler = RotatingFileHandler(log_file_name, maxBytes=5*1024*1024, backupCount=5)
### new_log_handler = RotatingFileHandler(log_file_name, maxBytes=5*1024, backupCount=5)

#logging.getLogger().addHandler(new_log_handler )

port_number = int(os.getenv("PORT_NUMBER", 8831))
deployment_env = os.getenv("DEPLOY_ENV", "development")
www_server = "flask" if deployment_env=="development" else "tornado"

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('my_api.yaml', arguments={'title': 'Optimizion Demo Service'})

application = app.app  # used for the wsgi
### application.logger.addHandler(new_log_handler )

if __name__ == '__main__':
    #application.logger.handlers=[]
    #logging.basicConfig(filename=log_file_name)
    app.run(port=port_number, debug=True)
    #app.run(threaded=False, processes = 3, port=port_number, debug=True)
