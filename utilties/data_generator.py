import random
import string


def generate_random_str(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class AccountCreation:
    rand_suffix = generate_random_str()
    first_name = f"{rand_suffix}_firstname"
    last_name = f"{rand_suffix}_lastname"
    country_name = 'India'
    email = f"{rand_suffix}@gmail.com"
    password = "sql1244@S"

    def account_creation_data(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "country": self.country_name,
            "email": self.email,
            "password": self.password

        }
