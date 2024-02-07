def evaluate_polynomial(coefficients, n):
    """
    Evaluate a polynomial function for a given value of n.

    Parameters:
        coefficients (list): Coefficients of the polynomial function.
        n (int): Value of n.

    Returns:
        int: Result of evaluating the polynomial function for the given value of n.
    """
    result = 0
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        result += coeff * (n ** (degree - i))
    return result

def main():
    # Example polynomial: f(x) = 4n^2 + 2n + 9
    coefficients = [4, 2, 9]
    n = int(input("Enter the value of n: "))

    result = evaluate_polynomial(coefficients, n)
    print(f"The result of evaluating the polynomial for n = {n} is: {result}")

if __name__ == "__main__":
    main()
