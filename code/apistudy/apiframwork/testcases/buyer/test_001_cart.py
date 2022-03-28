# !/usr/bin python3.8                                
# encoding: utf-8 -*-                            
# @author: ninghui_hiahia
# @Time: 2022/3/27  12:44 上午
import pytest

from api.buyer.cart import AddCartApi


class TestAddCart:
    test_data =  [
        ['必填参数均正确没有非必填字段',5173,   1,       200,'',''],
        ['产品已下架',               5875,   1,      500,'004','产品已下架'],
        ['产品不存在',              456665,  1,      500,'451','商品已失效，请刷新购物车'],
        ['购买数量超过库存',           5173, 99999999, 500,'451','商品库存已不足，不能购买。'],
        ['购买数量为0',               5173,  0,        400,'004','加入购物车数量必须大于0'],
        ['购买数量为负数',             5173,   -1,     400,'004','加入购物车数量必须大于0'],
        ['购买数量为空',               5173,  None,    400,'004','购买数量不能为空'],
        ['产品id为空',                None,      1,    400,'004','产品id不能为空']
    ]

    @pytest.mark.parametrize('casename,sku_id,num,expect_status_code,expect_busi_code,expect_message', test_data)
    def test_buy_now(self, casename, sku_id, num, expect_status_code, expect_busi_code, expect_message):

        add_cart=AddCartApi(sku_id=sku_id,num=num)
        resp=add_cart.send()

        status_code = resp.status_code
        assert status_code == expect_status_code
        print(resp.text)  # 由于响应信息可能为空，所以我们使用resp.text打印结果，因为空的字符串是无法使用resp.json()去获取的
        # 注意这个接口如果业务正常成功，那么响应信息是空的
        if status_code != 200:
            # 状态码不是200时，才进行响应信息的校验
            try:
                resp_json = resp.json()
            except:
                pass
            code = resp_json['code']
            # assert code == expect_busi_code
            pytest.assume(code == expect_busi_code)
            # 判断message的值是 商品已失效，请刷新购物车
            message = resp_json['message']
            # assert message == expect_message
            pytest.assume(message == expect_message)
        # if status_code == 200:
        #     # 从redis中获取数据并做校验
        #     uid = get_token  # get_token是个fixture，调用时他就相当于他的返回值，我们返回了uid
        #     # 格式化字符串时，如果字符串本身就有大括号，那么需要使用双大括号
        #     res = redis_util.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{uid}')
        #     res_list = javaobj.loads(res)  # 这是得到结果转换成python的列表
        #     # 业务上这个列表中，只会存储一个数据
        #     obj = res_list[0]  # 通过索引得到列表里的数据
        #     redis_num = obj.__getattribute__('num')  # 实际结果
        #     redis_skuId = obj.__getattribute__('skuId')  # 实际结果
        #     pytest.assume(redis_num == num)
        #     pytest.assume(redis_skuId == sku_id)
