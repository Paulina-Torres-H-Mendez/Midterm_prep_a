def get_divisors(n):
    """Returns a list of all divisors of n
    :param n: An integer number
    :return: A list of divisors of n
    """
    divisors = []  # Create an empty list to store divisors
    for i in range(1, n + 1):  # Loop from 1 to n
        if n % i == 0:  # If i divides n exactly (no remainder)
            divisors.append(i)  # Add i to the list of divisors
    return divisors  # Return the list of divisors

# Example usage:
print(get_divisors(47))  # Output: [1, 47]
print(get_divisors(280))  # Output: [1, 2, 4, 7, 14, 28]