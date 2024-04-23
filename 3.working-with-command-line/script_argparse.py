import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "This script will square a number")

    parser.add_argument("number", type=int, help='The number of square')

    parser.add_argument("--twice", '-t', help='print twice', action="store_true")

    args = parser.parse_args()

    squared_number = args.number ** 2
    print(f"The square of the {args.number} is {squared_number}")

    if args.twice:
        print(f"The square of the {args.number} is {squared_number}")