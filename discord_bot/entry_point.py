from argparse import ArgumentParser
from .register import register_new_account


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('-u', help='New account username', type=str, required=True, dest='username')
    parser.add_argument('-e', help='New account email', type=str, required=True, dest='email')

    try:
        print(
            register_new_account(**vars(parser.parse_args()))
        )
    except KeyError as e:
        print(e)
