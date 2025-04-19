def generate_selective_odd_series(a):
    if a % 2 == 0:
        count = a // 2
    else:
        count = (a + 1) // 2

    odd_series = []
    current = 1
    while len(odd_series) < count:
        odd_series.append(str(current))
        current += 2

    return ", ".join(odd_series)


def main():
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            print("Please enter a positive integer.")
        else:
            result = generate_selective_odd_series(a)
            print("Generated Series:", result)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
