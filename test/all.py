from unittest import defaultTestLoader
from unittest import TestSuite
from unittest import TextTestRunner


def main(path):
    test_suite = TestSuite()
    all_test = defaultTestLoader.discover(path, pattern='test_*.py')
    for test in all_test:
        test_suite.addTest(test)

    TextTestRunner().run(test_suite)


if __name__ == '__main__':
    path = './test'
    main(path)
