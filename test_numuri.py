from numuri import Luhn_checks_my_card, check_card_type

def test_checks_my_card():
    assert Luhn_checks_my_card("4003600000000014") == True
    assert Luhn_checks_my_card("6176292929") == False
    assert Luhn_checks_my_card("371449635398431") == True
    assert Luhn_checks_my_card("5555555555554444") == True
    assert Luhn_checks_my_card("4111111111111111") == True
def test_checks_card_type():
    assert check_card_type("4003600000000014") == "VISA"
    assert check_card_type("6176292929") == "INVALID"
    assert check_card_type("371449635398431") == "AMEX"
    assert check_card_type("5555555555554444") == "MasterCard"
    assert check_card_type("4111111111111111") == "VISA"
