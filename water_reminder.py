def calculate_water_intake(weight, age):
    return round((weight * 35) / 1000, 2)

def suggest_reminder_interval(age):
    if age < 30:
        return "Every 2 hours"
    elif 30 <= age <= 55:
        return "Every 3 hours"
    else:
        return "Every 4 hours"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age: "))

        if weight <= 0 or age <= 0:
            raise ValueError

        water_intake = calculate_water_intake(weight, age)
        interval = suggest_reminder_interval(age)

        print(f"\nRecommended daily water intake: {water_intake} liters")
        print(f"Reminder interval: {interval}")

    except ValueError:
        print("Invalid input: Input must be positive numbers")

if __name__ == "__main__":
    get_user_input()
