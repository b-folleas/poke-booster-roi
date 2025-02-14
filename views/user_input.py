def get_user_choice():
    """Display options and get user's choice."""
    while True:
        print("\nOptions:")
        print("1. Enter a set code directly")
        print("2. Display sets by series")
        print("3. Display all sets")
        print("0. Exit")

        choice = input("Choose an option (0-3): ").strip().lower()

        if choice in ["0", "done", "exit", "bye"]:
            return None
        if choice in ["1", "2", "3"]:
            return choice

        print("Error: Invalid option, please try again.")


def select_set(sets):
    """Allow user to select a set based on their choice."""
    while True:
        choice = get_user_choice()
        if choice is None:
            return None

        if choice == "1":
            set_id = input("Enter the set code: ").strip()
            selected_set = next((s for s in sets if s["id"] == set_id), None)
            if selected_set:
                return selected_set
            print("Error: Set not found, please try again.")

        elif choice == "2":
            series = sorted(set(s["series"] for s in sets))
            print("\nAvailable series:")
            for i, s in enumerate(series, start=1):
                print(f"{i}. {s}")

            try:
                series_choice = int(input("\nSelect a series number: ")) - 1
                if 0 <= series_choice < len(series):
                    selected_series = series[series_choice]
                    sets_in_series = [s for s in sets if s["series"] == selected_series]
                    return sets_in_series
                else:
                    print("Error: Invalid number.")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "3":
            return sets
