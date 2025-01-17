def validate_user_data(user_data):
    required_fields = ["age", "weight", "activity_level", "goal"]
    for field in required_fields:
        if field not in user_data:
            return False
    if user_data["age"] <= 0:
        return False
    return True
