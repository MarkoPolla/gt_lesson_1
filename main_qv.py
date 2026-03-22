import time

questions = {
    "Сколько планет в Солнечной системе?": "8",
    "Столица Франции?": "Париж"
}

score = 0

for q, a in questions.items():
    start_time = time.time()
    user_answer = input(q + " ")
    end_time = time.time()

    # Вычисляем затраченное время
    elapsed_time = round(end_time - start_time, 1)
    print(f"Время ответа: {elapsed_time} сек.")

    # Проверка таймера
    if elapsed_time > 5:
        print('Вы не уложились в таймер 5 секунд')
        user_answer = 'wrong'  # Принудительно делаем ответ неправильным

    # Проверка ответа
    if user_answer.lower().strip() == a.lower():
        print("Правильно!")
        score += 1
    else:
        print("Неверно!")

# Итоговый результат выводится после завершения всех вопросов
print(f"Ваш результат: {score} из {len(questions)}")