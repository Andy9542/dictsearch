first_letter = ""
second_letter = ""
third_letter = ""
fourth_letter = ""
fifth_letter = ""
sixth_letter = ""
seventh_letter = ""
eighth_letter = ""
ninth_letter = ""
tenth_letter = ""
eleventh_letter = ""
twelfth_letter = ""
thirteenth_letter = ""
fourteenth_letter = ""
fifteenth_letter = ""

def load_dictionary_from_file(file_path):
    """Загружает список слов из файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

def get_user_input():
    """Получает входные данные от пользователя."""
    global letters_count_in_word, first_letter, second_letter, third_letter, fourth_letter, fifth_letter, sixth_letter, seventh_letter, eighth_letter, ninth_letter, tenth_letter, eleventh_letter, twelfth_letter, thirteenth_letter, fourteenth_letter, fifteenth_letter, letters
    
    # Запрос длины слова
    while True:
        try:
            letters_count_in_word = int(input("Укажите длину слова (от 2 до 15): "))
            if 2 <= letters_count_in_word <= 15:
                break
            print("Длина слова должна быть от 2 до 15 символов.")
        except ValueError:
            print("Введите корректное число.")
    
    # Запрос фиксированных букв
    print("Введите фиксированные буквы (оставьте пустым, если буква может быть любой):")
    first_letter = input("Первая буква: ").lower() or ""
    second_letter = input("Вторая буква: ").lower() or ""
    third_letter = input("Третья буква: ").lower() or ""
    fourth_letter = input("Четвертая буква: ").lower() or ""
    fifth_letter = input("Пятая буква: ").lower() or ""
    sixth_letter = input("Шестая буква: ").lower() or ""
    seventh_letter = input("Седьмая буква: ").lower() or ""
    eighth_letter = input("Восьмая буква: ").lower() or ""
    ninth_letter = input("Девятая буква: ").lower() or ""
    tenth_letter = input("Десятая буква: ").lower() or ""
    eleventh_letter = input("Одиннадцатая буква: ").lower() or ""
    twelfth_letter = input("Двенадцатая буква: ").lower() or ""
    thirteenth_letter = input("Тринадцатая буква: ").lower() or ""
    fourteenth_letter = input("Четырнадцатая буква: ").lower() or ""
    fifteenth_letter = input("Пятнадцатая буква: ").lower() or ""
    
    # Запрос доступных букв
    letters_input = input("Введите доступные буквы через запятую (например: а,б,в,г): ").lower()
    if letters_input:
        letters = [letter.strip() for letter in letters_input.split(',')]
    else:
        # Значение по умолчанию, если пользователь не ввел буквы
        letters = ["р", "и", "с", "т", "а", "л", "л"]
        print(f"Используются буквы по умолчанию: {','.join(letters)}")

def get_fixed_letters():
    """Возвращает словарь с фиксированными буквами и их позициями."""
    fixed_letters = {}

    if first_letter and 0 < letters_count_in_word:
        fixed_letters[0] = first_letter
    if second_letter and 1 < letters_count_in_word:
        fixed_letters[1] = second_letter
    if third_letter and 2 < letters_count_in_word:
        fixed_letters[2] = third_letter
    if fourth_letter and 3 < letters_count_in_word:
        fixed_letters[3] = fourth_letter
    if fifth_letter and 4 < letters_count_in_word:
        fixed_letters[4] = fifth_letter
    if sixth_letter and 5 < letters_count_in_word:
        fixed_letters[5] = sixth_letter
    if seventh_letter and 6 < letters_count_in_word:
        fixed_letters[6] = seventh_letter
    if eighth_letter and 7 < letters_count_in_word:
        fixed_letters[7] = eighth_letter
    if ninth_letter and 8 < letters_count_in_word:
        fixed_letters[8] = ninth_letter
    if tenth_letter and 9 < letters_count_in_word:
        fixed_letters[9] = tenth_letter
    if eleventh_letter and 10 < letters_count_in_word:
        fixed_letters[10] = eleventh_letter
    if twelfth_letter and 11 < letters_count_in_word:
        fixed_letters[11] = twelfth_letter
    if thirteenth_letter and 12 < letters_count_in_word:
        fixed_letters[12] = thirteenth_letter
    if fourteenth_letter and 13 < letters_count_in_word:
        fixed_letters[13] = fourteenth_letter
    if fifteenth_letter and 14 < letters_count_in_word:
        fixed_letters[14] = fifteenth_letter
    
    return fixed_letters

def count_letters(letters_list):
    """Создает словарь с частотами букв."""
    letter_counts = {}
    for letter in letters_list:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def generate_words(position, current_word, available_letters, fixed_letters):
    """Рекурсивно генерирует все возможные слова заданной длины с фиксированными буквами."""
    # Базовый случай: слово полностью сформировано
    if position >= letters_count_in_word:
        return [current_word]
    
    # Если текущая позиция содержит фиксированную букву
    if position in fixed_letters:
        return generate_words(position + 1, current_word + fixed_letters[position], available_letters, fixed_letters)
    
    # Иначе пробуем все доступные буквы
    results = []
    used_letters = set()  # Для отслеживания уже использованных букв на этом уровне рекурсии
    
    for letter in available_letters:
        if available_letters[letter] > 0 and letter not in used_letters:
            used_letters.add(letter)  # Отмечаем букву как использованную на данном уровне
            
            # Уменьшаем количество доступных букв
            available_letters[letter] -= 1
            
            # Рекурсивно генерируем слова с оставшимися буквами
            results.extend(generate_words(position + 1, current_word + letter, available_letters, fixed_letters))
            
            # Возвращаем букву обратно в доступные
            available_letters[letter] += 1
    
    return results

def search_words_in_dictionary(dictionary):
    """Ищет все возможные комбинации слов в словаре."""
    fixed_letters = get_fixed_letters()
    letter_counts = count_letters(letters)
    possible_words = generate_words(0, "", letter_counts, fixed_letters)
    
    found_words = []
    for word in possible_words:
        if word in dictionary and len(word) == letters_count_in_word:
            found_words.append(word)
    
    return found_words

# Запуск поиска
if __name__ == "__main__":
    # Загрузка словаря из файла
    dictionary = load_dictionary_from_file("./dictionaries/nouns.txt")
    print(f"Загружено {len(dictionary)} слов из словаря.")
    
    # Получение пользовательского ввода
    get_user_input()
    
    # Поиск слов
    found_words = search_words_in_dictionary(dictionary)
    
    # Вывод результатов
    print(f"Найдено слов: {len(found_words)}")
    for word in found_words:
        print(word)
    
    # Сохранение результатов в файл, если найдены слова
    if found_words:
        output_file = "results.txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"Найдено слов: {len(found_words)}\n")
            for word in found_words:
                file.write(f"{word}\n")
        print(f"Результаты сохранены в файл {output_file}")
