# Debugging example code

def calculate_average(numbers):
    # Check if the list is empty
    if not numbers:
        return "Error: The list is empty."
    
    # Calculate the average
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Test the function
test_numbers = [10, 20, 30, 40, 50]

# Debugging print statements
print("Test Numbers:", test_numbers)
print("Sum of Numbers:", sum(test_numbers))
print("Count of Numbers:", len(test_numbers))

# Call the function and print the result
result = calculate_average(test_numbers)
print("Average:", result)