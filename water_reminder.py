def calculate_water_intake(weight, age):
    return round((weight * 35) / 1000, 2)

def suggest_reminder_interval(age):
    if age < 30:
        return "Every 2 hours"
    elif 30 <= age <= 55:
        return "Every 3 hours"
    else:
        return "Every 4 hours"

def recommend_water_temperature(age):
    if age < 30:
        return "Cool water"
    elif 30 <= age <= 55:
        return "Room temperature water"
    else:
        return "Lukewarm water"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age: "))

        if weight <= 0 or age <= 0:
            raise ValueError("Inputs must be positive numbers.")

        water_intake = calculate_water_intake(weight, age)
        interval = suggest_reminder_interval(age)
        temperature = recommend_water_temperature(age)

        print(f"\nRecommended daily water intake: {water_intake} liters")
        print(f"Reminder interval: {interval}")
        print(f"Ideal water temperature: {temperature}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    get_user_input()