from unittest.mock import patch
from email_send import send_mail


@patch('smtplib.SMTP_SSL')
def test_send_mail(mock_smtp):
    send_mail()
    mock_smtp.assert_called()
    context = mock_smtp.return_value.__enter__.return_value
    context.login.assert_called()
    context.sendmail.assert_called_with('Your email @gamil.com',
                                        'Your email @gamil.com',
                                        'user is cool')
