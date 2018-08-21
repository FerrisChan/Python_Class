from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


@main.route("/admin")
def index():
    u = current_user()
    if u.is_admin():
        bs = Board.all()
        return render_template('board/admin_index.html', bs = bs)
    else:
        return redirect(url_for("topic.index"))


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    if u.is_admin():
        m = Board.new(form)
        return redirect(url_for('board.index'))
    else:
        return redirect(url_for("topic.index"))


@main.route("/delete")
def delete():
    u = current_user()
    if u.is_admin():
        print("debug", u, u.is_admin() )
        id = int(request.args.get('id'))
        Board.delete(id)
        return redirect(url_for(".index"))
    else:
        return redirect(url_for("topic.index"))