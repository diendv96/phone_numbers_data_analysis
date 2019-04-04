import models.App as App


def get_actual_activation_date(phone_number):
    if not isinstance(phone_number, str):
        raise TypeError('Please provide a string argument')
    data = App.App.read_csv("data/PhoneNumberResult.csv", index_col=0, squeeze=True).to_dict()
    phone_number = int(phone_number.lstrip("0"))
    if phone_number in data:
        return data[phone_number]
    else:
        return None


def test_activation_date_multiple_owner():
    assert get_actual_activation_date('0987000001') == '2016-06-01'


def test_activation_date_one_owner():
    assert get_actual_activation_date('0987000002') == '2016-02-01'


def test_activation_date_phone_number_deactivated():
    assert get_actual_activation_date('0987000003') == '2016-01-01'

