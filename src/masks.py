def get_mask_card_number(number_of_card: str) -> str:
    """принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    str_card_number = ""
    if len(number_of_card) == 16:
        str_card_number += number_of_card
    else:
        print("Error card number")

    private_number = str_card_number[:6] + (len(str_card_number[6:-4]) * "*") + str_card_number[-4:]  # noqa: E501
    space_four = len(private_number)
    space_number = len(str_card_number) // 4  # делим строку по 4 символа

    return " ".join([private_number[i : i + space_number] for i in range(0, space_four, space_number)])  # noqa: E501


number_of_bill = int(input("Enter the number of bill: "))


def get_mask_account(number_of_bill: str) -> str:
    """принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX
    """

    str_bill_number = str(number_of_bill)  # вернет строку

    return "*" * len(str_bill_number[:-14]) + str_bill_number[-4:]
