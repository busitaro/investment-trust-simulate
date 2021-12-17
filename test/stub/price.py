from datetime import datetime

from interface import IData


class PriceData(IData):
    def __init__(self):
        self.__buy_date_count = 0

    @property
    def first_date(self) -> datetime:
        raise NotImplementedError()

    @property
    def end_date(self) -> datetime:
        raise NotImplementedError()

    def buy(self, date: datetime, amount: int) -> int:
        if date == datetime(2020, 1, 2):
            return 40930
        elif date == datetime(2020, 1, 4):
            return 8573
        elif date == datetime(2020, 1, 7):
            return 5839
        elif date == datetime(2020, 1, 9):
            return 10390
        elif date == datetime(2020, 1, 10):
            return 7437
        else:
            raise ValueError('date is unexpected')

    def evaluate(self, date, unit_num) -> int:
        if date == datetime(2020, 1, 1):
            return 40930
        elif date == datetime(2020, 1, 2):
            return 83920
        elif date == datetime(2020, 1, 3):
            return 8482
        elif date == datetime(2020, 1, 4):
            return 90832
        elif date == datetime(2020, 1, 5):
            return 300000
        elif date == datetime(2020, 1, 6):
            return 7348729
        elif date == datetime(2020, 1, 7):
            return 7473
        elif date == datetime(2020, 1, 8):
            return 904839
        elif date == datetime(2020, 1, 9):
            return 848398
        elif date == datetime(2020, 1, 10):
            return 62362
        else:
            raise ValueError('date is unexpected')

    def exists(self, date) -> bool:
        return True

    def get_continuous_date(self) -> list:
        return [
            datetime(2020, 1, 1),
            datetime(2020, 1, 2),
            datetime(2020, 1, 3),
            datetime(2020, 1, 4),
            datetime(2020, 1, 5),
            datetime(2020, 1, 6),
            datetime(2020, 1, 7),
            datetime(2020, 1, 8),
            datetime(2020, 1, 9),
            datetime(2020, 1, 10),
        ]

    def get_next_buy_date(self) -> datetime:
        buy_dates = [
            datetime(2020, 1, 2),
            datetime(2020, 1, 4),
            datetime(2020, 1, 7),
            datetime(2020, 1, 9),
            datetime(2020, 1, 10),
        ]

        if self.__buy_date_count < len(buy_dates):
            buy_date = buy_dates[self.__buy_date_count]
            self.__buy_date_count = self.__buy_date_count + 1
        else:
            buy_date = None
        return buy_date
