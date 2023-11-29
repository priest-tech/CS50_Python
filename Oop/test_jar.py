import pytest
from jar import Jar

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-5)

    with pytest.raises(ValueError):
        Jar("invalid_capacity")

def test_deposit_and_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(-3)

    with pytest.raises(ValueError):
        jar.deposit(10)

    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(5)

    with pytest.raises(ValueError):
        jar.withdraw(-2)

def test_str_representation():
    jar = Jar(7)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_capacity_property():
    jar = Jar(15)
    assert jar.capacity == 15

    jar = Jar()
    assert jar.capacity == 12
