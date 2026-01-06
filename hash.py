import hashlib

def sha256gen(plain_text):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(plain_text.encode('utf-8'))
    return sha256_hash.hexdigest()
