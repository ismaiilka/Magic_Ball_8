import random, time, os

clear = lambda: os.system('cls')
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

def start_message():
    clear()
    time.sleep(3)
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    time.sleep(3)
    clear()
    name = input('Как тебя зовут?\n')
    time.sleep(2)
    clear()
    input('Привет, {name}. Какой вопрос тебя интересует?\n'.format(name=name))
    time.sleep(3)
    clear()
    print(random.choice(answers))
    time.sleep(3)

def main():
    while True:
        clear()
        response = input('Хочешь задать еще один вопрос?\n')
        time.sleep(2)
        clear()
        if response.lower() == 'да':
            input('Спроси меня.\n')
            time.sleep(2)
            clear()
            print(random.choice(answers))
            time.sleep(3)
            clear()
            continue
        elif response.lower() == 'нет':
            print('Возвращайся если возникнут вопросы!')
            break
        else:
            print('Некорректный ответ.')
            time.sleep(2)
            clear()
            continue

