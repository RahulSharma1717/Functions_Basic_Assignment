# Create a return type function that takes marks of 5 subjects from a student and calculates the percentage of the student.

def calculate_percentage():
    marks = input("Enter marks for 5 subjects separated by spaces: ")
    my_list = list(map(int, marks.split()))

    # Ensure exactly 5 marks are entered
    if len(my_list) != 5:
        print("Error: Please enter exactly 5 marks.")
        return

    # Validate that all marks are within the range 0 to 100
    for m in my_list:
        if not (0 <= m <= 100):
            print(f"Error: Invalid mark {m}. Marks should be between 0 and 100.")
            return

    # Calculate total and percentage
    total = sum(my_list)
    percentage = total / 500 * 100
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")

# Call the function
if __name__ == "__main__":
    calculate_percentage()



"""Output:
Enter marks for 5 subjects separated by spaces: 52 63 47 85 94
Total Marks: 341
Percentage: 68.20%"""

"""Enter marks for 5 subjects separated by spaces:  87 63 82 74 123
Error: Invalid mark 123. Marks should be between 0 and 100."""