import unittest
from datetime import datetime
from pprint import pprint

from injector import Injector

from simulate import Simulator
from injection import TestDIModule


class TestDateControl(unittest.TestCase):
    def setUp(self) -> None:
        injector = Injector([TestDIModule()])
        self.simulator = injector.get(Simulator)

    def test_exec1(self):
        """
        execの正常系確認

        """
        expected_buy_history = [
            [datetime(2020, 1, 2), 30_000, 40930],
            [datetime(2020, 1, 4), 30_000, 8573],
            [datetime(2020, 1, 7), 30_000, 5839],
            [datetime(2020, 1, 9), 30_000, 10390],
            [datetime(2020, 1, 10), 30_000, 7437],
        ]
        expected_evaluation = [
            [datetime(2020, 1, 1), 0, 0, 40930, 40930],
            [datetime(2020, 1, 2), 30_000, 40930, 83920, 53920],
            [datetime(2020, 1, 3), 30_000, 40930, 8482, -21518],
            [datetime(2020, 1, 4), 60_000, 49503, 90832, 30832],
            [datetime(2020, 1, 5), 60_000, 49503, 300000, 240000],
            [datetime(2020, 1, 6), 60_000, 49503, 7348729, 7288729],
            [datetime(2020, 1, 7), 90_000, 55342, 7473, -82527],
            [datetime(2020, 1, 8), 90_000, 55342, 904839, 814839],
            [datetime(2020, 1, 9), 120_000, 65732, 848398, 728398],
            [datetime(2020, 1, 10), 150_000, 73169, 62362, -87638],
        ]

        self.simulator.exec(amount_per_buying=30_000)

        # 購入履歴
        try:
            self.assertEqual(
                len(self.simulator.buy_history),
                len(expected_buy_history)
            )
            for idx in range(len(expected_buy_history)):
                self.assertEqual(
                    len(self.simulator.buy_history[idx]),
                    len(expected_buy_history[idx])
                )
                for idx2 in range(len(expected_buy_history[idx])):
                    self.assertEqual(
                        self.simulator.buy_history[idx][idx2],
                        expected_buy_history[idx][idx2]
                    )
        except Exception as ex:
            print('------ expected ------')
            pprint(expected_buy_history)
            print('------ actual ------')
            pprint(self.simulator.buy_history)
            raise ex

        # 評価
        try:
            self.assertEqual(
                len(self.simulator.evaluation_history),
                len(expected_evaluation)
            )
            for idx in range(len(expected_evaluation)):
                self.assertEqual(
                    len(self.simulator.evaluation_history[idx]),
                    len(expected_evaluation[idx])
                )
                for idx2 in range(len(expected_evaluation[idx])):
                    self.assertEqual(
                        self.simulator.evaluation_history[idx][idx2],
                        expected_evaluation[idx][idx2]
                    )
        except Exception as ex:
            print('------ expected ------')
            pprint(expected_evaluation)
            print('------ actual ------')
            pprint(self.simulator.evaluation_history)
            raise ex


if __name__ == '__main__':
    unittest.main()
