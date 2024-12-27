from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str:
    """ Функция, маскирующая счет и карту. """
    if "Счет" in nums:
        return f"Счет {get_mask_account(nums[5:])}"
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))


def get_data(old_data: str) -> str:
    """ Функция принимает строку и выводит дату в формате ДД.ММ.ГГ """
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])


if __name__ == '__main__':
    print(get_data("2024-03-11T02:26:18.671407"))
