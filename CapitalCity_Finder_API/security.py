from models.user import User


def authenticate(username, password):
    user = User.get_by_username(username)
    if user and user.password==password:
        return user                     # JWT returns token for the user


def identity(payload):
    user_id = payload['identity']
    return User.get_by_id(user_id)  # every time for new request, JWT checks if the id in the token matches

