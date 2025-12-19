import bcrypt

def hash_password(password):

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


def verify_password(password,hashed_password):

    if bcrypt.checkpw(password, hashed_password):
        return True
    else:
        return False


print(verify_password(b"@Brayotan2076",b"$2b$12$yTI6zNlloYWXrfHQ8D5P6eaYnMxkk.kSxLM0kkKigGktonMHaxVwy"))