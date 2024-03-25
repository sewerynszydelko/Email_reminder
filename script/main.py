""" Main file """
from os import environ, getenv
from dotenv import load_dotenv
import data_base as my_db


class User:
    """ User class """

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"User:{self.name}"

    @staticmethod
    def get_input_choice_type(message: str, chosen_type=str):
        """Get input from user in specific type (int or str) with your message
        Args:
            message (str): Your message to user
            chosen_type (_type_, optional): You can chose to waht type o convert input. Defaults to str.
        Returns:
            str or int: returns user input in specific type
        """
        user_input = input(message)
        try:
            if chosen_type is int:
                return int(user_input)

            if chosen_type is str:
                return user_input
            else:
                return user_input

        except ValueError as error:
            print("You chose wrong type: ", error)
            return False


def show_all_boks():
    with my_db.BaseConnectManager("base.db") as curosr:
        data = my_db.get_title_authors(curosr)

    for book in data:
        print(book)


if __name__ == "__main__":
    show_all_boks()
