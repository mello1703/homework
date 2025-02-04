import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename="../logs/masks_log.log",
    filemode="w",
    )
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()

# account_number = input()
# card_number_str = input()


def get_mask_card_number(card_number: str) -> str:
    """Функция,  которая шифрует номер карты"""
    card_number_logger.info("Создаю маску номера карты")
    if len(card_number) == 16 and card_number.isdigit():
        card_number_logger.error("Неправильный номер карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    card_number_logger.info("Маска номера карты создана")
    return "некорректный ввод"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    mask_account_logger.info("Создаю маску номера счета")
    if len(account_number) == 20 and account_number.isdigit():
        mask_account_logger.error("Неправильный номер счета")
        return f"**{account_number[-4:]}"
    mask_account_logger.info("Маска номера счета создана")
    return "некорректный ввод"


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
