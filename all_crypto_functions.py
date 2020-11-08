# создание списков для шифра цезвря и добавление буквы ё в русский словарь
ALPHABET_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ALPHABET_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALPHABET_RU.insert(6, 'ё')
# создание словарей для азбуки морзе
MORSE_dict_ENG = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                  'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                  'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                  's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '--..-',
                  'y': '-.--', 'z': '--..', ' ': ' '}
MORSE_dict_RU = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-',
                 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.',
                 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.',
                 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '.--.-.',
                 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-'}


# обработка исключений
class SomethingWrong(Exception):  # базовое исключение
    pass


class WrongLanguage(SomethingWrong):  # исключение неверно выбранного языка
    pass


class WrongChar(SomethingWrong):  # исключение некорректоного символа
    pass


def caesar_cipher(text, shift=0, lang='RU', cap=True):
    out = []
    if lang == 'RU':  # выбираем нужный список для шифрования
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    if cap:  # проверка на сохранение регистра текста
        for char in text:
            if char == char.upper():  # определение больших букв
                char = char.lower()
                if char in main_list:
                    res = main_list[(main_list.index(char) + shift) % 33].capitalize()
                    # если буква относится к алфавиту, то применяем к ней шифр
                else:
                    res = char  # иначе симл остается прежним
            else:  # все тоже самое и для маленьких букв
                if char in main_list:
                    res = main_list[(main_list.index(char) + shift) % 33]
                else:
                    res = char
            out.append(res)  # добавляем в список полученный результат

    else:  # если регистр текста не важен
        text = text.lower()  # приведение текста к нижнему регистру
        for char in text:
            if char in main_list:  # все тот же алгоритм
                res = main_list[(main_list.index(char) + shift) % 33]
            else:
                res = char
            out.append(res)  # добавляем в список полученный результат

    return ''.join(out)  # функция возвращает уже строку


def morse_code_encrypt(text, lang='RU'):
    if lang == 'RU':  # Выбираем нужный словарь для шифрования
        main_dict = MORSE_dict_RU
    elif lang == 'ENG':
        main_dict = MORSE_dict_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    out = []
    for i in text:
        if i in main_dict:
            out.append(main_dict[i])  # если есть значение в словаре - добавляем уже изменненое
        else:
            raise WrongChar('В тексте есть символы из другого языка')
    return ' '.join(out)  # join применяется к пробелу,
    # чтобы при декодировании можно было легко отделить буквы в слове


def vigenere_code_encrypt(key, text, lang='RU'):
    # избавление текста и ключа от "лишних" знаков
    key = ''.join(map(lambda x: x.lower() if x.isalpha() or x == ' ' else '', key))
    text = ''.join(map(lambda x: x.lower() if x.isalpha() or x == ' ' else '', text))

    out = []  # список, который будет возвращаться
    space = 0  # счетчик пробелов, чтобы индексы ключа правильно считались

    if lang == 'RU':  # выбираем нужный список для шифрования
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    # проверка на наличие всех символов в списке
    if all([True if x in main_list and y in main_list else False for x, y in zip(text, key)]):
        raise WrongChar('В тексте или в ключе есть символ другого языка')

    for index, ch in enumerate(text):
        if ch != ' ':  # обработка пробелов
            mj = main_list.index(ch)  # индекс буквы слова
            kj = main_list.index(key[(index - space) % len(key)])
            # индекс ключа с учетом пробелов
            cj = (mj + kj) % len(main_list)  # индекс уже зашифрованной буквы
            out.append(main_list[cj])  # добавление зашифрованной буквы в список
        else:
            space += 1  # увеличение счетчика пробелов
            out.append(' ')
    return ''.join(out)


def vigenere_code_decrypt(key, text, lang='RU'):
    # избавление текста и ключа от "лишних" знаков
    key = ''.join(map(lambda x: x if x.isalpha() or x == ' ' else '', key))
    text = ''.join(map(lambda x: x if x.isalpha() or x == ' ' else '', text))

    out = []  # список, который будет возвращаться
    space = 0  # счетчик пробелов, чтобы индексы ключа правильно считались

    if lang == 'RU':  # выбираем нужный список для шифрования
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    # проверка на наличие всех символов в списке
    if all([True if x in main_list and y in main_list else False for x, y in zip(text, key)]):
        raise WrongChar('В тексте или в ключе есть символ другого языка')

    for index, ch in enumerate(text):  # используем enumerate, чтобы сохранить индексы букв
        if ch != ' ':  # обработка пробелов
            cj = main_list.index(ch)  # индекс буквы слова
            kj = main_list.index(key[(index - space) % len(key)])
            # индекс ключа с учетом пробелов
            mj = (cj - kj) % len(main_list)  # индекс уже расшифрованной буквы
            out.append(main_list[mj])  # добавление расшифрованной буквы в список
        else:
            space += 1  # увеличение счетчика пробелов
            out.append(' ')
    return ''.join(out)
