# WIILLIAM RAY RESPICIO
# BSCS 3

# student_database.py
# Part 3 — Dictionaries Laboratory
# Task 3.1: Student Database
# Task 3.2: Word Frequency Counter

from typing import Dict, Optional, Tuple, List
from collections import Counter
import re

Student = Dict[str, str]
StudentsDB = Dict[str, Student]

students: StudentsDB = {}


def add_student(student_id: str, name: str, grade: str, major: str) -> None:
    if not student_id or not name or not grade or not major:
        raise ValueError("All fields (ID, name, grade, major) are required.")
    students[student_id] = {"name": name, "grade": grade, "major": major}
    print(f"Added ID {student_id}: {name}, Grade {grade}, Major {major}")


def get_student(student_id: str) -> Optional[Student]:
    return students.get(student_id)


def update_grade(student_id: str, new_grade: str) -> bool:
    s = students.get(student_id)
    if s is None:
        return False
    s["grade"] = new_grade
    return True


def delete_student(student_id: str) -> bool:
    if student_id in students:
        del students[student_id]
        return True
    return False


def display_all() -> None:
    if not students:
        print("No students in database.")
        return
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Grade: {info['grade']} | Major: {info['major']}")


def tokenize(text: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def word_frequency(text: str) -> List[Tuple[str, int]]:
    words = tokenize(text)
    counts = Counter(words)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


def most_common_word(text: str) -> Tuple[str, int]:
    words = tokenize(text)
    counts = Counter(words)
    if not counts:
        return "", 0
    return counts.most_common(1)[0]


def menu():
    while True:
        print("\n== Student Database ==")
        print("1) Add student")
        print("2) Retrieve by ID")
        print("3) Update grade")
        print("4) Delete student")
        print("5) Display all")
        print("6) Word frequency counter")
        print("0) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid = input("ID: ").strip()
            name = input("Name: ").strip()
            grade = input("Grade (e.g., A, B+): ").strip()
            major = input("Major: ").strip()
            try:
                add_student(sid, name, grade, major)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            sid = input("Enter ID to retrieve: ").strip()
            s = get_student(sid)
            print(s if s else "Not found.")
        elif choice == "3":
            sid = input("Enter ID to update: ").strip()
            newg = input("New grade: ").strip()
            ok = update_grade(sid, newg)
            print("Updated." if ok else "ID not found.")
        elif choice == "4":
            sid = input("Enter ID to delete: ").strip()
            ok = delete_student(sid)
            print("Deleted." if ok else "ID not found.")
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("\n-- Word Frequency --")
            print("Enter/paste your text (finish with an empty line):")
            lines: List[str] = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            freqs = word_frequency(text)
            if not freqs:
                print("No words found.")
            else:
                print("Top 10:")
                for word, cnt in freqs[:10]:
                    print(f"{word}: {cnt}")
                mcw = most_common_word(text)
                print("Most common:", mcw)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
