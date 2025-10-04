import json
import random
import os

QUESTIONS_FILE = r"C:\Users\JAYA\Desktop\colleg project\questions.json"
ASKED_FILE = "asked.json"

with open(QUESTIONS_FILE, "r") as f:
    questions = json.load(f)
if os.path.exists(ASKED_FILE):
    with open(ASKED_FILE, "r") as f:
        asked_indices = json.load(f)
else:
    asked_indices = []

if len(asked_indices) >= len(questions):
    asked_indices = []

remaining_questions = [q for i, q in enumerate(questions) if i not in asked_indices]

random.shuffle(remaining_questions)

score = 0
for i, q in enumerate(remaining_questions, 1):
    print(f"Q{i}: {q['question']}")
    for idx, choice in enumerate(q['choices'], 1):
        print(f"  {idx}. {choice}")
    while True:
        answer = input("Enter your choice (1-4): ")
        if answer.isdigit() and 1 <= int(answer) <= len(q['choices']):
            break
        print("Invalid input, please enter a number between 1 and 4.")
    if q['choices'][int(answer) - 1] == q['correct_answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['correct_answer']}\n")

print(f"Quiz Complete! Your score: {score}/{len(questions)}")
