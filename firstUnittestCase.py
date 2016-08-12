# coding=utf-8
import unittest

'''
测试除法
1、自动以1个除法函数div
2、测试 1/1
3、测试 3/4
4、测试 3/0
'''


def div(a, b):
    return a / b
    # 1 / 2 = 1


class MyfirstTestCase(unittest.TestCase):
    pass

    def setUp(self):
        print 'run before every testcase'

    def tearDown(self):
        print 'run after every testcase'

    def test_1div1(self):
        print 'case1:1/1'
        case1 = div(1, 1)
        self.assertEqual(case1, 1/1)

    def test_3div4(self):
        print 'case1:3/4'
        case2 = div(3, 4)
        self.assertEqual(case2, 3/4)

    def test_3div0(self):
        print 'case3:3/0'
        case3 = div(3, 0)
        self.assertRaises(ZeroDivisionError, div, 3, 0)


if __name__ == '__main__':
    unittest.main()
