# WIILLIAM RAY RESPICIO
# BSCS 3

# coordinates.py
# Part 2 — Tuples & Sets Laboratory
# Task 2.1: Coordinate System with Tuples
# Task 2.2: Unique Word Counter with Sets


import math
import re
from collections import Counter
from typing import Tuple, List, Set, Dict, TypedDict, Tuple as Tup

Point = Tuple[float, float]


class WordStats(TypedDict):
    total_words: int
    unique_words: Set[str]
    unique_count: int
    counts: Counter  # Counter[str]
    most_common: List[Tup[str, int]]

# ---- Task 2.1: Coordinate functions ----


def distance(p1: Point, p2: Point) -> float:
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def midpoint(p1: Point, p2: Point) -> Point:
    return (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0

# ---- Task 2.2: Text processing functions ----


def tokenize(text: str) -> List[str]:
    """
    Split text into lowercase words (alphanumeric and apostrophes).
    """
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def analyze_text(text: str, top_n: int = 5) -> WordStats:
    """
    Build words list, unique set, counts Counter, and most common list.
    """
    words: List[str] = tokenize(text)
    unique: Set[str] = set(words)
    counts: Counter = Counter(words)
    most_common: List[Tup[str, int]] = counts.most_common(top_n)
    return {
        "total_words": len(words),
        "unique_words": unique,
        "unique_count": len(unique),
        "counts": counts,
        "most_common": most_common,
    }

# ---- Interactive helpers ----


def prompt_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Please enter a valid number.")

# ---- Menus ----


def points_menu():
    print("\n-- Coordinate Operations --")
    x1 = prompt_float("x1: ")
    y1 = prompt_float("y1: ")
    x2 = prompt_float("x2: ")
    y2 = prompt_float("y2: ")
    p1, p2 = (x1, y1), (x2, y2)
    print("distance(p1, p2):", distance(p1, p2))
    print("midpoint(p1, p2):", midpoint(p1, p2))
    # Demonstrate immutability without illegal item assignment
    new_p1 = (10.0,) + p1[1:]
    print("Tuples are immutable; created new tuple instead of assigning:", new_p1)


def words_menu():
    print("\n-- Unique Word Counter --")
    print("Enter/paste your text (at least 3 sentences).")
    print("Finish with an empty line, or press Enter immediately to use the sample text.")
    lines: List[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    if lines:
        text = "\n".join(lines)
    else:
        # Default sample: 3 sentences
        text = (
            "Python is a programming language. "
            "Python is easy to learn. "
            "Python is powerful."
        )

    top_in = input("How many top words to show? (default 5): ").strip()
    try:
        top_n = int(top_in) if top_in else 5
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number, using default 5.")
        top_n = 5

    stats = analyze_text(text, top_n=top_n)

    # ---- Display all results ----
    words_list = tokenize(text)
    print("\n=== Results ===")
    print(f"Total words: {stats['total_words']}")
    print(f"Unique words: {stats['unique_count']}")
    print("\nWords (in order):")
    print(", ".join(words_list))
    print("\nUnique word set (sorted):")
    print(", ".join(sorted(stats["unique_words"])))
    print("\nFrequencies (all words):")
    # Show all frequencies sorted by count desc, then word asc
    for w, c in sorted(stats["counts"].items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{w}: {c}")
    print("\nMost common:")
    for w, c in stats["most_common"]:
        print(f"{w}: {c}")


def menu():
    while True:
        print("\n== Tuples & Sets ==")
        print("1) Distance and midpoint (Task 2.1)")
        print("2) Unique word counter (Task 2.2)")
        print("0) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            points_menu()
        elif choice == "2":
            words_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
