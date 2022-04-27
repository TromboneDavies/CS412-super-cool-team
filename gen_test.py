import itertools
import random

def main():
    letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y".split()
    tests = {}
    for line in itertools.product(list(letters), repeat=2):
        a, b = line
        if a != b and (b, a) not in tests:
            tests[line] = random.randint(1, 10)
    final = f"{len(letters)}\n"
    for test in tests:
        a, b = test
        c = tests[test]
        final += f"{a} {b} {c}\n"
    
    with open("test.txt", "w+") as f:
        f.write(final)

if __name__ == "__main__":
    main()
