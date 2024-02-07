def find_solutions(n, target_sum):
    solutions = []
    for x1 in range(target_sum + 1):
        for x2 in range(target_sum + 1 - x1):
            for x3 in range(target_sum + 1 - x1 - x2):
                # Add more loops for additional variables x4, x5, ..., xn if needed
                x_n = target_sum - x1 - x2 - x3
                if x_n >= 0:
                    solutions.append((x1, x2, x3, x_n))
    return solutions

def main():
    n = int(input("Enter the number of variables (n): "))
    target_sum = int(input("Enter the target sum (C): "))

    if target_sum > 10:
        print("Error: Target sum must be less than or equal to 10.")
        return

    solutions = find_solutions(n, target_sum)

    print(f"\nSolutions for x1 + x2 + x3 + ... + xn = {target_sum}:")
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
