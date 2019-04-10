import string
import random
import time


def generate_slug():
    random.seed(time.time())
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(7))
