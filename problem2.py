def generate_odd_series(a):
    if a <= 0:
        return ""
    odd_numbers = []
    count = 0
    num = 1
    while count < a:
        odd_numbers.append(str(num))
        num += 2
        count += 1
    return ",".join(odd_numbers)

if __name__ == "__main__":
    a = int(input("Enter the number of odd numbers to generate: "))
    print("Odd Number Series:", generate_odd_series(a))
