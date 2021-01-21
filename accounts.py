from app import db, User
from werkzeug.security import generate_password_hash

def add_account():
    print('Enter username: ')
    name_input = input()
    print('Enter password')
    pass_input = input()
    hashed_password = generate_password_hash(pass_input, method = 'sha256')
    new_user = User(username = name_input, password = hashed_password)
    db.session.add(new_user)
    db.session.commit()
    print('User Created')


add_account()