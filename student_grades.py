# WIILLIAM RAY RESPICIO
# BSCS 3

# student_grades.py
# Part 1 — Lists Laboratory
# Task 1.1: Student Grade Manager
# Task 1.2: List Operations Practice

from typing import List, Tuple

student_names: List[str] = []
student_grades: List[float] = []


def add_student(name: str, grade: float) -> None:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    try:
        g = float(grade)
    except (TypeError, ValueError):
        raise ValueError("Grade must be a number.")
    if g < 0 or g > 100:
        raise ValueError("Grade must be between 0 and 100.")
    student_names.append(name.strip())
    student_grades.append(g)
    if g.is_integer():
        print(f"Added {name} with grade {int(g)}")
    else:
        print(f"Added {name} with grade {g}")


def average_grade() -> float:
    if not student_grades:
        return 0.0
    return sum(student_grades) / len(student_grades)


def highest_grade() -> float:
    if not student_grades:
        return 0.0
    return max(student_grades)


def display_grades() -> None:
    print("Student Grades:")
    for name, grade in zip(student_names, student_grades):
        if float(grade).is_integer():
            print(f"{name}: {int(grade)}")
        else:
            print(f"{name}: {grade}")


def remove_student(name: str) -> bool:
    if name in student_names:
        idx = student_names.index(name)
        removed = (student_names.pop(idx), student_grades.pop(idx))
        print(f"Removed {removed[0]} with grade {int(removed[1]) if float(removed[1]).is_integer() else removed[1]}")
        return True
    return False


def list_operations(numbers: List[int]) -> Tuple[List[int], int, float, int, int, int]:
    if not numbers:
        return [], 0, 0.0, 0, 0, 0
    sorted_list = sorted(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    mx = max(numbers)
    mn = min(numbers)
    ln = len(numbers)
    return sorted_list, total, avg, mx, mn, ln


def prompt_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Please enter a valid number.")


def prompt_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")


def menu():
    while True:
        print("\n== Student Grade Manager ==")
        print("1) Add student and grade")
        print("2) Display all students and grades")
        print("3) Show average grade")
        print("4) Show highest grade")
        print("5) Remove a student")
        print("6) List operations practice")
        print("0) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            grade = prompt_float("Grade (0-100): ")
            try:
                add_student(name, grade)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            display_grades()
        elif choice == "3":
            avg = average_grade()
            print(f"Average Grade: {avg}")
        elif choice == "4":
            hi = highest_grade()
            if float(hi).is_integer():
                print(f"Highest Grade: {int(hi)}")
            else:
                print(f"Highest Grade: {hi}")
        elif choice == "5":
            name = input("Enter exact student name to remove: ").strip()
            ok = remove_student(name)
            if not ok:
                print("Student not found.")
        elif choice == "6":
            raw = input("Enter integers separated by spaces (e.g., 5 2 8 1 9 3): ").strip()
            try:
                nums = [int(x) for x in raw.split()] if raw else []
            except ValueError:
                print("Invalid list, use integers only.")
                continue
            sorted_list, total, avg, mx, mn, ln = list_operations(nums)
            print("Sorted:", sorted_list)
            print("Sum:", total)
            print("Average:", avg)
            print("Max:", mx)
            print("Min:", mn)
            print("Length:", ln)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
