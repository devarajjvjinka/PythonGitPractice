for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))

fast_food_items.popitem()
print(fast_food_items)


internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  # use to update the dictionary
gamers = internet_celebrities.copy()  # copy the dictionary with reference
internet_celebrities.clear()  # clears the dictionary
print(internet_celebrities)  #
print(gamers)  # 6


#gamers.setdefault("shroud","Social media") dictionary cannot be overridden with set default

gamers.setdefault("Instagram","Social media")

gamers["Ninja"]="Manja"

print(gamers)


