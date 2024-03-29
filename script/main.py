""" Main file """
from os import environ, getenv
from dotenv import load_dotenv
import data_base as my_db
import email_send as es
import smtplib


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
    """ Shows all titles with thier autros from data base """
    with my_db.BaseConnectManager("base.db") as curosr:
        data = my_db.get_title_authors(curosr)

    for book in data:
        print(book)


def create_message_to_remaind(data, name):
    """ Create message that reminds about book to return """
    final_message = f"Hello {name}\nIm writing to you to remind about book that you borowed:\n{
        data[0]["title"]}-{data[0]["author"]}\nPleas return to libry by end of month\nBest Regards!"

    return final_message


def mian_run():
    print("Hello welcom in menu of book base choce what you  want below\n")
    while True:
        user_input = User.get_input_choice_type(
            "What you want to do ?: \n1: See all books in base\n2:choice book\n3:Give new book to data base\n4:Exit of program\n5:send remaind message to people\n")

        match user_input:
            case "4":
                break
            case "1":
                show_all_boks()
                input("type anything to continoue ")
            case "2":
                show_all_boks()
                choice_book = User.get_input_choice_type(
                    "Pleas write choicen book title by row number from 0 to 7:").split(" ")
                
                with my_db.BaseConnectManager("base.db") as cursor:
                    title_author = my_db.get_title_authors(cursor)
                    print(title_author[int(choice_book)][title])

            case "3":
                email_adres, title, author, created_at = User.get_input_choice_type(
                    "Pleas enter: email, title, autohr,data\n:").split(",")
                my_db.add_new_book(email_adres, title,
                                   author, created_at, "base.db")
                show_all_boks()
            case "5":
                name = input("Pleas give me name to remaind: ")
                cursor = my_db.create_connection()
                data = my_db.get_title_authors(cursor)
                message = create_message_to_remaind(data=data, name=name)

                try:
                    es.send_mail(message)
                except smtplib.SMTPAuthenticationError as error:
                    print("Error:", error)


if __name__ == "__main__":
    print(create_message_to_remaind(
        [{"title": "ambroży", "author": "Henryk"}], "Bob"))
