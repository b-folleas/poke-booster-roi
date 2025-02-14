def estimate_price(card):
    """Estimate the price of a card in perfect condition (using a reasonable price)."""

    # Price estimation for Cardmarket
    def estimate_price_cardmarket(prices):
        """Estimate the price of a card from Cardmarket."""
        # Retrieve prices
        price = prices.get('avg1')
        reverse_holo_price = prices.get('reverseHoloAvg1')

        # Filter out abnormal prices
        valid_prices = [price, reverse_holo_price]
        valid_prices = [p for p in valid_prices if (p is not None or p == 0)]

        # If no valid price is found, return a default price
        if not valid_prices:
            return 0.01

        # Return the median price
        valid_prices.sort()
        return valid_prices[len(valid_prices) // 2]

    # Price estimation for TCGPlayer
    def estimate_price_tcgplayer(prices):
        """Estimate the price of a card from TCGPlayer."""
        # Retrieve prices for normal and reverse holo cards
        normal_price = prices.get('normal', {}).get('market')
        reverse_holo_price = prices.get('reverseHolofoil', {}).get('market')

        # Filter out abnormal prices
        valid_prices = [normal_price, reverse_holo_price]
        valid_prices = [p for p in valid_prices if (p is not None or p == 0)]

        # If no valid price is found, return a default price
        if not valid_prices:
            return 0.01

        # Return the median price
        valid_prices.sort()
        return valid_prices[len(valid_prices) // 2]

    # Retrieve prices from TCGPlayer and Cardmarket
    tcgplayer_prices = card.get('tcgplayer', {}).get('prices', {})
    cardmarket_prices = card.get('cardmarket', {}).get('prices', {})

    # Estimate prices for each source
    tcgplayer_estimate = estimate_price_tcgplayer(tcgplayer_prices)
    cardmarket_estimate = estimate_price_cardmarket(cardmarket_prices)

    # Return the average of the estimated prices
    return round((tcgplayer_estimate + cardmarket_estimate) / 2, 2)


def get_probability(card):
    """Return the probability of a card based on its rarity or other criteria."""
    rarity = card.get("rarity", "").lower()

    # Mapping rarities to estimated probabilities
    rarity_probabilities = {
        "common": 0.75,
        "uncommon": 0.20,
        "rare": 0.05,
        "holo": 0.02,
        "rare holo": 0.01,
        "legendary": 0.01,
        "mythical": 0.005
    }

    # Return the probability based on rarity, or a default value
    return rarity_probabilities.get(rarity, 0.02)  # Default value for unknown rarities


def calculate_expected_value(cards):
    """Calculate the expected value of a booster pack based on the cards."""
    total_value = 0
    for card in cards:
        # Estimate the price of the card in perfect condition
        price = estimate_price(card)

        # Estimated probability of pulling this card from the booster
        probability = get_probability(card)

        # Add to the total expected value
        total_value += price * probability

    # Return the expected value rounded to 2 decimal places
    return round(total_value, 2)
