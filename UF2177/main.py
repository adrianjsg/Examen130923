from flask import Flask
from controller import Routes
from repository import Repository
from connector import ConnectorDatabase

if __name__ == '__main__':
    app = Flask(__name__)

    # Configura la conexión a la base de datos
    db_connector = ConnectorDatabase(
        host="localhost",
        user="root",
        password="root",
        database="Estudiantes",
        port=3306
    )

    repository = Repository(db_connector)

    routes = Routes(app, repository)

    app.run(debug=True)





