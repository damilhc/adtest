# -*- coding: utf-8 -*-

import requests
import time
import json


def time_cost(func):
    def new_func(*args, **kargs):
        start = time.time()
        print("%s, {%s} start" %(time.strftime("%X", time.localtime()), func.__name__))
        res = func(*args, **kargs)
        print("%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("%.3fs taken for {%s}" % (time.time() - start, func.__name__))
        return res
    return new_func

plan_id = 70  # 测试计划 ID
ad_type = ('CheetahMobile', 'VIE', 'VPN')  # 广告类型


@time_cost
def ad_test_run(plan_id, ad_type):
    import ssl
    import requests

