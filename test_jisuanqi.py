
import pytest
import yaml
from test_pytest.ZhangNan01.jisuanqi import Calculator

class TestCalc:

    # 测试add函数
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,get_datas):
        result = None
        try:
        # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_datas[0], get_datas[1])
        # 判断result结果是否等于期望的值
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == get_datas[2]

    @pytest.mark.run(order=3)
    def test_sub(self, get_calc, get_datas1):
        # 调用add函数,返回的结果保存在result里面
        result = get_calc.sub(get_datas1[0], get_datas1[1])
        # 判断result结果是否等于期望的值
        assert result == get_datas1[2]

    @pytest.mark.run(order=4)
    def test_mul(self, get_calc, get_datas2):
        # 调用add函数,返回的结果保存在result里面
        result = get_calc.mul(get_datas2[0], get_datas2[1])
        # 判断result结果是否等于期望的值
        assert result == get_datas2[2]

    @pytest.mark.run(order=2)
    def test_div(self, get_calc, get_datas3):
        # 调用add函数,返回的结果保存在result里面
        try:
            result = get_calc.div(get_datas3[0], get_datas3[1])
        # 判断result结果是否等于期望的值
            assert result == get_datas3[2]
        except Exception as e:
            print(e)





