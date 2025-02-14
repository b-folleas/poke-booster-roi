from api.tcg_api import get_sets, get_cards_from_set
from services.price_analysis import calculate_expected_value
from views.display import print_sets, print_cards
from views.user_input import select_set


def main():
    print("Fetching sets...")
    sets = get_sets()

    while True:
        selected_set_or_list = select_set(sets)
        if selected_set_or_list is None:
            print("\nGoodbye!")
            break

        if isinstance(selected_set_or_list, list):
            print_sets(selected_set_or_list)
            continue  # Back to menu after printing

        selected_set = selected_set_or_list
        print(f"\nRetrieving cards from set: {selected_set['name']} ({selected_set['id']})...")
        cards = get_cards_from_set(selected_set["id"])

        expected_value = calculate_expected_value(cards)
        print(f"\nEstimated booster value: {expected_value}$")

        while True:  # Print cards or back to menu
            choice = input("\nDo you want to see the detailed card list? (y/n): ").strip().lower()
            if choice in ["y", "yes"]:
                print_cards(cards, selected_set["total"])
                break
            elif choice in ["n", "no"]:
                break
            else:
                print("Invalid choice, please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
