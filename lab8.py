def analyze_vowels(text):
    vowels = "аеєиіїоуюяAEЄИІЇОУЮЯaeiouAEIOU"
    vowel_list = [char for char in text if char in vowels]
    print("Кількість голосних букв:", len(vowel_list))
    print("Самі голосні:", vowel_list)

def process_number_lists(list1, list2):
    if not list1 and not list2:
        print("Обидва списки порожні.")
        return []
    
    combined = list1 + list2
    unique_sorted = sorted(set(combined))
    print("Об'єднаний, без повторів і відсортований список:", unique_sorted)
    return unique_sorted

def analyze_text_symbols(text):
    from collections import Counter

    char_counter = Counter(text)
    print("Частота кожного символу:")
    for char, count in char_counter.items():
        print(f"'{char}': {count}")

    unique_chars = {char for char, count in char_counter.items() if count == 1}
    print("Унікальні символи:", unique_chars)

    common_chars = {char for char, count in char_counter.items() if count > 1}
    print("Символи, що повторюються:", common_chars)


print("=== Завдання 1 ===")
analyze_vowels("Привіт, як справи?")

print("\n=== Завдання 2 ===")
process_number_lists([1, 2, 3, 2], [3, 4, 5])

print("\n=== Завдання 3 ===")
analyze_text_symbols("Привіт, як справи?")
