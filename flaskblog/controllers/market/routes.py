from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models.spx import Spx

market = Blueprint('market', __name__)

@market.route("/market")
@login_required
def spx():
    spx = Spx.query.all()
    return render_template('market/spx.html', spx=spx)
