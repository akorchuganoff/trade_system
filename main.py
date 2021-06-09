from data import db_session
from data.offer import Offer
from data.user import User
from forms.add_offer_form import AddOfferForm
from forms.registration import RegisterForm, LoginForm
from flask import Flask, render_template, redirect, request, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)

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


@app.route("/system")
@app.route("/", methods=['GET', 'POST'])
def system():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        offers = db_sess.query(Offer).all()[:5]
        print(offers[0].name)
        return render_template("system.html", n=max(0, len(offers)), offers=offers)
    elif request.method == 'POST':
        pass


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("registration.html", form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("registration.html", form=form,
                                   message="Почта уже зарегистрирована в системе")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            nation=form.nation.data,
            money=10000
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template("registration.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильно указана почта или пароль",
                               form=form)
    return render_template("login.html", form=form)


@app.route('/add_offer', methods=['GET', 'POST'])
def add_offer():
    print(request.method)
    form = AddOfferForm()
    if form.validate_on_submit():
        print(1243142)
        return redirect('/account')

    return render_template("add_offer.html", form=form)

def main():
    # db_sess = db_session.create_session()
    # db_sess.commit()
    db_session.global_init("db/trade_system.db")
    app.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == '__main__':
    main()
