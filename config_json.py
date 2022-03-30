import json

with open('credenciais.json') as arquivo_json:
    config = json.load(arquivo_json)


with open('payment.json') as payment_json:
    payment = json.load(payment_json)


USER = config.get("USER")
PASSWORD = config.get("PASSWORD")
DATABASE = config.get("DATABASE")
JWT_SECRET_KEY = config.get("JWT_SECRET_KEY")
PORT = config.get("PORT")
HOST = config.get("HOST")
DATABASE_URL = config.get("DATABASE_URL")


def read_json_env():
    return f'User:{USER} Password: {PASSWORD} Database: {DATABASE} JWT Secret Key: {JWT_SECRET_KEY} Port: {PORT} Host: {HOST}'


def read_payment_json():
    PAYMENT = payment.get("payment")
    VALUE = PAYMENT.get("value")
    PAYMENT_DATE = PAYMENT.get("payment_data")
    PAYLOAD = PAYMENT.get("payload")
    TRACK_ONE = PAYLOAD.get("track_one")
    TRACK_TWO = PAYLOAD.get("track_two")
    return f'Value:{VALUE} PaymentDate:{PAYMENT_DATE} TrackOne:{TRACK_ONE} TrackTwo: {TRACK_TWO}'
