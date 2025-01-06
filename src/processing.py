from typing import Dict, List
#импортируем библиотеку для аннотации функции

def filter_by_state(l_lict: List[Dict], key: str = "EXECUTED") -> List[Dict]:
    #Создаем функцию фильтрации
    new_filter_by_state = []
    key_users = "CANCELED"
    for item in l_lict:
        if item["state"] == key:
            new_filter_by_state.append(item)
        elif item["state"] == key_users:
            new_filter_by_state.append(item)
    return new_filter_by_state


def sort_by_date(last_dict: List[Dict], keys_date: str = "%Y-%m-%dT%H:%M:%S.%f") -> List[Dict]:
    #Создаем функцию сортировки по дате
    #Создаем пустой список для неотсортированных данных
    new_date_list = []
    #Создаем пустой список для сортировки
    sorted_date_list = []
    for item in last_dict:
        #В цикле перебираем данные и добавляем в список
        new_date_list.append({"id": item["id"], "state": item["state"], "date": item["date"]})
    #Сортируем данные по ключу date и добавляем в список согласно сортировке
    sorted_date_list = sorted(new_date_list, key=lambda x: x["date"], reverse=True)

    return sorted_date_list

#Проверочки
spi_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
spi_exe = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2028-06-30T02:08:58.425572"},
]
print(filter_by_state(spi_exe))
print(sort_by_date(spi_exe))

print(filter_by_state(spi_canceled))
print(sort_by_date(spi_canceled))
