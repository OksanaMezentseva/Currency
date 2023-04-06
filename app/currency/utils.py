from _decimal import Decimal


def to_2_point_decimal(value: str) -> Decimal:
    '''
    Convert str value to Decimal with 2 places
    :param value: '123.456'
    :return: 123.45
    '''
    return round(Decimal(value), 2)