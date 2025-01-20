import pytest
from fitness import validate_user_data
from fitness import generate_fitness_program
from fitness import suggest_improvements

def test_valid_user_data():
    assert validate_user_data({"age": 25, "weight": 70, "activity_level": "moderate", "goal": "weight_loss"})

def test_invalid_age():
    assert not validate_user_data({"age": -5, "weight": 70, "activity_level": "moderate", "goal": "weight_loss"})

def test_missing_activity_level():
    assert not validate_user_data({"age": 25, "weight": 70, "goal": "weight_loss"})

# Tests pour la génération de programme de fitness
def test_generate_fitness_program_weight_loss():
    user_data = {"age": 30, "weight": 80, "activity_level": "moderate", "goal": "weight_loss"}
    expected_program = ["Cardio: 30 minutes, 5x per week", "Strength: 2x per week"]
    assert generate_fitness_program(user_data) == expected_program

def test_generate_fitness_program_muscle_gain():
    user_data = {"age": 28, "weight": 75, "activity_level": "high", "goal": "muscle_gain"}
    expected_program = ["Strength: 4x per week", "Cardio: 15 minutes, 2x per week"]
    assert generate_fitness_program(user_data) == expected_program

def test_generate_fitness_program_unsupported_goal():
    user_data = {"age": 35, "weight": 68, "activity_level": "low", "goal": "yoga"}
    assert generate_fitness_program(user_data) == ["Goal not supported"]


# Tets pour la fonction suggest_improvements
def test_suggest_improvements_positive_trend():
    assert suggest_improvements([3, 5]) == "Great progress! Consider increasing intensity or duration."

def test_suggest_improvements_negative_trend():
    assert suggest_improvements([4, 2]) == "Activity has decreased. Try to maintain consistency."

def test_suggest_improvements_no_change():
    assert suggest_improvements([3, 3]) == "Consistency is key. Keep up the good work!"

# Tests for error handling
def test_invalid_data_types():
    with pytest.raises(ValueError):
        validate_user_data({"age": "vingt", "weight": "soixante", "activity_level": "modere", "goal": "perte de poids"})

def test_extreme_values():
    assert not validate_user_data({"age": 200, "weight": 70, "activity_level": "modere", "goal": "perte de poids"})

def test_missing_all_fields():
    assert not validate_user_data({})