from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card: str) -> str:
    # Создаем функцию выбора типа карты

    # Создаем переменную хранящию выбор типа карты
    str_card_number = ""
    # создаем переменную хранящую выбор типа счета
    str_bill_number = ""

    # находим набор чисел в строке
    is_digit_str = "".join(i if i.isdigit() else " " for i in type_card)
    # создаем условие выбора типа карты и применяем метод .lower
    if type_card.lower() == "Visa Platinum" or type_card.lower() == "Maestro":
        str_card_number += type_card
        return f"{str_card_number} {get_mask_card_number(is_digit_str)} "
    else:
        str_bill_number += type_card
        return f"{str_bill_number} {get_mask_account(is_digit_str)} "


def get_date(user_of_date: str) -> str:
    # Создаем функцию фиксации времени

    # Импорт библиотеки datetime
    import datetime

    # переделаем строку в объект
    date_format = datetime.datetime.strptime(user_of_date, "%Y-%m-%dT%H:%M:%S.%f")

    # форматируем строку в "Д.М.Г"
    new_date = date_format.strftime("%d.%m.%Y")

    return new_date


types_cards = mask_account_card("Visa Platinum 7700908956781245")
print(types_cards)


print(get_date("2024-12-29T19:34:34.671407"))
