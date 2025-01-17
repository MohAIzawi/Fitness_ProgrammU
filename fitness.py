def validate_user_data(user_data):
    if "age" not in user_data or user_data["age"] <= 0:
        return False
    if "activity_level" not in user_data:
        return False
    return True
