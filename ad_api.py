# -*- coding: utf-8 -*-
import requests
import time
import json

# ssssss

print("hello")
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
    import urllib3
    urllib3.disable_warnings()

    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip,deflate, lzma, sdch",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    data = {
        'id': plan_id
    }
    url = 'https://itest.cmcm.com/api/p1_advert/%s/local/run' %(ad_type)
    print(url)
    r = requests.post(url, data=json.dumps(data), timeout=180, verify=False, headers=headers)
    print(r.text)


def ad_test_stop(plan_id, ad_type):
    import requests
    import ssl
    import urllib3
    urllib3.disable_warnings()
    ssl._create_default_https_context = ssl._create_unverified_context

    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        # "Accept-Encoding": "gzip,deflate, lzma, sdch",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    data = {
        'id': plan_id
    }
    url = 'https://itest.cmcm.com/api/p1_advert/%s/local/stop' %(ad_type)
    print(url)
    r = requests.post(url, data=json.dumps(data), timeout=180, verify=False, headers=headers)
    print(r.text)


def main():
    #ad_test_run(plan_id, ad_type[0])
    ad_test_stop(plan_id, ad_type[0])


if __name__ == '__main__':
    main()
