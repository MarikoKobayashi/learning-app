from flask import Flask
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

def create():
    with app.app_context():
        user = User(
            username='nakata', 
            password_hash=generate_password_hash('penguin'), 
        )

        db.session.add(user)
        db.session.commit()

def read():
    with app.app_context():
        user = User.query.filter_by(id=3).first()
        if user:
            print(f'ID: {user.id}, Username: {user.username}')
            
def update():
    with app.app_context():
        user = User.query.filter_by(id=3).first()
        if user:
            user.username = 'yusuke'
            db.session.commit()

def delete():
    with app.app_context():
        user = User.query.filter_by(username='yusuke').first()
        if user:
            db.session.delete(user)
            db.session.commit()

def read_all():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f'ID: {user.id}, Username: {user.username}')

if __name__ == '__main__':
    create()
    read() 
    update()
    read()
    delete()
    read_all()