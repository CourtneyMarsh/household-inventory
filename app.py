from flask import Flask
from controllers.category_controller import category_blueprint
from controllers.location_controller import location_blueprint

app = Flask(__name__)
app.register_blueprint(location_blueprint, url_prefix='/location')
app.register_blueprint(category_blueprint, url_prefix='/category')

if __name__ == '__main__':
    app.run(debug=True)