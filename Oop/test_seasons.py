from datetime import date
from seasons import get_age_in_minutes
from num2words import num2words


def test_get_age_in_minutes():
    # Test case 1: Check if the function returns the correct age in minutes
    dob = "2000-01-01"
    expected_age_in_minutes = 12565440  # Assuming the test is run on 2023-11-22
    assert get_age_in_minutes(dob) == num2words(expected_age_in_minutes).replace(" and", "")

    # Test case 2: Check if the function handles current date properly
def test_get_age_in_minutes_today():   
    dob = "1990-12-31"
    today = date.today()
    expected_age_in_minutes = (today - date(1990, 12, 31)).days * 24 * 60
    assert get_age_in_minutes(dob) == num2words(expected_age_in_minutes).replace(" and", "")
