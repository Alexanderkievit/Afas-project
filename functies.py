import random

def deviation_calculate(original_value, min_value, max_value, number_of_decimal = "0"):
    deviation_calculate = int(original_value) * ((int((max_value - min_value + 1) * random.randint(int(number_of_decimal), 5) + int(min_value))) / 100)
    return deviation_calculate

def random_value(min_value, max_value, number_of_decimal):
    random_value = int((max_value - min_value + 1) * random.randint() + min_value)
    return random_value

def value_sum(first_value, second_value, number_of_decimal = "0"):
    value_sum = round((first_value + second_value), int(number_of_decimal))
    return value_sum

def value_sub(first_value, second_value, number_of_decimal = "0"):
    value_sub = round((first_value - second_value), int(number_of_decimal))
    return value_sub

def value_mult(first_value, second_value, number_of_decimal = "0"):
    value_mult = round((first_value * second_value), int(number_of_decimal))
    return value_mult

def value_dev(first_value, second_value, number_of_decimal = "0"):
    value_dev = round((first_value / second_value), int(number_of_decimal))
    return value_dev