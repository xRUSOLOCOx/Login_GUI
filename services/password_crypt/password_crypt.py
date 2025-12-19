import bcrypt

def hash_password(password):

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


def verify_password(password,hashed_password):

    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False


