from flask import Flask
from datasource.db_session import engine
from entities.model import Base
from controllers.routes import Client_bp

app= Flask(__name__)

#create tables
Base.metadata.create_all(engine)

#registry routes
app.register_blueprint(Client_bp)

if __name__=="__main__":
    app.run(debug=False, port=8082)

