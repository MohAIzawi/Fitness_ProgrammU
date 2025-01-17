def validate_user_data(user_data):
    required_fields = ["age", "weight", "activity_level", "goal"]
    for field in required_fields:
        if field not in user_data:
            return False
    if user_data["age"] <= 0:
        return False
    return True

def generate_fitness_program(user_data):
    if not validate_user_data(user_data):
        return None

    goal = user_data["goal"].lower()
    if goal == "weight_loss":
        return ["Cardio: 30 minutes, 5x per week", "Strength: 2x per week"]
    elif goal == "muscle_gain":
        return ["Strength: 4x per week", "Cardio: 15 minutes, 2x per week"]
    return ["Goal not supported"]
