# run an app server
import connexion
import os

port_number = int(os.getenv("PORT_NUMBER", 8831))
deployment_env = os.getenv("DEPLOY_ENV", "development")
www_server = "flask" if deployment_env=="development" else "tornado"

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('my_api.yaml', arguments={'title': 'Optimizion Demo Service'})
app.run(port=port_number, server= www_server, debug=True)
#app.run(threaded=False, processes = 3, port=port_number, debug=True)
