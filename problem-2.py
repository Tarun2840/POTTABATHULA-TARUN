def generate_odd_numbers(n):
    if n <= 0:
        return ""
    odd_numbers = []
    count = 0
    num = 1
    while count < n:
        odd_numbers.append(str(num))
        num += 2
        count += 1
    return ",".join(odd_numbers)


def main():
    try:
        n = int(input("Enter the number of odd numbers to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_odd_numbers(n)
            print("Odd Number Series:", series)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
