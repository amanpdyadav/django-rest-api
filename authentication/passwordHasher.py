import bcrypt
from django.contrib.auth.hashers import make_password, check_password


def hashpassword(password):
    return make_password(
        password=password.encode('utf-8'),
        salt=None,
        hasher='unsalted_md5')


def passwordCorrect(password, hashed):
    return check_password(password.encode('utf-8'), hashed)