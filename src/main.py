"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Social, Post, Multimedia



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users/<int:id>', methods=['PUT','PATCH'])
def update_user(id):
    body=request.get_json()
    user = User.get_user(id)
    if not user:
        raise APIException('User not found', status_code=404)
    return user

@app.route('/users/<int:id_user>/socials/<int:id_social>', methods=['PUT','PATCH'])
def update_social(id_user,id_social):
    body=request.get_json()
    social = Social.get_social(id_user,id_social)
    if not social:
        raise APIException('Social media account not found', status_code=404)
    return jsonify(social)

@app.route('/users/<int:id_user>/socials/<int:id_social>/posts/<int:id_post>', methods=['PUT','PATCH'])
def update_post(id_user,id_social,id_post):
    body=request.get_json()
    post = Post.get_post(id_user,id_social,id_post)
    if not post:
        raise APIException('Post not found', status_code=404)
    else:
        return jsonify(post)
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
