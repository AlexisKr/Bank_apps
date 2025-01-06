from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card

hidden_card_number = get_mask_card_number("5678904547123457")
print(hidden_card_number)

hidden_bill_number = get_mask_account("5678904547123457")
print(hidden_bill_number)

types_cards = mask_account_card("Visa Platinum 7700689045601234")
print(types_cards)

processing_check_sort = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2028-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
print(processing_check_sort)

processing_check_filter = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
)
print(processing_check_filter)

processing_check_canceled_filter = filter_by_state(
    [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
print(processing_check_canceled_filter)
