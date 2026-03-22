questions = {
    "Сколько планет в Солнечной системе?": "8",
    "Столица Франции?": "Париж"
}

score = 0

for q, a in questions.items():
    user_answer = input(q + " ")
    # .strip() убирает случайные пробелы в начале или конце ответа
    if user_answer.lower().strip() == a.lower():
        print("Правильно!")
        score += 1
    else:
        print("Неверно!")

print(f"Ваш результат: {score} из {len(questions)}")