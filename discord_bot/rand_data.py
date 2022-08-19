from random import randint, choice
from string import ascii_letters


class BIRTH_DATE:

    def __new__(cls, *args, **kwargs):
        return f"{randint(1990, 2005)}" \
               f"-{'{:02}'.format(randint(1, 12))}" \
               f"-{'{:02}'.format(randint(1, 27))}"


class PASSWORD:

    def __new__(cls, password_len=10, *args, **kwargs):
        return "".join([
            choice(ascii_letters) for _ in range(password_len)
        ])
