from sys import stdin


def main():
    # reading from stdin and creating a linked list
    maximum = -float("inf")
    for line in stdin:
        number = int(line)
        if number > maximum:
            maximum = number
    # searching and printing out the result
    print(maximum)


if __name__ == "__main__":
    main()
