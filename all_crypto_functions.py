Caesar_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
Caesar_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Caesar_RU.insert(6, 'ё')
# создание списков для шифра цезвря и добавление буквы ё в русский словарь
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


# создание словарей для азбуки морзе
# обработка исключений
class SomethingWrong(Exception):  # базовое исключение
    pass


class WrongLanguage(SomethingWrong):  # исключение неверно выбранного языка
    pass


class WrongChar(SomethingWrong):  # исключение некорректоного символа
    pass


def caesar_cipher(text, lang='RU', cap=True, shift=0):
    out = []
    if lang == 'RU':  # выбираем нужный список для шифрования
        main_list = Caesar_RU
    elif lang == 'ENG':
        main_list = Caesar_ENG
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


def morse_code(text, lang='RU'):
    if lang == 'RU':  # Выбираем нужный словарь для шифрования
        main_dict = MORSE_dict_RU
    elif lang == 'ENG':
        main_dict = MORSE_dict_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    out = []
    for i in text:
        if i in dict:
            out.append(main_dict[i])  # если есть значение в словаре - добавляем уже изменненое
        else:
            raise WrongChar('В тексте есть символы из другого языка')
    return ' '.join(out)  # join применяется к пробелу,
    # чтобы при декодировании можно было легко отделить буквы в слове


Vigenere_code_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Vigenere_code_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
Vigenere_code_RU.insert(6, 'ё')


def encrypt(key, text):
    key = ''.join(map(lambda x: x if x.isalpha() or x == ' ' else '', key))
    text = ''.join(map(lambda x: x if x.isalpha() or x == ' ' else '', text))
    out = []
    if lang == 'RU':  # выбираем нужный список для шифрования
        main_list = Caesar_RU
    elif lang == 'ENG':
        main_list = Caesar_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    space = 0
    for index, ch in enumerate(text):
        if ch.isalpha():
            mj = main_list.index(ch)
            kj = main_list.index(key[(index - space) % len(key)])
            cj = (mj + kj) % len(tabula_recta)
            out.append(tabula_recta[cj])
        else:
            space += 1
            out.append(' ')
    return ''.join(out)


def decrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = tabula_recta.index(ch)
            kj = tabula_recta.index(key[(index - space) % len(key)])
            mj = (cj - kj) % len(tabula_recta)
            result.append(tabula_recta[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)

print(encrypt('lemo', 'attackatdawn attackatdawn'))
print(123)