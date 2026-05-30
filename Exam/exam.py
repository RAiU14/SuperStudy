import os
import random
import sys

# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Select the File
def reading_quiz():
    file_path = r"Exam\\Quiz_Files"
    files = [item for item in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, item))]

    if not files:
        print("No files found.")
        return None

    print("Available files:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

    choice = int(input("Select a file number: "))

    if choice < 1 or choice > len(files):
        print("Invalid choice.")
        return None

    return files[choice - 1]


# Reading the quiz file
def quiz_read(file_name):
    with open(f"Exam\\Quiz_Files\\{file_name}", "r", encoding="utf-8") as f:
        data = f.readlines()

    quiz = []
    current_question = None

    for line in data:
        line = line.strip()

        if line == "":
            continue

        # Detect question
        if line.startswith("Q."):
            if current_question is not None:
                quiz.append(current_question)

            current_question = {
                "question": line,
                "options": [],
                "answer": 0,
                "points": 1
            }

        # Detect options: 
        elif (
            current_question is not None
            and len(line) > 2
            and line[0] in ["1", "2", "3", "4"]
            and line[1] == "."
        ):
            current_question["options"].append(line)

        # Detect answer: 
        elif current_question is not None and line.lower().startswith("answer:"):
            current_question["answer"] = int(line.split(":")[1].strip())

        # Detect points: 
        elif current_question is not None and line.lower().startswith("points:"):
            current_question["points"] = int(line.split(":")[1].strip())

    if current_question is not None:
        quiz.append(current_question)

    return quiz


# Add score
def score_add(current_points: int, points: int):
    return current_points + points


# Get user answer
def get_user_answer(current_points, total_points):
    while True:
        user_input = input("Enter your answer 1-4, or q to quit: ").strip()

        if user_input.lower() == "q":
            print("\nQuiz ended early.")
            print("Current Score:", str(current_points) + "/" + str(total_points))
            sys.exit()

        if not user_input.isdigit():
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        answer = int(user_input)

        if answer < 1 or answer > 4:
            print("Wrong number. Please enter only 1, 2, 3, or 4.")
            continue

        return answer

# Display one question
def display_question(question_data, current_points, question_number, total_questions, total_points):
    clear_terminal()

    print("Quiz")
    print("Progress:", str(question_number) + "/" + str(total_questions))
    print("Current Score:", current_points)

    print(question_data["question"])

    for option in question_data["options"]:
        print(option)

    if get_user_answer(current_points, total_points) == question_data["answer"]:
        print("Correct!")
        current_points = score_add(current_points, question_data["points"])

    else:
        print("Wrong!")
        print("Correct answer:", question_data["answer"])
        input("Press Enter to continue\n")

    return current_points

# Final score report
def display_report(current_points, total_points):
    clear_terminal()

    print("Quiz completed!")
    print("Final Score:", str(current_points) + "/" + str(total_points))



# Main program
def main():
    current_points = 0
    quiz = quiz_read(reading_quiz())

    if len(quiz) == 0:
        print("No questions found in quiz file.")
        return

    random.shuffle(quiz)
    
    total_points = 0

    for item in quiz:
        total_points += item["points"]

    total_questions = len(quiz)

    for index, question_data in enumerate(quiz):
        current_points = display_question(
            question_data,
            current_points,
            index + 1,
            total_questions,
            total_points
        )

    display_report(current_points, total_points)


if __name__ == "__main__":
    main()