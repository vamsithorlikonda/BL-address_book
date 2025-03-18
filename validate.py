import re
from functools import wraps

def validate_input(input_type):
    """
    Decorator to validate user input based on input_type dynamically.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(prompt, input_type):
            patterns = {
                "name": r"^[A-Za-z]{2,}$",
                "address": r"^[A-Za-z0-9\s,.-]{5,}$",
                "city_state": r"^[A-Za-z\s]{2,}$",
                "zip": r"^\d{5,6}$",
                "phone": r"^\d{10}$",
                "email": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            }

            error_messages = {
                "name": "Invalid name! Only alphabets, min 2 characters.",
                "address": "Invalid address! Must be at least 5 characters long.",
                "city_state": "Invalid city/state! Only alphabets, min 2 characters.",
                "zip": "Invalid zip code! Must be 5 or 6-digit number.",
                "phone": "Invalid phone number! Must be exactly 10 digits.",
                "email": "Invalid email! Please enter a valid email address."
            }

            while True:
                user_input = func(prompt)
                if re.match(patterns.get(input_type, ""), user_input):
                    return user_input
                print(error_messages.get(input_type, "Invalid input!"))
        return wrapper
    return decorator

@validate_input("Default")
def get_valid_input(prompt):
    return input(prompt)