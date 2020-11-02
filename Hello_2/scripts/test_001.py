import allure, pytest

class Test_abc:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="我是测试001")
    def test_001(self):
        allure.attach("描述", "我在测试001里面")
        assert 1