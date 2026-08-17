import math
def parse_positive_integer(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required.")

    try:
        number = int(str(value).strip())
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a whole number.")

    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")

    return number



def parse_positive_float(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required.")

    try:
        number = float(str(value).strip())
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a number.")

    if not math.isfinite(number):
        raise ValueError(f"{field_name} must be a real, finite number.")

    if number <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")

    return number

def analyze_triangular_number(number):
    number = parse_positive_integer(number, "Number")

    test_value = (8 * number) + 1
    root = math.isqrt(test_value)

    if root ** 2 == test_value:
        position = (root - 1) // 2
        is_triangular = True
        explanation = (
            f"8({number}) + 1 = {test_value}, which is {root}². "
            f"Therefore, {number} = {position}({position} + 1) ÷ 2, "
            f"so it is triangular."
        )
    else:
        position = None
        is_triangular = False
        explanation = (
            f"8({number}) + 1 = {test_value}, which is not a perfect square. "
            f"Therefore, {number} is not triangular."
        )

    values = {
        "number": number,
        "is_triangular": is_triangular,
        "position": position,
        "test_value": test_value,
        "root": root,
        "explanation": explanation,
    }

    return values

def generate_collatz_sequence(starting_number, max_steps=100):
    number = parse_positive_integer(starting_number, "Starting number")
    max_steps = parse_positive_integer(max_steps, "Maximum steps")

    sequence = [number]
    current_number = number
    steps = 0
    highest_value = number

    while current_number != 1 and steps < max_steps:
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = (current_number * 3) + 1

        sequence.append(current_number)
        steps += 1

        if current_number > highest_value:
            highest_value = current_number

    reached_one = current_number == 1

    values = {
        "starting_number": number,
        "sequence": sequence,
        "steps": steps,
        "highest_value": highest_value,
        "reached_one": reached_one,
        "max_steps": max_steps,
    }

    return values

def calculate_circle_accuracy(circumference, diameter):
    circumference = parse_positive_float(circumference, "Circumference")
    diameter = parse_positive_float(diameter, "Diameter")

    measured_ratio = circumference / diameter

    difference = abs(measured_ratio - math.pi)
    percent_error = (difference / math.pi) * 100

    if percent_error <= 0.1:
        rating = "Extremely close"
    elif percent_error <= 1:
        rating = "Very close"
    elif percent_error <= 5:
        rating = "Somewhat close"
    else:
        rating = "Not close"

    expected_circumference = diameter * math.pi
    circumference_difference = abs(
        circumference - expected_circumference
    )

    values = {
        "circumference": circumference,
        "diameter": diameter,
        "measured_ratio": measured_ratio,
        "pi_value": math.pi,
        "difference": difference,
        "percent_error": percent_error,
        "expected_circumference": expected_circumference,
        "circumference_difference": circumference_difference,
        "rating": rating,
    }

    return values




