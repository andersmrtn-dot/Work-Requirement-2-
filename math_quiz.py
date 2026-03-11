"""
math_quiz.py - Math Quiz with Exception Handling
Generates random addition questions, validates user input,
and tracks score across multiple rounds.
"""

import random


# ── Configuration ─────────────────────────────────────────
NUM_RANGE   = (1, 50)   # Range for random integers
TOTAL_ROUNDS = 5        # Questions per quiz session


# ── Helpers ───────────────────────────────────────────────

def print_banner():
    print("\n" + "=" * 45)
    print("   🧮  MATH QUIZ — ADDITION CHALLENGE")
    print("=" * 45)
    print(f"  Answer {TOTAL_ROUNDS} questions. Type the sum.")
    print(f"  Numbers are between {NUM_RANGE[0]} and {NUM_RANGE[1]}.")
    print("=" * 45 + "\n")


def print_result_bar(score: int, total: int):
    """Print a visual score bar at the end of the quiz."""
    percentage = (score / total) * 100
    filled     = int(percentage / 10)
    bar        = "█" * filled + "░" * (10 - filled)

    print("\n" + "=" * 45)
    print("   📊  QUIZ COMPLETE")
    print("=" * 45)
    print(f"  Score   : {score} / {total}  ({percentage:.0f}%)")
    print(f"  Progress: [{bar}]")

    if percentage == 100:
        print("  🏆  Perfect score! Outstanding!")
    elif percentage >= 80:
        print("  🌟  Great job! Almost perfect!")
    elif percentage >= 60:
        print("  👍  Good effort! Keep practising.")
    elif percentage >= 40:
        print("  📚  Keep going — practice makes perfect!")
    else:
        print("  💪  Don't give up — try again!")

    print("=" * 45 + "\n")


def ask_question(round_num: int) -> bool:
    """
    Generate one addition question and return True if answered correctly.
    Handles invalid (non-integer) input with try/except.
    """
    a = random.randint(*NUM_RANGE)
    b = random.randint(*NUM_RANGE)
    correct_answer = a + b

    print(f"  ─── Question {round_num} of {TOTAL_ROUNDS} ───────────────")
    print(f"  ❓  What is  {a}  +  {b}  ?")

    while True:                          # keep asking until valid input
        try:
            user_input = input("  ➤  Your answer: ").strip()
            answer = int(user_input)     # may raise ValueError
        except (ValueError, EOFError):
            print("  ⚠️   Invalid input! Please enter a whole number.\n"
                  f"  ➤  Try again — What is {a} + {b} ?")
            continue                     # re-prompt on bad input

        # Valid integer received — evaluate correctness
        if answer == correct_answer:
            print(f"  ✅  Correct! {a} + {b} = {correct_answer}\n")
            return True
        else:
            print(f"  ❌  Wrong! The correct answer was {correct_answer}.\n")
            return False


def play_quiz():
    """Run a full quiz session and display the final score."""
    print_banner()
    score = 0

    for round_num in range(1, TOTAL_ROUNDS + 1):
        if ask_question(round_num):
            score += 1

    print_result_bar(score, TOTAL_ROUNDS)
    return score


def main():
    while True:
        play_quiz()
        try:
            again = input("  🔄  Play again? (yes / no): ").strip().lower()
        except EOFError:
            again = "no"
        if again not in ("yes", "y"):
            print("\n  👋  Thanks for playing! Goodbye!\n")
            break
        print()


if __name__ == "__main__":
    main()
