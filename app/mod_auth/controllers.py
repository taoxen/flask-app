# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from flask_login import LoginManager, UserMixin, login_user,\
		  login_required, logout_user, current_user

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db, login_manager

# Import module forms
from app.mod_auth.forms import LoginForm, RegisterForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Set the route and accepted methods
@mod_auth.route('/')
def index():
    return render_template('auth/index.html');

@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                return redirect(url_for('auth.dashboard'))
	flash('Invalid username or password', 'error')
        #return '<h3>Invalid username or password<h3>'

    return render_template('auth/login.html', form=form)

@mod_auth.route('/dashboard/')
@login_required
def dashboard():
    return render_template('auth/dashboard.html', name=current_user.name)

@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        flash('all is well')
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(name=form.username.data, password=hashed_password, email=form.email.data)
        new_user.role = 1
        new_user.status = 1
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)


@mod_auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))

