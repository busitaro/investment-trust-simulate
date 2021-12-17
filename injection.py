from injector import Module

from interface import IData
from data.price import PriceData
from test.stub.price import PriceData as testPriceData


class DataDIModule(Module):
    def __init__(self, filepath: str):
        self.__filepath = filepath

    def configure(self, binder) -> None:
        binder.bind(IData, to=PriceData(self.__filepath))


class TestDIModule(Module):
    def configure(self, binder) -> None:
        binder.bind(IData, to=testPriceData())
