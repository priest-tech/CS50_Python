from numb3rs import validate

def test_valid_ip():
    assert validate('192.168.0.1') is True
    assert validate('255.255.255.255') is True
    assert validate('0.0.0.0') is True

def test_invalid_ip():
    assert validate('256.168.0.1') is False
    assert validate('192.168.0.300') is False
    assert validate('999.999.999.999') is False
    assert validate('192.168.0') is False
    assert validate('192.168.0.') is False
    assert validate('.192.168.0') is False
    assert validate('text') is False
    assert validate('192.168.0.-1') is False
