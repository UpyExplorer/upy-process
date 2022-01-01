from flask import Flask, render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

db.init_app(app)
