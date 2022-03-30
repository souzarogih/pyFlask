from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout, UserConfirm
from resources.site import Sites, Site
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from config_json import read_json_env, read_payment_json, DATABASE_URL
from sql_alchemy import banco

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' # comentado para subir aplicação no herok
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
banco.init_app(app) # criado para subir aplicação no heroku
api = Api(app)
jwt = JWTManager(app)

# Leitura de arquivo json
# receive = config_json.read_json_env()
# print(receive)

# receive_payment = read_payment_json()
# print('receive_payment:', receive_payment)


@app.route('/')
def index():
    return '<h1>Deploy para Heroku realizado com sucesso!</h1>'

@app.before_first_request
def cria_banco():
    banco.create_all()


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'You have been logged out.'}), 401


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(Sites, '/sites')
api.add_resource(Site, '/sites/<string:url>')
api.add_resource(UserConfirm, '/confirmacao/<int:user_id>')

# comentado para subir aplicação no herok
# if __name__ == '__main__':
#     from sql_alchemy import banco
#     banco.init_app(app)
#     app.run(debug=True)