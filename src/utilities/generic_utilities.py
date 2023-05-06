import random
import string
import logging as logger


def generate_random_email_and_password(domain: str = "example.com", email_prefix: str = "john.doe"):
    logger.debug("Generating random email and password...")
    random_string = "".join(random.choices(string.ascii_lowercase, k=10))
    email = email_prefix + "_" + random_string + "@" + domain

    password = "".join(random.choices(string.ascii_lowercase, k=20))

    random_info = {"email": email, "password": password}
    logger.debug(f"Generated random info {random_info}")
    return random_info
