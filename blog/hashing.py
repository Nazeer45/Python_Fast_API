from passlib.hash import bcrypt_sha256

class Hash():
    def bcrypt(password: str):
        return bcrypt_sha256.hash(password)
    
    def verify(hashed_password, plain_password):
        return bcrypt_sha256.verify(plain_password, hashed_password)