# account_number = input()
# card_number_str = input()


def get_mask_card_number(card_number: str) -> str:
    """Функция,  которая шифрует номер карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "некорректный ввод"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    return "некорректный ввод"

#
# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
