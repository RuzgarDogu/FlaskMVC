from flask import request, jsonify, Blueprint, current_app
from itsdangerous import JSONWebSignatureSerializer as Serializer

def create_ap_token(payload):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps(payload).decode('utf-8')

def verify_api_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        payload = s.loads(token)
    except:
        return None
    return payload
