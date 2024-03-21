from os import environ, getenv
from dotenv import load_dotenv


class User:

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


if __name__ == "__main__":
    test = User('bob')
    result = test.get_input_choice_type(
        "Pleas enter how many years do you have: ")
    print(type(result), result, sep="\n")
