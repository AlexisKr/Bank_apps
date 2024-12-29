from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.masks import number_of_bill

hidden_card_number = get_mask_card_number('5678904547123457')
print(hidden_card_number)

hidden_bill_number = get_mask_account('5678904547123455')
print(hidden_bill_number)
