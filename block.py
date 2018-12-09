import json, hashlib



def hash_me(k):
    if type(k) is not str:
        k = json.dumps(k, sort_keys=True)
        k = k.encode()
    return hashlib.sha256(k).hexdigest()

def update_state(transaction, state):
    state = state.copy()

    for key in transaction:
        state[key] += transaction[key]

    return state

def check_transaction(transaction, state):
    if sum(transaction.values()) is not 0:
        return False

    for key in transaction.keys():
        if key in state.keys():
            account_balance = state[key]
        else:
            account_balance = 0

        if account_balance + transaction[key] < 0:
            return False

    return True

def make_block(transactions, chain):
    parent_hash = chain[-1]['hash']
    block_number = chain[-1]['contents']['block_number'] + 1

    block_contents = {
        'block_number': block_number,
        'parent_hash': parent_hash,
        'transaction_count': block_number + 1,
        'transaction': transactions
    }

    return {'hash': hash_me(block_contents), 'contents': block_contents}

def check_block_hash(block):
    expected_hash = hash_me(block['contents'])

    if block['hash'] is not expected_hash:
        raise

    return

