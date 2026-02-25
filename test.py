def get_percentage():
    try:
        value = float(input("Enter a percentage (0–100): "))

        if value < 0 or value > 100:
            raise ValueError("Percentage must be between 0 and 100.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

    else:
        # runs only if no exception was raised in try
        print("Thanks, valid percentage!")
        return value

    finally:
        # always runs, whether there was an error or not
        print("Done checking input.")


get_percentage()
