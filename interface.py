from abc import ABCMeta
from abc import abstractmethod
from datetime import datetime


class IData(metaclass=ABCMeta):
    @property
    @abstractmethod
    def first_date(self) -> datetime:
        """
        保持するデータの先頭日付を返却する

        Returns
        ---------
        0: datetime
            先頭日付

        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def end_date(self) -> datetime:
        """
        保持するデータの最後尾日付を返却する

        Returns
        ---------
        0: datetime
            最後尾日付

        """
        raise NotImplementedError()

    @abstractmethod
    def buy(self, date: datetime, amount: int) -> int:
        """
        指定金額で購入する際の
        取得口数を算出する

        Params
        ---------
        date: datetime
            購入日付
        amount: int
            購入金額

        Returns
        ---------
        0: int
            取得口数

        """
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self, date: datetime, unit_num: int) -> int:
        """
        指定日付の基準価格ベースでの評価額を算出する

        Params
        ---------
        date: datetime
            評価額算出日付
        unit_num: int
            口数

        Returns
        ---------
        0: int
            評価額
        """
        raise NotImplementedError()

    @abstractmethod
    def exists(self, date: datetime) -> bool:
        """
        指定日付のデータが存在するか判定する

        Params
        ---------
        date: datetime
            判定日付

        Returns
        ---------
        0: bool
            True: 有 / False: 無
        """
        raise NotImplementedError()

    @abstractmethod
    def get_continuous_date(self) -> list:
        """
        連続した日付のリストを返す

        Returns
        ---------
        0: list
            連続した日付
        """
        raise NotImplementedError()

    @abstractmethod
    def get_next_buy_date(self) -> datetime:
        """
        次の買付日付を返す

        Returns
        ---------
        0: datetime
            次の買付日付
        """
        raise NotImplementedError()
