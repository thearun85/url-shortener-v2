import random
import string

ALPHABETS = string.ascii_letters + string.digits
CODE_LENGTH = 6

def generate_shortcode() -> str:
    return "".join(random.choices(ALPHABETS, k=CODE_LENGTH))
