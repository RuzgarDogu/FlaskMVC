"""
    API controller içinde değil de, ayrı bir klasörde tanımlanmalı
    Bunun için de ana dizindeki __init__ kısmında düzenleme yapılmalı
    Aynı controller için yapılanlar, api klasörü için de yapılmalı
"""

from flask import request, jsonify, Blueprint, current_app
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models.post import Post
from flaskblog.api.apifunctions import create_ap_token, verify_api_token

posts = Blueprint('_posts', __name__)

# Bu api için jwt veya bu örnekteki password reset kısmındaki token ile yapmak gerekecek
@posts.route("/api/<token>/post/<int:post_id>")
def _post(post_id,token):
    post = Post.query.get(post_id)
    if post and verify_api_token(token):
        api_post = {
            'id': post.id,
            'title' : post.title,
            'date_posted' : post.date_posted,
            'content' : post.content,
            'user_id' : post.user_id,
            'result': 'success',
            'payload': verify_api_token(token)
        }
        return jsonify(api_post)
    elif post and not verify_api_token(token):
        return jsonify({
            'result': 'warning',
            'message': 'Token is either wrong or has expired',
            # 'token': create_ap_token({'appid':1,'appname':'test'})
        })
    elif not post and verify_api_token(token):
        return jsonify({
            'result': 'warning',
            'message': 'Post is not found'
        })
    else:
        return jsonify({
            'result': 'warning',
            'message': 'Something is wrong with your credentials. Please check again.',
            # Bu aşağıdaki silinecek, test amaçlıdır.
            'token': create_ap_token({'appid':1,'appname':'test'})
        })
