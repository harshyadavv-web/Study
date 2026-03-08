def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = str(n)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == n

def generate_armstrong_numbers(limit):
    """Generate all Armstrong numbers up to the given limit."""
    armstrong_numbers = []
    for num in range(1, limit + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Example usage
if __name__ == "__main__":
    limit = 10000
    results = generate_armstrong_numbers(limit)
    print(f"Armstrong numbers up to {limit}: {results}")