import unittest
from main import duplicate_check_function_1,func

class TestMethod(unittest.TestCase):
    # 测试两个相同文本
    def test_same_file(self):
        duplicate_check_function_1("D:\origi.txt","D:\origi.txt")

    # 测试两个空文本
    def test_empty_file(self):
        duplicate_check_function_1("D:\oigiempty.txt","D:\oigiempty.txt")

    # 测试两个错误路径
    def test_wrong_path(self):
        duplicate_check_function_1("D:\origin.txt","D:\origi.txt")

    # 测试两个不同文本
    def test_diff_file(self):
        duplicate_check_function_1("D:\origi.txt","D:\origidif.txt")

    # 测试两个相似文本
    def test_sim_file(self):
        duplicate_check_function_1("D:\origi.txt","D:\origicopy.txt")

    # 测试两个大的文本
    def test_long_file(self):
        func("D:\orig.txt","D:\orig_0.8_add.txt")

    # 测试一个大的文本和一个小的文本
    def test_sl_file(self):
        func("D:\orig.txt","D:\origi.txt")

    # 测试两个不同类型的大文本
    def test_dl_file(self):
        func("D:\orig.txt","D:\orig_0.8_dis_1.txt")
    # 测试一个空文本和一个有内容的文本
    def test_eh_file(self):
        duplicate_check_function_1("D:\origi.txt","D:\oigiempty.txt")
    # 测试一个路径错误文本和一个空文本
    def test_wpe_file(self):
        duplicate_check_function_1("D:\oigion.txt","D:\oigiempty.txt")