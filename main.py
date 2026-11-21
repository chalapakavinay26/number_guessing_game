import random

def number_guessing_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    print("\n=== Number Guessing Game ===")
    print("1 or 50 middle one number hide.")
    print(f"you max attempts {max_attempts} you have chances!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - your guessing number enter: "))
        except ValueError:
            print("please enter correct number!\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("try high number ! (Too low)\n")
        elif guess > secret_number:
            print("try small number! (Too high)\n")
        else:
            print(f"super! you {attempts} attempt correct number ({secret_number}) you found!")
            return

    print(f"ohh noo, chances gone! hide number: {secret_number}")


if __name__ == "__main__":
    number_guessing_game()
