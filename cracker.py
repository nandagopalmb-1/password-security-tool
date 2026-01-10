from utils import hash_password

def dictionary_attack(target_hash, wordlist_path):
    with open(wordlist_path, "r", errors="ignore") as file:
        for word in file:
            word = word.strip()
            if hash_password(word) == target_hash:
                return word
    return None
