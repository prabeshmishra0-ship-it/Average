def calculate_average(items):
    total = sum(items)
    average = total / len(items)
    return average

def main():
    numbers = [10, 20, 30, 40, 50]
    result = calculate_average(numbers)
    print("The average is:", result)
    return result

main()