def main():
    user_name = input("Enter your name: ")
    user_city = input("Enter your city: ")

    while True:
        try:
            user_age = int(input("Enter your age: "))
            if user_age >= 0 and user_age <= 120:
                break
            else:
                print("Error: Age must be between 0 and 120.")
        except ValueError:
            print("Error: Please enter a valid number, not text.")

    birth_year = 2026 - user_age

    if user_age >= 18:
        status = "You are an adult."
    else:
        status = "You are a minor."

    print(f"Hello, {user_name}! You live in {user_city} and were likely born in {birth_year}. {status}")

if __name__ == "__main__":
    main()