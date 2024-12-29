from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card

hidden_card_number = get_mask_card_number('5678904547123457')
print(hidden_card_number)

hidden_bill_number = get_mask_account('5678904547123457')
print(hidden_bill_number)

types_cards = mask_account_card('Visa Platinum')
print(types_cards)


