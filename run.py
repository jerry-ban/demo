# run an app server
import connexion
import os
import logging

logging.basicConfig(level=logging.INFO)

port_number = int(os.getenv("PORT_NUMBER", 8831))
deployment_env = os.getenv("DEPLOY_ENV", "development")
www_server = "flask" if deployment_env=="development" else "tornado"

app = connexion.FlaskApp(__name__, port = port_number, specification_dir='openapi/')
app.add_api('my_api.yaml', arguments={'title': 'Optimizion Demo Service'})

application = app.app  # used for the wsgi

if __name__ == '__main__':
    app.run(server= www_server, debug=True)
#app.run(port=port_number, server= www_server, debug=True)
#app.run(threaded=False, processes = 3, port=port_number, debug=True)
