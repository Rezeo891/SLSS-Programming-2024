# Exam Cal
# Lucas Zhang
# Mar 5 2024

def calculate_percentage(total_marks, obtained_marks):
    
    # Calculate the percentage obtained in the exam.
    
    # Args:
        # total_marks (float): Total marks for the exam.
        # obtained_marks (float): Marks obtained in the exam.
    
    # Returns:
        # float: Percentage obtained.
    
    percentage = (obtained_marks / total_marks) * 100
    return percentage

def main():
    total_marks = float(input("Enter the total marks: "))
    obtained_marks = float(input("Enter the marks obtained: "))

    percentage = calculate_percentage(total_marks, obtained_marks)

    if percentage >= 86:
        grade = "A"
    elif percentage >= 73:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Percentage obtained: {round(percentage , 2)}")
    print("Grade: ", grade)

if __name__ == "__main__":
    main()
