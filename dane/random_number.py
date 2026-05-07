import json


def random_number():
    FILENAME = "seed.json"
    try:
        with open(FILENAME, 'r') as f:
            data = json.load(f)
            last_x = data["last_value"]
    except FileNotFoundError:
        last_x = 12345


    new_x = (1103515245 * last_x + 12345) % 2147483648

    with open(FILENAME, "w") as f:

        json.dump({"last_value": new_x}, f)

    return new_x


wynik = random_number()
print(f"Moja losowa liczba: {wynik}")
