import pytest
from fitness import validate_user_data

def test_valid_user_data():
    assert validate_user_data({"age": 25, "weight": 70, "activity_level": "moderate", "goal": "weight_loss"})

def test_invalid_age():
    assert not validate_user_data({"age": -5, "weight": 70, "activity_level": "moderate", "goal": "weight_loss"})

def test_missing_activity_level():
    assert not validate_user_data({"age": 25, "weight": 70, "goal": "weight_loss"})
