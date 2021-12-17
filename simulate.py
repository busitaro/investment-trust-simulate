import sys
from csv import writer

from injector import Injector
from injector import inject

from interface import IData
from injection import DataDIModule


class Simulator():
    @inject
    def __init__(self, data: IData):
        self.__data = data
        self.buy_history = []
        self.evaluation_history = []

    def exec(self, amount_per_buying: int):
        total_purchase_price = 0    # 累計買付価格
        unit_num = 0                    # 保有口数
        buy_date = self.__data.get_next_buy_date()

        for date in self.__data.get_continuous_date():
            if self.__data.exists(date):
                if (buy_date is not None) and (date >= buy_date):
                    # 買付
                    buy_num = self.__data.buy(date, amount_per_buying)
                    unit_num = \
                        unit_num + buy_num
                    total_purchase_price = \
                        total_purchase_price + amount_per_buying
                    buy_date = self.__data.get_next_buy_date()
                    self.buy_history.append(
                        [date, amount_per_buying, buy_num]
                    )
                # 評価
                evaluation = self.__data.evaluate(date, unit_num)
                self.evaluation_history.append([
                    date,
                    total_purchase_price,
                    unit_num,
                    evaluation,
                    evaluation - total_purchase_price
                ])

    def output(self):
        with open('file/output/buy.csv', 'w', newline='') as f:
            writer(f).writerows(self.buy_history)
        with open('file/output/evaluation.csv', 'w', newline='') as f:
            writer(f).writerows(self.evaluation_history)


def main():
    args = sys.argv
    if len(args) != 2:
        print('parameter is invalid')
        quit()

    injector = Injector([DataDIModule('file/input/target.csv')])
    simulator = injector.get(Simulator)

    simulator.exec(amount_per_buying=int(args[1]))
    simulator.output()


if __name__ == '__main__':
    main()
