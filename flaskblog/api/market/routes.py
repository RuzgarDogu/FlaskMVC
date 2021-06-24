"""
    API controller içinde değil de, ayrı bir klasörde tanımlanmalı
    Bunun için de ana dizindeki __init__ kısmında düzenleme yapılmalı
    Aynı controller için yapılanlar, api klasörü için de yapılmalı
"""

from flask import request, jsonify, Blueprint, current_app
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models.spx import Spx
from flaskblog.api.apifunctions import create_ap_token, verify_api_token

market = Blueprint('_market', __name__)

# Bu api için jwt veya bu örnekteki password reset kısmındaki token ile yapmak gerekecek
@market.route("/api/<token>/market")
def _market(token):
    spx = Spx.query.limit(5).all()
    result = []
    for s in spx:
        result.append(s.to_json())
    if result and verify_api_token(token):
        api_post = {
            'result': 'success',
            'payload': verify_api_token(token),
            'data': result
        }
        return jsonify(api_post)
    elif spx and not verify_api_token(token):
        return jsonify({
            'result': 'warning',
            'message': 'Token is either wrong or has expired',
            # 'token': create_ap_token({'appid':1,'appname':'test'})
        })
    elif not spx and verify_api_token(token):
        return jsonify({
            'result': 'warning',
            'message': 'Data is not found'
        })
    else:
        return jsonify({
            'result': 'warning',
            'message': 'Something is wrong with your credentials. Please check again.',
            # Bu aşağıdaki silinecek, test amaçlıdır.
            'token': create_ap_token({'appid':1,'appname':'test'})
        })
