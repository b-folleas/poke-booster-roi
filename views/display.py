from tabulate import tabulate


def paginate_and_display(data, headers, page_size=20):
    """Generic function to paginate and display tabular data."""
    total_pages = (len(data) + page_size - 1) // page_size

    for page in range(total_pages):
        start = page * page_size
        end = start + page_size
        table = data[start:end]

        print(tabulate(table, headers=headers, tablefmt="grid"))
        print(f"Page {page + 1}/{total_pages}")

        if page < total_pages - 1:
            input("Press Enter to display the next page...")


def print_sets(sets, page_size=20):
    """Display available sets with pagination."""
    table_data = [(s['id'], s['series'], s['name'], s['releaseDate'], s['total']) for s in sets]
    headers = ["ID", "Series", "Name", "Release date", "Total Cards"]
    paginate_and_display(table_data, headers, page_size)


def print_cards(cards, total_cards, page_size=50):
    """Display cards and their price with pagination."""
    table_data = []

    for card in cards:
        card_id = card["id"]
        name = card["name"]
        number = card["number"]
        number_display = f"{number}/{total_cards}"

        prices = card.get("tcgplayer", {}).get("prices", {})
        price_list = [
            prices.get("normal", {}).get("market"),
            prices.get("reverseHolofoil", {}).get("market")
        ]

        valid_prices = [p for p in price_list if p is not None]
        market_price = valid_prices[len(valid_prices) // 2] if valid_prices else "N/A"

        table_data.append([card_id, number_display, name, market_price])

    headers = ["ID", "Number", "Card", "Price ($)"]
    paginate_and_display(table_data, headers, page_size)
