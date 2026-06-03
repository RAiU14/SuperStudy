import os
import random
import json
from datetime import datetime


QUIZ_FOLDER = os.path.join("Exam", "Quiz_Files")
METADATA_FOLDER = os.path.join("Exam", "Metadata")


# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Get User Data
def get_user_data():
    os.makedirs(METADATA_FOLDER, exist_ok=True)

    while True:
        name = input("Enter your name to begin: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in name):
            print("Name can only contain letters and spaces. Numbers are not allowed.")
            continue

        final_name = ""

        for char in name.lower().replace(" ", "_"):
            if char.isalpha() or char == "_":
                final_name += char

        metadata_file = os.path.join(METADATA_FOLDER, final_name.strip("_") + ".json")

        if os.path.exists(metadata_file):
            with open(metadata_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            attempt_number = len(metadata["attempts"]) + 1

            print("Welcome back,", name)
            print("This is your attempt number:", attempt_number)

        else:
            metadata = {
                "username": name,
                "attempts": []
            }

            attempt_number = 1

            with open(metadata_file, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)

            print("New user created:", name)
            print("This is your attempt number:", attempt_number)

        input("Press Enter to continue...")

        return attempt_number, metadata_file
    

# Save attempt metadata
def save_attempt_metadata(
    metadata_file,
    attempt_number,
    quiz_file,
    current_points,
    total_points,
    answered_questions,
    total_questions,
    completed
):
    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    attempt_data = {
        "attempt_number": attempt_number,
        "quiz_file": quiz_file,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": current_points,
        "total_points": total_points,
        "answered_questions": answered_questions,
        "total_questions": total_questions,
        "completed": completed
    }

    metadata["attempts"].append(attempt_data)

    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)


# Select the quiz file
def reading_quiz():
    if not os.path.exists(QUIZ_FOLDER):
        print("Quiz folder not found:", QUIZ_FOLDER)
        return None

    files = sorted([
    item for item in os.listdir(QUIZ_FOLDER)
    if os.path.isfile(os.path.join(QUIZ_FOLDER, item))])

    if not files:
        print("No files found.")
        return None

    print("Available files:")

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    while True:
        user_input = input("Select a file number: ").strip()

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(user_input)

        if choice < 1 or choice > len(files):
            print("Invalid choice.")
            continue

        return files[choice - 1]


# Read the quiz file
def quiz_read(file_name):
    with open(os.path.join(QUIZ_FOLDER, file_name), "r", encoding="utf-8") as f:
        data = f.readlines()

    quiz = []
    current_question = None

    for line in data:
        line = line.strip()

        if line == "":
            continue

        if line.startswith("Q."):
            if current_question is not None:
                quiz.append(current_question)

            current_question = {
                "question": line,
                "options": [],
                "answer": 0,
                "points": 1
            }

        elif (
            current_question is not None
            and len(line) > 2
            and line[0] in ["1", "2", "3", "4"]
            and line[1] == "."
        ):
            current_question["options"].append(line)

        elif current_question is not None and line.lower().startswith("answer:"):
            current_question["answer"] = int(line.split(":")[1].strip())

        elif current_question is not None and line.lower().startswith("points:"):
            current_question["points"] = int(line.split(":")[1].strip())

    if current_question is not None:
        quiz.append(current_question)

    return quiz


# Add score
def score_add(current_points: int, points: int):
    return current_points + points


# Get user answer
def get_user_answer():
    while True:
        user_input = input("Enter your answer 1-4, or q to quit: ").strip()

        if user_input.lower() == "q":
            return None

        try:
            answer = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if answer < 1 or answer > 4:
            print("Wrong number. Please enter only 1, 2, 3, or 4.")
            continue

        return answer


# Display one question
def display_question(question_data, current_points, question_number, total_questions):
    clear_terminal()

    print("Quiz")
    print("Progress:", str(question_number) + "/" + str(total_questions))
    print("Current Score:", current_points)
    print()

    print(question_data["question"])
    print()

    for option in question_data["options"]:
        print(option)

    print()

    user_answer = get_user_answer()

    if user_answer is None:
        return current_points, True

    if user_answer == question_data["answer"]:
        print("Correct!")
        current_points = score_add(current_points, question_data["points"])
    else:
        print("Wrong!")
        print("Correct answer:", question_data["answer"])

    input("Press Enter to continue...")

    return current_points, False


# Final score report
def display_report(current_points, total_points):
    clear_terminal()

    print("Quiz completed!")
    print("Final Score:", str(current_points) + "/" + str(total_points))

    if total_points > 0:
        print("Percentage:", str(round((current_points / total_points) * 100, 2)) + "%")


# Early quit report
def display_quit_report(current_points, total_points):
    clear_terminal()

    print("Quiz ended early.")
    print("Current Score:", str(current_points) + "/" + str(total_points))

    if total_points > 0:
        print("Current Percentage:", str(round((current_points / total_points) * 100, 2)) + "%")


# Main program
def main():
    current_points = 0
    answered_questions = 0
    completed = True

    attempt_number, metadata_file = get_user_data()

    clear_terminal()

    quiz_file = reading_quiz()

    if quiz_file is None:
        return

    quiz = quiz_read(quiz_file)

    if len(quiz) == 0:
        print("No questions found in quiz file.")
        return

    random.shuffle(quiz)

    total_points = 0

    for item in quiz:
        total_points += item["points"]

    total_questions = len(quiz)

    for index, question_data in enumerate(quiz):
        current_points, user_quit = display_question(
            question_data,
            current_points,
            index + 1,
            total_questions
        )

        if user_quit:
            completed = False
            break

        answered_questions += 1

    if completed:
        display_report(current_points, total_points)
    else:
        display_quit_report(current_points, total_points)

    save_attempt_metadata(
        metadata_file,
        attempt_number,
        quiz_file,
        current_points,
        total_points,
        answered_questions,
        total_questions,
        completed
    )

    print()
    print("Attempt saved successfully.")


if __name__ == "__main__":
    main()