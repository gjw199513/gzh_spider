# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/7/30 22:48'

# 访问url
url = "https://mp.weixin.qq.com/mp/profile_ext?" \
      "action=getmsg" \
      "&__biz=MzI5NTA1MjcxMQ==" \
      "&f=json&offset=10&count=10" \
      "&is_ok=1&scene=124&uin=777&key=777" \
      "&pass_ticket=MQlrl%2Fcg4VhhAJxzaD2M5FTu5g6lDlp%2B%2BLzVwz5QTMjWrnlvv8aNXmjm0GsK3Gv%2B" \
      "&wxtoken=&appmsg_token=967_HacjkxlA3V77g1DbykVBAHLT2A0qfysIGmHf6A~~&x5=1" \
      "&f=json"  # appmsg_token 也是临时的

# 访问头信息
headers = """
        Host: mp.weixin.qq.com
        Connection: keep-alive
        X-Requested-With: XMLHttpRequest
        User-Agent: Mozilla/5.0 (Linux; Android 8.0; BKL-AL20 Build/HUAWEIBKL-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044203 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN
        Accept: */*
        Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzI5NTA1MjcxMQ==&scene=124&devicetype=android-26&version=26060739&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=MQlrl%2Fcg4VhhAJxzaD2M5FTu5g6lDlp%2B%2BLzVwz5QTMjWrnlvv8aNXmjm0GsK3Gv%2B&wx_header=1
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh-CN;q=0.8,en-US;q=0.6
        Cookie: wxuin=3677621543; devicetype=android-26; version=26060739; lang=zh_CN; pass_ticket=MQlrl/cg4VhhAJxzaD2M5FTu5g6lDlp++LzVwz5QTMjWrnlvv8aNXmjm0GsK3Gv+; wap_sid2=CKea0NkNElxwRjl0UENFeTkxQVdJZUNzeW5CQ3ZiNlhIQWdXTVBMb0dzcEdTTE5pQlpjeWJqQnpTMk9LY3VwczBYT1gxQmxjR2dDbHAtZ2kyYkMzYXdEdXBqSXhGc2NEQUFBfjCwwfzaBTgNQJVO
        Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.7&TBSVC=43610&CO=BK&COVC=044203&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= BKL-AL20 &RL=1080*2160&OS=8.0.0&API=26
        Q-GUID: 977aa2e517c7c2e249c2b73713b788cb
        Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
        """



