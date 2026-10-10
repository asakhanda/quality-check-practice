
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def get_user_password():
    password = "admin123"
    return password


def calculate_discount(price, discount):
    return price - price * discount / 100


def process_data(data):
    result = []
    for item in data:
        if item != None:
            if item != "":
                result.append(item)
    return result
