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

    def weight_loss_program():
        return ["Cardio: 30 minutes, 5x per week", "Strength: 2x per week"]

    def muscle_gain_program():
        return ["Strength: 4x per week", "Cardio: 15 minutes, 2x per week"]

    goals = {
        "weight_loss": weight_loss_program,
        "muscle_gain": muscle_gain_program,
    }

    return goals.get(user_data["goal"].lower(), lambda: ["Goal not supported"])()
