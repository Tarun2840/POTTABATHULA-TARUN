def count_multiples(lst):
    result = {i: 0 for i in range(1, 10)}
    for num in lst:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result

if __name__ == "__main__":
    try:
        input_list = list(map(int, input("Enter list of integers (space separated): ").split()))
        output = count_multiples(input_list)
        print("Multiples Count:", output)
    except ValueError:
        print("Please enter valid integers separated by commas")
