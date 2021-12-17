from datetime import datetime
from datetime import timedelta
import random

import pandas as pd

from interface import IData


class PriceData(IData):
    def __init__(self, target_file: str):
        self.target_file = target_file
        self.__price_df = self.__input_price()
        self.__price_df['date'] = pd.to_datetime(self.__price_df['date'])
        self.__buy_date = self.first_date
        self.buy_total_num = 0
        self.buy_total_price = 0

    @property
    def first_date(self) -> datetime:
        return self.__price_df.iloc[0].date

    @property
    def end_date(self) -> datetime:
        return self.__price_df.iloc[-1].date

    def buy(self, date: datetime, amount: int) -> int:
        data = self.__search_by_date(date)
        if data is None:
            raise ValueError('data of {} is nothing'.format(date))
        else:
            return round(amount / data.base_price * 10000, 0)

    def evaluate(self, date, unit_num) -> int:
        data = self.__search_by_date(date)
        if data is None:
            raise ValueError('data of {} is nothing'.format(date))
        else:
            return round(data.base_price * unit_num / 10000, 0)

    def exists(self, date) -> bool:
        data = self.__search_by_date(date)
        return data is not None

    def get_continuous_date(self):
        for days in range((self.end_date - self.first_date).days):
            yield self.first_date + timedelta(days)

    def get_next_buy_date(self):
        if self.__buy_date == self.first_date:
            delta = timedelta(random.randint(0, 20))
        else:
            delta = timedelta(random.randint(20, 40))
        self.__buy_date = self.__buy_date + delta
        return self.__buy_date

    def __input_price(self) -> pd.DataFrame:
        price_df = \
            pd.read_csv(self.target_file) \
            .sort_values(by=['date']) \
            .reset_index() \
            .drop('index', axis=1)
        return price_df

    def __search_by_date(self, date: datetime):
        target_df = \
            self.__price_df[self.__price_df['date'] == date]
        if len(target_df) != 1:
            return None
        else:
            return target_df.iloc[0]
