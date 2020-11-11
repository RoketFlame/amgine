ALPHABET_RU = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ALPHABET_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALPHABET_RU.insert(6, 'ё')
# создание списков алфавита языков и добавление буквы ё в русский алфавит

DICT_MORSE_ENCODE_ENG = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                         'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                         'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '--..-',
                         'y': '-.--', 'z': '--..'}

DICT_MORSE_ENCODE_RU = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
                        'ж': '...-',
                        'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--',
                        'н': '-.',
                        'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
                        'ф': '..-.',
                        'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-',
                        'ъ': '.--.-.',
                        'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-'}

DICT_MORSE_DECODE_ENG = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
                         '--.': 'g',
                         '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm',
                         '-.': 'n',
                         '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                         '..-': 'u',
                         '...-': 'v', '.--': 'w', '--..-': 'x', '-.--': 'y', '--..': 'z'}

DICT_MORSE_DECODE_RU = {'.-': 'а', '-...': 'б', '.--': 'в', '--.': 'г', '-..': 'д', '.': 'е',
                        '...-': 'ж',
                        '--..': 'з', '..': 'и', '.---': 'й', '-.-': 'к', '.-..': 'л', '--': 'м',
                        '-.': 'н',
                        '---': 'о', '.--.': 'п', '.-.': 'р', '...': 'с', '-': 'т', '..-': 'у',
                        '..-.': 'ф',
                        '....': 'х', '-.-.': 'ц', '---.': 'ч', '----': 'ш', '--.-': 'щ',
                        '.--.-.': 'ъ',
                        '-.--': 'ы', '-..-': 'ь', '..-..': 'э', '..--': 'ю', '.-.-': 'я'}


class SomethingWrong(Exception):  # базовое исключение
    pass


class WrongLanguage(SomethingWrong):  # исключение неверно выбранного языка
    pass


class WrongChar(SomethingWrong):  # исключение некорректоного символа
    pass


def caesar_code(text, shift=0, lang='RU', cap=True):
    # выбираем нужный список для шифрования
    if lang == 'RU':
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    out = []
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
        out = list(
            map(lambda x: main_list[(main_list.index(x) + shift) % 33] if x in main_list else x,
                text))  # преобразовывание символов текста

    return ''.join(out)  # функция возвращает уже строку


def morse_encode(text, lang='RU'):
    # выбираем нужный словарь для шифрования
    if lang == 'RU':
        main_dict = DICT_MORSE_ENCODE_RU
    elif lang == 'ENG':
        main_dict = DICT_MORSE_ENCODE_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    out = []
    text = ' '.join(text.split())  # убираем лишние пробелы
    for char in text:
        if char.lower() in main_dict:
            out.append(
                main_dict[char.lower()])  # если есть значение в словаре - добавляем уже изменненое
        elif char == '\n':
            out.append('\n')
        elif char == ' ':
            out.append(' ')
    return ' '.join(out)  # join применяется к пробелу,
    # чтобы при декодировании можно было легко отделить буквы в слове


def morse_decode(text, lang='RU'):
    # выбираем нужный словарь для шифрования
    if lang == 'RU':
        main_dict = DICT_MORSE_DECODE_RU
    elif lang == 'ENG':
        main_dict = DICT_MORSE_DECODE_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    out = []
    text = [word.split() for word in text.split('   ')]  # разделение шифра на буквы
    for word in text:
        word_res = []
        for char in word:
            if char in main_dict:
                word_res.append(main_dict[char])
            elif char == '\n':
                word_res.append('\n')
        out.append(word_res)
    str_out = ' '.join([''.join(word) for word in out])  # склеивание списка
    # str_out = str_out.replace('|', ' ')  # дополнительна проверка на раделители
    return str_out  # конечное склеивание


def vigenere_encode(key, text, lang='RU'):
    # избавление текста и ключа от "лишних" знаков
    key = ''.join(map(lambda x: x.lower() if x.isalnum() or x == ' ' else '', key))
    text = ''.join(map(lambda x: x.lower() if x.isalnum() or x == ' ' else '', text))

    out = []  # список, который будет возвращаться
    no_alpha_chars = 0  # счетчик не алфавитных символов, чтобы индексы ключа правильно считались
    # выбираем нужный список для шифрования
    if lang == 'RU':
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    # проверка на наличие всех символов в списке
    if not all([True if x in main_list or x.isdigit() or x == ' ' else False for x in text]):
        if not all([True if x in main_list or x.isdigit() or x == ' ' else False for x in key]):
            raise WrongChar('В тексте или в ключе есть символ другого языка')

    for index, char in enumerate(text):
        if char.isalpha():  # обработка толкько словарных символов
            mj = main_list.index(char)  # индекс буквы слова
            kj = main_list.index(key[(index - no_alpha_chars) % len(key)])
            # индекс ключа с учетом "лишних" символов
            cj = (mj + kj) % len(main_list)  # индекс уже зашифрованной буквы
            out.append(main_list[cj])  # добавление зашифрованной буквы в список
        else:
            no_alpha_chars += 1  # увеличение счетчика "лишних" символов
            out.append(char)
    return ''.join(out)


def vigenere_decode(key, text, lang='RU'):
    # избавление текста и ключа от "лишних" знаков
    key = ''.join(map(lambda x: x if x.isalnum() or x == ' ' else '', key))
    text = ''.join(map(lambda x: x if x.isalnum() or x == ' ' else '', text))

    out = []  # список, который будет возвращаться
    no_alpha_chars = 0  # счетчик не алфавитных символов, чтобы индексы ключа правильно считались
    # выбираем нужный список для шифрования
    if lang == 'RU':
        main_list = ALPHABET_RU
    elif lang == 'ENG':
        main_list = ALPHABET_ENG
    else:
        raise WrongLanguage('Введён неверный язык')  # исключение, если нет такого языка
    # проверка на наличие всех символов в списке
    if not all([True if x in main_list or x.isdigit() or x == ' ' else False for x in text]):
        if not all([True if x in main_list or x.isdigit() or x == ' ' else False for x in key]):
            raise WrongChar('В тексте или в ключе есть символ другого языка')

    for index, char in enumerate(text):  # используем enumerate, чтобы сохранить индексы букв
        if char.isalpha():  # обработка толкько словарных символов
            cj = main_list.index(char)  # индекс буквы слова
            kj = main_list.index(key[(index - no_alpha_chars) % len(key)])
            # индекс ключа с учетом пробелов
            mj = (cj - kj) % len(main_list)  # индекс уже расшифрованной буквы
            out.append(main_list[mj])  # добавление расшифрованной буквы в список
        else:
            no_alpha_chars += 1  # увеличение счетчика "лишних" символов
            out.append(char)
    return ''.join(out)
