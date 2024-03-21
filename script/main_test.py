from main import User


def test_user_get_input_choice_type_positive():
    # Given
    message = "Test message: "
    # When
    result = User.get_input_choice_type(message=message, chosen_type=str)
    # Then
    assert result == "text"


def test_user_get_input_choice_type_negative():
    # Given
    message = "Test message negative: "
    # When
    result = User.get_input_choice_type(message=message, chosen_type=str)
    # Then
    assert not result == "text"
