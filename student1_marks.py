
def calculate_marks():
    try:
        name = input("Enter student name: ")

        mark1 = float(input("Enter Tamil mark: "))
        mark2 = float(input("Enter English mark: "))
        mark3 = float(input("Enter Python mark: "))

        marks = [mark1, mark2, mark3]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Marks must be between 0 and 100!")
            return

        total = sum(marks)
        average = total / 3

        print("\n--- Student Result ---")
        print("Name:", name)
        print("Total:", total)
        print("Average:", average)

        if all(mark >= 35 for mark in marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")

    except ValueError:
        print("Please enter valid numbers!")

calculate_marks()
