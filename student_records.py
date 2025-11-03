# WIILLIAM RAY RESPICIO
# BSCS 3

# student_records.py
# Part 4 — File Handling Laboratory
# Task 4.1: Student Records File System
# Task 4.2: File Operations Practice

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Dict, Any, Optional

Student = Dict[str, Any]
StudentsDB = Dict[str, Student]

# In-memory store for interactive session
records: StudentsDB = {}

# ---------------------------
# Task 4.1: Core file functions
# ---------------------------


def save_records(data: StudentsDB, filepath: str | Path) -> bool:
    """
    Save student records to a pickle file with robust error handling.
    Returns True on success, False otherwise.
    """
    path = Path(filepath)
    try:
        if path.parent and str(path.parent) != ".":
            path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        print(f"Saved {len(data)} records to {path}")
        return True
    except (OSError, pickle.PicklingError) as e:
        print(f"Error saving to {path}: {e}")
        return False


def load_records(filepath: str | Path) -> Optional[StudentsDB]:
    """
    Load student records from a pickle file with robust error handling.
    Returns the loaded dict on success, or None on failure.
    """
    path = Path(filepath)
    try:
        with path.open("rb") as f:
            loaded: StudentsDB = pickle.load(f)
        if not isinstance(loaded, dict):
            print(f"Unexpected data format in {path}; expected dict.")
            return None
        print(f"Loaded {len(loaded)} records from {path}")
        return loaded
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except (OSError, EOFError, pickle.UnpicklingError) as e:
        print(f"Error loading from {path}: {e}")
        return None


def export_to_text(data: StudentsDB, filepath: str | Path) -> bool:
    """
    Export student records to a human-readable text file.
    Returns True on success, False otherwise.
    """
    path = Path(filepath)
    try:
        if path.parent and str(path.parent) != ".":
            path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            if not data:
                f.write("No records.\n")
            else:
                for sid in sorted(data.keys()):
                    info = data[sid]
                    line = (
                        f"ID: {sid} | "
                        f"Name: {info.get('name', '')} | "
                        f"Grade: {info.get('grade', '')} | "
                        f"Major: {info.get('major', '')}\n"
                    )
                    f.write(line)
        print(f"Exported {len(data)} records to {path}")
        return True
    except OSError as e:
        print(f"Error exporting to {path}: {e}")
        return False

# ---------------------------
# Task 4.1: Sample data & helpers
# ---------------------------


def sample_students() -> StudentsDB:
    """
    Create sample student data for testing.
    """
    return {
        "1001": {"name": "Alice", "grade": "A", "major": "Computer Science"},
        "1002": {"name": "Bob", "grade": "B+", "major": "Information Systems"},
        "1003": {"name": "Charlie", "grade": "A-", "major": "Software Engineering"},
    }


def add_record_interactive() -> None:
    """
    Prompt user to add a record into in-memory 'records'.
    """
    sid = input("ID: ").strip()
    name = input("Name: ").strip()
    grade = input("Grade: ").strip()
    major = input("Major: ").strip()
    if not sid or not name or not grade or not major:
        print("All fields are required.")
        return
    records[sid] = {"name": name, "grade": grade, "major": major}
    print(f"Added ID {sid}")


def show_records(data: StudentsDB | None = None) -> None:
    """
    Display records from provided dict or from in-memory 'records'.
    """
    view = data if data is not None else records
    if not view:
        print("No records.")
        return
    for sid in sorted(view.keys()):
        info = view[sid]
        print(
            f"ID: {sid} | "
            f"Name: {info.get('name', '')} | "
            f"Grade: {info.get('grade', '')} | "
            f"Major: {info.get('major', '')}"
        )


def clear_records() -> None:
    records.clear()
    print("Cleared all in-memory records.")


def quick_test(save_path: str = "students.pkl", txt_path: str = "students.txt") -> None:
    """
    Create sample data, save, load, and export to verify the full flow.
    """
    print("Creating sample student data...")
    data = sample_students()
    show_records(data)
    print("\nSaving with pickle...")
    if not save_records(data, save_path):
        return
    print("Loading from pickle...")
    loaded = load_records(save_path)
    if loaded is None:
        return
    print("Loaded data:")
    show_records(loaded)
    print("\nExporting to text...")
    export_to_text(loaded, txt_path)

# ---------------------------
# Task 4.2: File mode demo
# ---------------------------


def demo_file_modes(base_path: str = "demo_file_ops.txt") -> None:
    """
    Demonstrate 'w', 'r', and 'a' using with statements.
    Handles file-not-found when reading.
    """
    path = Path(base_path)

    # Write mode ('w'): create/overwrite
    try:
        with path.open("w", encoding="utf-8") as f:
            f.write("Line 1: Created with write mode.\n")
        print(f"Write complete -> {path}")
    except OSError as e:
        print(f"Error writing to {path}: {e}")
        return

    # Read mode ('r'): read existing
    try:
        with path.open("r", encoding="utf-8") as f:
            print("Initial file contents:")
            print(f.read())
    except FileNotFoundError:
        print(f"File not found for reading: {path}")
    except OSError as e:
        print(f"Error reading {path}: {e}")

    # Append mode ('a'): append more lines
    try:
        with path.open("a", encoding="utf-8") as f:
            f.write("Line 2: Appended line.\n")
            f.write("Line 3: Another appended line.\n")
        print("Append complete.")
    except OSError as e:
        print(f"Error appending to {path}: {e}")
        return

    # Read again to show final contents
    try:
        with path.open("r", encoding="utf-8") as f:
            print("Final file contents:")
            print(f.read())
    except FileNotFoundError:
        print(f"File not found for reading: {path}")
    except OSError as e:
        print(f"Error reading {path}: {e}")

# ---------------------------
# Interactive menu
# ---------------------------


def menu():
    while True:
        print("\n== Student Records File System (Part 4) ==")
        print("1) Add record")
        print("2) Show in-memory records")
        print("3) Clear in-memory records")
        print("4) Save records to pickle")
        print("5) Load records from pickle")
        print("6) Export records to text")
        print("7) Quick test: sample -> save -> load -> export")
        print("8) Demo file modes (w/r/a)")
        print("0) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_record_interactive()
        elif choice == "2":
            show_records()
        elif choice == "3":
            clear_records()
        elif choice == "4":
            path = input("Pickle path (default students.pkl): ").strip() or "students.pkl"
            save_records(records, path)
        elif choice == "5":
            path = input("Pickle path to load (default students.pkl): ").strip() or "students.pkl"
            loaded = load_records(path)
            if loaded is not None:
                records.clear()
                records.update(loaded)
        elif choice == "6":
            path = input("Text export path (default students.txt): ").strip() or "students.txt"
            export_to_text(records, path)
        elif choice == "7":
            pkl = input("Pickle path (default students.pkl): ").strip() or "students.pkl"
            txt = input("Text path (default students.txt): ").strip() or "students.txt"
            quick_test(pkl, txt)
        elif choice == "8":
            path = input("Demo file path (default demo_file_ops.txt): ").strip() or "demo_file_ops.txt"
            demo_file_modes(path)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
