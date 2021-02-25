import pytest
import os
from test_pytest import ZhangNan01
from test_pytest.ZhangNan01.jisuanqi import Calculator
import yaml
yaml_file_path=os.path.dirname(__file__) + "/canshu.yml"

@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = ZhangNan01.jisuanqi.Calculator()
    return calc



with open("./canshu.yml") as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["adddatas"]

    sub_datas = datas["subdatas"]

    mul_datas = datas["muldatas"]

    div_datas = datas["divdatas"]

    cal_ids = datas["calids"]


@pytest.fixture(params=add_datas,ids=cal_ids)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=sub_datas,ids=cal_ids)
def get_datas1(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas,ids=cal_ids)
def get_datas2(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=div_datas,ids=cal_ids)
def get_datas3(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


