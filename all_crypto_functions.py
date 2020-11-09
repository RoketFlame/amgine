Caesar_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
Caesar_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Caesar_RU.insert(6, 'ё')  # создание списков для шифра цезвря и добавление буквы ё в русский словарь

DICT_MORSE_CODE_ENG = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                       'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                       'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                       's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '--..-',
                       'y': '-.--', 'z': '--..', ' ': '|'}

DICT_MORSE_CODE_RU = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
                      'ж': '...-',
                      'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--',
                      'н': '-.',
                      'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
                      'ф': '..-.',
                      'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '.--.-.',
                      'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '|'}

DICT_MORSE_DECODE_ENG = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
                         '--.': 'g',
                         '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm',
                         '-.': 'n',
                         '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                         '..-': 'u',
                         '...-': 'v', '.--': 'w', '--..-': 'x', '-.--': 'y', '--..': 'z', '|': ' '}

DICT_MORSE_DECODE_RU = {'.-': 'а', '-...': 'б', '.--': 'в', '--.': 'г', '-..': 'д', '.': 'е',
                        '...-': 'ж',
                        '--..': 'з', '..': 'и', '.---': 'й', '-.-': 'к', '.-..': 'л', '--': 'м',
                        '-.': 'н',
                        '---': 'о', '.--.': 'п', '.-.': 'р', '...': 'с', '-': 'т', '..-': 'у',
                        '..-.': 'ф',
                        '....': 'х', '-.-.': 'ц', '---.': 'ч', '----': 'ш', '--.-': 'щ',
                        '.--.-.': 'ъ',
                        '-.--': 'ы', '-..-': 'ь', '..-..': 'э', '..--': 'ю', '.-.-': 'я', '|': ' '}

Vigenere_code_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Vigenere_code_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
Vigenere_code_RU.insert(6, 'ё')


class SomethingWrong(Exception):  # базовое исключение
    pass


class WrongLanguage(SomethingWrong):  # исключение неверно выбранного языка
    pass


class WrongChar(SomethingWrong):  # исключение некорректоного символа
    pass


def caesar_code(text, lang='RU', cap=True, shift=0):
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
    if lang == 'RU':
        diction = DICT_MORSE_CODE_RU
    elif lang == 'ENG':
        diction = DICT_MORSE_CODE_ENG
    out = []
    code_text = ' '.join(text.split())
    for i in code_text:
        if i.upper() in diction or i.lower() in diction:
            out.append(diction[i.lower()])  # если есть значение в словаре - добавляем уже изменненое
        elif i == '\n':
            out.append('\n')
    return ' '.join(out)  # join применяется к пробелу,
    # чтобы при декодировании можно было легко отделить буквы в слове


def morse_decode(code, lang='RU'):
    if lang == 'RU':
        diction = DICT_MORSE_DECODE_RU
    elif lang == 'ENG':
        diction = DICT_MORSE_DECODE_ENG
    out = []
    text = code.split()
    for i in text:
        if i in diction:
            out.append(diction[i])
        elif i == '\n':
            out.append('\n')
    str_out1 = ''.join(out)
    str_out = str_out1.replace('|', ' ')
    return ' '.join(str_out.split())


def vigenere_code(key, text):
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


def vigenere_decode(key, text):
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