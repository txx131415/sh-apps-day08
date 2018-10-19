import allure, pytest

"""
    配置allure命令行工具 -- 不必须 会有点不支持
    1.解压allure-2.6.0压缩包
    2.进入到解压后文件夹bin目录
    3.赋值bin目录路径，添加到系统path环境变量里
    4.进入命令行 输入allure
    5.新建测试文件
    6.配置pytest命令行参数--alluredir report08
    7。执行测试脚本
    8.在report08目录上级去执行allure generate report08/ -o report08/html
    9。会在report08下生成html文件夹，进入文件夹用六拉你去打开index.html

"""


class Test_001:
    @allure.step(title="输入用户名")  # 步骤描述
    def input_name(self):
        # 点击登录/注册按钮
        allure.attach('登录/注册按钮', '我是测试点击登录/注册按钮的描述～～～')
        # 点击输入框
        allure.attach("输入框", '我是输入框描述～～')
        # 输入用户名
        allure.attach("用户名", '我是用户名的描述')
        pass

    @allure.step(title="输入密码")
    def input_passwd(self):
        pass

    @pytest.allure.severty(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="我是登陆测试方法")
    def test_001_1(self):
        # self.input_name()
        # self.input_passwd()
        assert False

    @pytest.allure.severty(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="我是登陆测试方法")
    def test_001_2(self):
        assert True

    @pytest.allure.severty(pytest.allure.severity_level.NORMAL)
    @allure.step(title="我是登陆测试方法")
    def test_001_2(self):
        assert True