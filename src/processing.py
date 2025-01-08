from typing import Dict, List

# импортируем библиотеку для аннотации функции


def filter_by_state(l_lict: List[Dict], key_s: str = "EXECUTED") -> List[Dict]:
    """
    принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    # Создаем логиику функции фильтрации
    new_filter_by_state = []
    # Создаем цикл для перебора данных
    for item in l_lict:
        # Создаем условие для фильтрации
        if item["state"] == key_s:
            # Добавляем данные в список
            new_filter_by_state.append(item)
    return new_filter_by_state


def sort_by_date(last_dict: List[Dict], descending: bool = "True") -> List[Dict]:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date
    ).
    """
    # Создаем пустой список для неотсортированных данных
    new_date_list = []
    for item in last_dict:
        # В цикле перебираем данные и добавляем в список
        new_date_list.append({"id": item["id"], "state": item["state"], "date": item["date"]})

    return sorted(last_dict, key=lambda x: x["date"], reverse=descending)
