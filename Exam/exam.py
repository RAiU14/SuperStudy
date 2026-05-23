import os


# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Reading the quiz file
def quiz_read():
    with open("quiz1.txt", "r", encoding="utf-8") as f:
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

        # Detect options: 1. option text
        elif (
            current_question is not None
            and len(line) > 2
            and line[0] in ["1", "2", "3", "4"]
            and line[1] == "."
        ):
            current_question["options"].append(line)

        # Detect answer: Answer: 2
        elif current_question is not None and line.lower().startswith("answer:"):
            current_question["answer"] = int(line.split(":", 1)[1].strip())

        # Detect points: 
        elif current_question is not None and line.lower().startswith("points:"):
            current_question["points"] = int(line.split(":", 1)[1].strip())

    if current_question is not None:
        quiz.append(current_question)

    return quiz


# Add score
def score_add(current_points: int, points: int):
    return current_points + points


# Get user answer
def get_user_answer():
    while True:
        user_input = input("Enter your answer 1-4: ").strip()

        if not user_input.isdigit():
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        answer = int(user_input)

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

    print(question_data["question"])

    for option in question_data["options"]:
        print(option)


    user_answer = get_user_answer()

    if user_answer == question_data["answer"]:
        print("Correct!")
        current_points = score_add(current_points, question_data["points"])
    else:
        print("Wrong!")
        # Hiding it so that people can learn at a different time. Debating this situation
        # print("Correct answer:", question_data["answer"])

    return current_points


# Final score report
def display_report(current_points, total_points):
    clear_terminal()

    print("Quiz completed!")
    print("Final Score:", str(current_points) + "/" + str(total_points))

    percentage = (current_points / total_points) * 100

    print("Percentage:", str(round(percentage, 2)) + "%")

    if percentage >= 80:
        print("Result: Excellent")
    elif percentage >= 60:
        print("Result: Good")
    elif percentage >= 40:
        print("Result: Average")
    else:
        print("Better luck next time!")


# Main program
def main():
    current_points = 0

    quiz = quiz_read()

    if len(quiz) == 0:
        print("No questions found in quiz file.")
        return

    total_points = 0

    for item in quiz:
        total_points += item["points"]

    total_questions = len(quiz)

    for index, question_data in enumerate(quiz):
        current_points = display_question(
            question_data,
            current_points,
            index + 1,
            total_questions
        )

    display_report(current_points, total_points)


if __name__ == "__main__":
    main()