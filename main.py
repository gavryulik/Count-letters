from translate import Translator

# TODO: RUSSIAN VOWELS
glas_letter_russian = list(
    map(str.lower, ["А", "У", "О", "И", "Э", "Ы", "Я", "Ю", "Е", "Ё"]))

# TODO: RUSSIAN CONSONANTS
soglas_letter_russian = list(
    map(str.lower, [
        "Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С",
        "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Ь", "Ъ", "Щ"
    ]))

# TODO: ENGLISH VOWELS
glas_letter_usa = list(map(str.lower, ["A", "E", "I", "O", "U", "Y"]))

# TODO: ENGLISH CONSONANTS
soglas_letter_usa = list(
    map(str.lower, [
        "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R",
        "S", "T", "V", "W", "X", "Y", "Z"
    ]))

# TODO: UKRAINIAN VOWELS
glas_letter_ukr = list(
    map(str.lower, ["А", "О", "У", "И", "Е", "Є", "І", "Ї", "Ю", "Я"]))

# TODO: UKRAINIAN CONSONANTS
soglas_letter_ukr = list(
    map(str.lower, [
        "Б", "В", "Г", "Ґ", "Д", "З", "ДЗ", "Ж", "ДЖ", "К", "Л", "М", "Н", "П",
        "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Л'", "М'", "Н'",
        "Р", "Й"
    ]))

def count_letters(input_text, glas_letters, soglas_letters):
    count_glas = sum(1 for letter in input_text if letter in glas_letters)
    count_soglas = sum(1 for letter in input_text if letter in soglas_letters)
    return count_glas, count_soglas

def translate_text(text, target_lang):
    try:
        translator = Translator(to_lang=target_lang)
        return translator.translate(text)
    except:
        return text

def letter():
    while True:
        language_input = input(
            "Enter the language you want to enter the sentence in: Russian/Ukrainian/English: ").lower()
        
        if language_input not in ["russian", "ukrainian", "english"]:
            print(translate_text("Please enter correctly!", "en"))
            continue
        
        if language_input == "russian":
            language_code = "ru"
            glas_letters = glas_letter_russian
            soglas_letters = soglas_letter_russian
        elif language_input == "ukrainian":
            language_code = "uk"
            glas_letters = glas_letter_ukr
            soglas_letters = soglas_letter_ukr
        else:
            language_code = "en"
            glas_letters = glas_letter_usa
            soglas_letters = soglas_letter_usa

        quantity_letters = int(input(translate_text("Please enter the number of sentences you want to enter: ", language_code)))

        count_glas_letter = 0
        count_soglas_letter = 0

        for quantity in range(1, quantity_letters + 1):
            if language_input == "russian":
                print(f"Предложение # {quantity}")
                while True:
                    letter_input = input("Введите предложение: ").lower()

                    if language_input == "russian":
                        valid_letters = glas_letter_russian + soglas_letter_russian
                    elif language_input == "english":
                        valid_letters = glas_letter_usa + soglas_letter_usa
                    else:
                        valid_letters = glas_letter_ukr + soglas_letter_ukr

                    if not all(letter in valid_letters and letter.isalpha()or letter.isspace() or letter in ",.!?-–"for letter in letter_input):
                        print("Пожалуйста, введите правильно!")
                        continue
                    else:
                        break
            
            elif language_input == "ukrainian":
                print(f"Речення # {quantity}")
                while True:
                    letter_input = input("Введіть речення: ").lower()

                    if language_input == "russian":
                        valid_letters = glas_letter_russian + soglas_letter_russian
                    elif language_input == "english":
                        valid_letters = glas_letter_usa + soglas_letter_usa
                    else:
                        language_input == "ukrainian"
                        valid_letters = glas_letter_ukr + soglas_letter_ukr

                    if not all(letter in valid_letters and letter.isalpha() or letter.isspace() or letter in ",.!?-–" for letter in letter_input):
                        print("Будь ласка, введіть правильно!")
                        continue
                    else:
                        break
            else:
                print(f"Sentence # {quantity}")
                while True:
                    letter_input = input("Enter the sentence: ").lower()

                    if language_input == "russian":
                        valid_letters = glas_letter_russian + soglas_letter_russian
                    elif language_input == "english":
                        valid_letters = glas_letter_usa + soglas_letter_usa
                    else:
                        language_input == "ukrainian"
                        valid_letters = glas_letter_ukr + soglas_letter_ukr

                    if not all(letter in valid_letters and letter.isalpha() or letter.isspace() or letter in ",.!?-–" for letter in letter_input):
                        print("Please enter correctly!")
                        continue
                    else:
                        break

            count_glas, count_soglas = count_letters(letter_input, glas_letters, soglas_letters)
            if language_code == "uk":
                print(f"Голосних: {count_glas}, Приголосних: {count_soglas}")
                count_glas_letter += count_glas
                count_soglas_letter += count_soglas
            elif language_code == "en":
                print(f"Vowels: {count_glas}, Consonants: {count_soglas}")
                count_glas_letter += count_glas
                count_soglas_letter += count_soglas
            else:
                print(f"Гласных: {count_glas}, Согласных: {count_soglas}")
                count_glas_letter += count_glas
                count_soglas_letter += count_soglas

        if language_code == "uk":
            print(f"Всього голосних {count_glas_letter}, та приголосних {count_soglas_letter}")
        elif language_code == "en":
            print(f"Total vowels {count_glas_letter}, and consonants {count_soglas_letter}")
        else:
            print(f"Всего гласных {count_glas_letter}, и согласных {count_soglas_letter}")
            
        povtor_input = input(translate_text("Would you like to enter more words?: ",language_code)).lower()

        if povtor_input != "yes" and povtor_input != "так" and povtor_input != "да":
            print(translate_text("The program is complete", language_code))
            break

letter()