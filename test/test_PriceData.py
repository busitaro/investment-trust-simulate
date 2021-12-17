import sys
import unittest
import mock
from datetime import datetime
from datetime import timedelta

from data.price import PriceData


class TestPriceData(unittest.TestCase):
    def setUpData(self, case: str):
        read_file = {
            'test_first_date1': 'test/file/test.csv',
            'test_end_date1': 'test/file/test.csv',
            'test_buy1': 'test/file/test.csv',
            'test_buy2': 'test/file/test.csv',
            'test_evaluate1': 'test/file/test.csv',
            'test_evaluate2': 'test/file/test.csv',
            'test_exists1': 'test/file/test.csv',
            'test_exists2': 'test/file/test.csv',
            'test_get_continuous_date1': 'test/file/test_date.csv',
            'test_get_next_buy_date1': 'test/file/test_date.csv',
        }
        self.priceData = PriceData(read_file[case])

    def tearDown(self):
        del self.priceData

    def test_first_date1(self):
        """
        first_dateのチェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        self.assertEqual(
            datetime.strptime('2021/11/10', '%Y/%m/%d'),
            self.priceData.first_date
        )

    def test_end_date1(self):
        """
        end_dateのチェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        self.assertEqual(
            datetime.strptime('2021/11/12', '%Y/%m/%d'),
            self.priceData.end_date
        )

    def test_buy1(self):
        """
        buyの正常動作を確認

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/11/10', '%Y/%m/%d')
        result = self.priceData.buy(date, 20000)
        self.assertEqual(result, 9000)

    def test_buy2(self):
        """
        buyに存在しない日付を指定した場合の例外チェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/12/31', '%Y/%m/%d')
        with self.assertRaises(ValueError):
            self.priceData.buy(date, 20000)

    def test_evaluate1(self):
        """
        evaluateの正常動作を確認

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/11/12', '%Y/%m/%d')
        unit_num = 835_229
        result = self.priceData.evaluate(date, unit_num)
        self.assertEqual(result, 2_784_069)

    def test_evaluate2(self):
        """
        evaluateに存在しない日付を指定した場合の例外チェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/12/31', '%Y/%m/%d')
        unit_num = 835_229
        with self.assertRaises(ValueError):
            self.priceData.evaluate(date, unit_num)

    def test_exists1(self):
        """
        データが存在する場合のexists

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/11/11', '%Y/%m/%d')
        result = self.priceData.exists(date)
        self.assertEqual(result, True)

    def test_exists2(self):
        """
        データが存在しない場合のexists

        """
        self.setUpData(sys._getframe().f_code.co_name)
        date = datetime.strptime('2021/12/31', '%Y/%m/%d')
        result = self.priceData.exists(date)
        self.assertEqual(result, False)

    def test_get_continuous_date1(self):
        """
        get_continuous_dateのチェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        expected_list = [
            datetime.strptime('2020/01/01', '%Y/%m/%d'),
            datetime.strptime('2020/01/02', '%Y/%m/%d'),
            datetime.strptime('2020/01/03', '%Y/%m/%d'),
            datetime.strptime('2020/01/04', '%Y/%m/%d'),
            datetime.strptime('2020/01/05', '%Y/%m/%d'),
            datetime.strptime('2020/01/06', '%Y/%m/%d'),
            datetime.strptime('2020/01/07', '%Y/%m/%d'),
            datetime.strptime('2020/01/08', '%Y/%m/%d'),
            datetime.strptime('2020/01/09', '%Y/%m/%d'),
            datetime.strptime('2020/01/10', '%Y/%m/%d'),
            datetime.strptime('2020/01/11', '%Y/%m/%d'),
            datetime.strptime('2020/01/12', '%Y/%m/%d'),
            datetime.strptime('2020/01/13', '%Y/%m/%d'),
            datetime.strptime('2020/01/14', '%Y/%m/%d'),
            datetime.strptime('2020/01/15', '%Y/%m/%d'),
            datetime.strptime('2020/01/16', '%Y/%m/%d'),
            datetime.strptime('2020/01/17', '%Y/%m/%d'),
            datetime.strptime('2020/01/18', '%Y/%m/%d'),
            datetime.strptime('2020/01/19', '%Y/%m/%d'),
            datetime.strptime('2020/01/20', '%Y/%m/%d'),
            datetime.strptime('2020/01/21', '%Y/%m/%d'),
            datetime.strptime('2020/01/22', '%Y/%m/%d'),
            datetime.strptime('2020/01/23', '%Y/%m/%d'),
            datetime.strptime('2020/01/24', '%Y/%m/%d'),
            datetime.strptime('2020/01/25', '%Y/%m/%d'),
            datetime.strptime('2020/01/26', '%Y/%m/%d'),
            datetime.strptime('2020/01/27', '%Y/%m/%d'),
            datetime.strptime('2020/01/28', '%Y/%m/%d'),
            datetime.strptime('2020/01/29', '%Y/%m/%d'),
            datetime.strptime('2020/01/30', '%Y/%m/%d'),
            datetime.strptime('2020/01/31', '%Y/%m/%d'),
        ]

        for idx, result in enumerate(self.priceData.get_continuous_date()):
            self.assertEqual(
                expected_list[idx],
                result
            )

    @mock.patch('random.randint')
    def test_get_next_buy_date1(self, random_call):
        """
        get_next_buy_dateのチェック

        """
        self.setUpData(sys._getframe().f_code.co_name)
        random_call.return_value = 20
        delta = timedelta(days=20)

        first_date = datetime.strptime('2020/01/01', '%Y/%m/%d')

        for i in range(5):
            expected = first_date + delta * (i + 1)
            result = self.priceData.get_next_buy_date()
            self.assertEqual(
                expected,
                result
            )


if __name__ == '__main__':
    unittest.main()
