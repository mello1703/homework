from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str:
    """ Функция, маскирующая счет и карту. """
    if "Счет" in nums:
        return f"Счет {get_mask_account(nums[5:])}"
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


def get_date(date_sting: str) -> str:
    """
    функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"  и возвращает
    строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    if len(date_sting) == 0:
        raise ValueError("Отсутствует дата")
    date_obj = datetime.fromisoformat(date_sting).date()
    return date_obj.strftime("%d.%m.%Y")


# if __name__ == '__main__':
#     print(get_data("2024-03-11T02:26:18.671407"))
