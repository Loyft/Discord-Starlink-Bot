def check_for_reaction(message):

    reaction = ""

    # elif goes brrrrrrr til i make json
    if "alien" in message:
        reaction = "👽"
    elif "Alien" in message:
        reaction = "👽"
    elif "ufo" in message:
        reaction = "🛸"
    elif "Ufo" in message:
        reaction = "🛸"
    elif "UFO" in message:
        reaction = "🛸"
    elif "rocket" in message:
        reaction = "🚀"
    elif "Rocket" in message:
        reaction = "🚀"

    return reaction
