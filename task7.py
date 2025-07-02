def compute_statistics(numbers):
    # Use built-in sorted for sorting
    sorted_numbers = sorted(numbers)

    # Manual calculation of sum, min, max
    total = 0
    count = 0
    minimum = sorted_numbers[0]
    maximum = sorted_numbers[0]

    for num in sorted_numbers:
        total += num
        count += 1
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / count if count > 0 else 0

    return {
        'Sum': total,
        'Average': round(average, 2),
        'Minimum': minimum,
        'Maximum': maximum,
        'Sorted List': sorted_numbers
    }

def display_statistics(stats):
    print("\n Smart List Analysis Summary:")
    for index, (key, value) in enumerate(stats.items(), start=1):
        print(f"{index}. {key}: {value}")

def is_valid_number_list(input_str):
    try:
        numbers = [float(x) for x in input_str.split()]
        return numbers
    except ValueError:
        return None

# ==== Main Program ====

print(" Welcome to Smart List Analyzer 🔍")
user_input = input("Enter a list of numbers (space-separated): ")

numbers = is_valid_number_list(user_input)

if numbers is None:
    print(" Invalid input. Please enter only numbers separated by spaces.")
else:
    stats = compute_statistics(numbers)
    display_statistics(stats)
