import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def estimate_crack_time(length, charset_size, guesses_per_sec=1_000_000):
    combinations = charset_size ** length
    seconds = combinations / guesses_per_sec
    return seconds
