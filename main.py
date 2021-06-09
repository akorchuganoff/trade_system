from data import db_session
from data.offer import Offer
from data.user import User
from forms.registration import RegisterForm, LoginForm
from flask import Flask, render_template, redirect, request, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'DK_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
def system():
    return render_template("system.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/registration")
def registration():
    form = RegisterForm()
    return render_template("registration.html", form=form)


def main():
    db_session.global_init("db/trade_system.db")
    app.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == '__main__':
    main()