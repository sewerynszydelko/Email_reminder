from main import User


def test_user_get_input_choice_type_positive():
    # Given
    test_user = User("Bob")
    message = "Test message: "
    # When
    result = test_user.get_input_choice_type(message=message, chosen_type=str)
    # Then
    assert result == "text"


def test_user_get_input_choice_type_negative():
    # Given
    test_user = User("Bob")
    message = "Test message negative: "
    # When
    result = test_user.get_input_choice_type(message=message, chosen_type=str)
    # Then
    assert not result == "text"
