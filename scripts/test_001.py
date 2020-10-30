import pytest, allure, os

# class Test_Abc:
#     def test_abc_001(self):
#         assert 1
#
# if __name__ == '__main__':
#     pytest.main("-s --alluredir report test_001.py")

# class Test_Abc:
#     @allure.step(title="第一个测试")
#     def test_abc_001(self):
#         # assert 1
#         assert 0

class Test_Abc:
    @allure.step(title="第一个测试")
    def test_abc_001(self):
        allure.attach("这是一个描述", "试一下")
        assert 1

    def test_abc_002(self):
        allure.attach("这是一个描述", "试一下")
        assert 0

# class Test_Abc:
#     @allure.step(title="第一个测试")
#     @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
#     def test_abc_001(self):
#         allure.attach("这是一个描述", "试一下")
#         assert 0
#
#     @allure.issue("http://www.163.com")
#     @pytest.allure.testcase('http://www.baidu.com/test_001')
#     @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
#     def test_abc_002(self):
#         allure.attach("这是一个描述", "试一下")
#         assert 0
