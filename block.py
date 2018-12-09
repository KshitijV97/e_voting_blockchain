import json, hashlib



def hash_me(k):
    if type(k) is not str:
        k = json.dumps(k, sort_keys=True)
        k = k.encode()
    return hashlib.sha256(k).hexdigest()