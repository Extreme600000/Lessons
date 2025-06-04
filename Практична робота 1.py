def check_answer(user_answer, correct_answer):
        """Перевіряє, чи відповідь користувача правильна.
        :param user_answer:
        :param correct_answer:
        :return:
        """
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False


def run_quiz():
        """Запускає вікторину."""
        questions = [
            {"question": "Яка (справжня) грошова одиниця є українською"
                    "А.Гривня"
                   "Б.Шаг"
                   "В.Рубль", "answer": "Б"},
            {"question": "Скільки способів втечі є в Granny Legacy?"
                  "А.2"
                  "Б.3"
                  "В.4", "answer": "В"},
            {"question": "Скільки способів втечі є в Granny Unnofical remake 1.9?"
                  "А.5"
                  "Б.3"
                  "В.4", "answer": "А"},
            {"question": "Скільки мішочків потрібно зібрати в Eyes the horror game (складність Extreme)?"
                  "А.15"
                  "Б.30"
                  "В.20", "answer": "Б"},
            {"question": "Яка команда головна в серіалі Beyblade X?"
                  "А.Команда Персона"
                  "Б.Команда Пендрагон"
                  "В.Команда Ігдрасіль", "answer": "А"},
            {"question": "Яка мета була в команди Персона?"
                  "А.Перемогти команду Ігдрасіль"
                  "Б.Дізнатися про команду Зуганік"
                  "В.Зійти на вершину X вежі", "answer": "В"},
            {"question": "Хто є головним героєм серіалу Клинок разсекающий демонов?"
                  "А.Ки Хун"
                  "Б.Танджиро"
                  "В.Недзуко", "answer": "Б"},
            {"question": "Хто є самим головним ворогом всього серіалу Клинок разсекающий демонов?"
                  "А.Гютаро"
                  "Б.Дакі"
                  "В.Мудзан", "answer": "В"},
            {"question": "Скільки буде x**2-4x-5=0?"
                  "А.x1=2,x2=0"
                  "Б.x1=-1,x2=2.3"
                  "В.x1=3.5,x2=-0.5", "answer": "В"},
            {"question": "Куди будуть напрямлені вітки при y=-3x**2-7*x-3=0?"
                   "А.Вгору"
                   "Б.Вниз"
                   "В.Неможливо визначити", "answer": "Б"},
            {"question":"Скільки рівнів складності існує в Granny Legacy?"
                   "А.3"
                   "Б.4"
                   "В.5", "answer": "В"},
            {"question":"Скільки коштує Impossible в Granny Legacy?"
                   "А.10"
                   "Б.3"
                   "В.0", "answer": "А"},
            {"question": "Скільки пісень в Hit Single(мод FNF(Real))?"
                   "А.20"
                   "Б.10"
                   "В.5", "answer": "Б"},
            {"question":"Як називаєтся гра в якій потрібно охороняти вежу від ворогів?"
                   "А.Tower Deffence"
                   "Б.Minecraft"
                   "В.Roblox", "answer": "А"},
            {"question": "Як називається плейс (в Roblox) в якому потрібно тікати від води,кислоти,кип'ятка,лави?"
                   "А.Dead Rails"
                   "Б.Doors"
                   "В.Flood Escape", "answer": "В"},
            {"question": "Скільки дверей в Rooms?"
                   "А.250"
                   "Б.500"
                   "В.1000", "answer": "В"},
        ]
        score = 0
        for question_data in questions:
            print(question_data["question"])
            user_answer = input("Ваша відповідь: ")
            if check_answer(user_answer, question_data["answer"]):
                print("Правильно!")
                score += 1
            else:
                print(f"Неправильно. Правильна відповідь - {question_data['answer']}.")

        print(f"Ви правильно відповіли на: {score}/16")
run_quiz()
print("Ви великі молодці що старилися відповісти на ці запитання. "
      "Дякую усім за увагу! Усім до скорої зустрічі!")
