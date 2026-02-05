full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."

    stats = [strength, intelligence, charisma]

    for stat in stats:
        if type(stat) is not int:
            return "All stats should be integers."

    for stat in stats:
        if stat < 1:
            return "All stats should be no less than 1."

    for stat in stats:
        if stat > 4:
            return "All stats should be no more than 4."

    if sum(stats) != 7:
        return "The character should start with 7 points."

    def make_line(label, value):
        return f"{label} " + full_dot * value + empty_dot * (10 - value)

    result = name + "\n"
    result += make_line("STR", strength) + "\n"
    result += make_line("INT", intelligence) + "\n"
    result += make_line("CHA", charisma) + "\n"

    return result
