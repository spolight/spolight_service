from flask import Flask, redirect, url_for, render_template, request, make_response
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from oauth import OAuthSignIn
from flask.ext.sqlalchemy import SQLAlchemy
from flask import g
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from identitytoolkit import gitkitclient

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
lm = LoginManager(app)
lm.login_view = 'index'
'''
engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db.session.query_property()
'''

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(64), nullable=True, autoincrement=True)
    email = db.Column(db.String(64), nullable=True, autoincrement=True)

    def __init__(self, nickname=None, email=None):
        self.nickname = nickname
        self.email = email
'''
def init_db():
    import app.models
    Base.metadata.create_all(bind=engine)


def connect_db():
    return sqlite.connect(app.config['DATABASE'])
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
'''

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
'''
    # Check for and read the Google Identity Toolkit token if present
    if 'gtoken' in request.cookies:
    gitkit_user = gitkit_instance.VerifyGitkitToken(request.cookies['gtoken'])
    if gitkit_user:
      text = "Welcome " + gitkit_user.email + "! Your user info is: " + str(vars(gitkit_user))

    response = make_response(render_template('login.html', CONTENT=text))
    response.headers['Content-Type'] = 'text/html'
    return response
'''

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    username, email = oauth.callback()
    if email is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user=User.query.filter_by(email=email).first()
    if not user:
        nickname = username
        if nickname is None or nickname == "":
            nickname = email.split('@')[0]

        user=User(nickname=nickname, email=email)
        db.session.add(user)
        db.session.commit()

    login_user(user, remember=True)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
