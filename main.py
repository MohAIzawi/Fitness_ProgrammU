from fitness import generate_fitness_program, suggest_improvements

def main():
    print("Welcome to the Fitness ProgramU!")
    print("Please answer the following questions to get your fitness program.")

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    activity_level = input("Enter your activity level (low, moderate, high): ")
    goal = input("Enter your fitness goal (weight_loss, muscle_gain): ")

    user_data = {
        "age": age,
        "weight": weight,
        "activity_level": activity_level,
        "goal": goal
    }

    program = generate_fitness_program(user_data)
    if program:
        print("\nYour fitness program:")
        for activity in program:
            print(f"- {activity}")
    else:
        print("Invalid user data or unsupported goal.")

    print("\nWould you like suggestions for improvements based on your activity history? (yes/no)")
    if input().strip().lower() == "yes":
        activity_history = []
        print("Enter your activity history (enter 'done' to finish):")
        while True:
            activity = input("Enter activity level: ")
            if activity.lower() == 'done':
                break
            try:
                activity_history.append(int(activity))
            except ValueError:
                print("Please enter a valid number or 'done' to finish.")

        suggestions = suggest_improvements(activity_history)
        print("\nImprovement Suggestions:")
        print(suggestions)

if __name__ == "__main__":
    main()