def detect_zombie(message):
    has_smiley = ":)" in message
    has_frowny = ":(" in message

    if has_smiley and not has_frowny:
        return "alive"
    elif has_frowny and not has_smiley:
        return "undead"
    elif has_smiley and has_frowny:
        return "double agent"
    else:
        return "machine"


# Example usage
input_message = input()
result = detect_zombie(input_message)
print(result)
