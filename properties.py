import random
import string

customer = {
    "first_name": "Kartik",
    "last_name": "Gouti",
    "email": ''.join(random.choice(string.ascii_letters) for i in range(10)) + "@gmail.com",
    "password": "A2bc.223@gmail.com"
}

