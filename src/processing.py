from typing import Dict, List

# импортируем библиотеку для аннотации функции


def filter_by_state(l_lict: List[Dict], key: str = "EXECUTED") -> List[Dict]:
    # Создаем функцию фильтрации
    new_filter_by_state = []
    for item in l_lict:
        if item["state"] == key:
            new_filter_by_state.append(item)
        else:
            new_filter_by_state.append(item)
    return new_filter_by_state


def sort_by_date(last_dict: List[Dict], keys_date: str = "True") -> List[Dict]:
    # Создаем функцию сортировки по дате
    # Создаем пустой список для неотсортированных данных
    new_date_list = []
    # Создаем пустой список для сортировки
    sorted_date_list = []
    for item in last_dict:
        # В цикле перебираем данные и добавляем в список
        new_date_list.append({"id": item["id"], "state": item["state"], "date": item["date"]})
    # Сортируем данные по ключу date и добавляем в список согласно сортировке
    if keys_date == "True":
        sorted_date_list = sorted(new_date_list, key=lambda x: x["date"], reverse=True)
    else:
        sorted_date_list = sorted(new_date_list, key=lambda x: x["date"])

    return sorted_date_list

