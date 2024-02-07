from itertools import permutations

def generate_permutations(digits, with_repetition=False):
    if with_repetition:
        return permutations(digits)
    else:
        return permutations(digits, len(digits))

def main():
    digits = input("Enter a set of digits (comma-separated): ").split(',')
    
    # Remove any leading/trailing whitespace from input
    digits = [digit.strip() for digit in digits]

    # Generate permutations without repetition
    permutations_without_repetition = generate_permutations(digits)

    print("Permutations without repetition:")
    for perm in permutations_without_repetition:
        print(''.join(perm))

    # Generate permutations with repetition
    permutations_with_repetition = generate_permutations(digits, with_repetition=True)

    print("\nPermutations with repetition:")
    for perm in permutations_with_repetition:
        print(''.join(perm))

if __name__ == "__main__":
    main()
