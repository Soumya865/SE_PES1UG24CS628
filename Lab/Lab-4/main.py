from game import SlidingPuzzle


if __name__ == "__main__":
    print("Choose puzzle size:")
    print("3 - 3x3")
    print("4 - 4x4")
    print("5 - 5x5")

    while True:
        choice = input("Enter size (3/4/5): ").strip()

        if choice in ("3", "4", "5"):
            size = int(choice)
            break

        print("Please enter 3, 4, or 5.")

    SlidingPuzzle(size).run()