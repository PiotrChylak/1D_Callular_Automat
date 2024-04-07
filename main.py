import os
import random

if __name__ == "__main__":
    rule = input("Enter the rule: ")
    n = int(input("Enter the length of random sequence: "))
    k = int(input("Enter the number of iterations: "))
    file = input("Enter the file name: ")
    location = "C:\\Users\\piotc\\Desktop\\Automat"  # You have to paste your own path :)
    file_path = os.path.join(location, file)

    random_sequence = [random.choice(['*', '_']) for _ in range(n)]
    bottom_sequence = ['_' for _ in range(n)]

    rule_dictionary = {}
    patterns = ['***', '**_', '*_*', '*__', '_**', '_*_', '__*', '___']
    for i, pattern in enumerate(patterns):
        rule_dictionary[pattern] = rule[i]

    for j in range(k):
        pattern = ''.join(random_sequence[j % n] + random_sequence[(j + 1) % n] + random_sequence[(j + 2) % n])
        # print(pattern)
        # print(rule_dictionary[pattern])
        bottom_sequence[j % n] = rule_dictionary[pattern]

    result = ''.join('*' if char == '1' else '_' for char in bottom_sequence)

    print("Rule dictionary:", rule_dictionary)
    print("\n")
    print("Random sequence:", ''.join(random_sequence))
    print("Result sequence:", result)
    print("\n")

    with open(file_path, "w") as f:
        f.write("Rule: {}\n".format(rule))
        f.write("Number of steps: {}\n".format(k))
        f.write("Random sequence: {}\n".format(''.join(random_sequence)))
        f.write("Result sequence: {}\n".format(result))
    print("Result saved to", file_path)
