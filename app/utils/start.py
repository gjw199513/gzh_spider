# coding:utf-8
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""
from __future__ import print_function

import time
from datetime import datetime
import schedule
import requests


from app.models.models import GzhArticle
from app.utils.ShowapiRequest import ShowapiRequest

# 请求示例 url 默认请求参数已经做URL编码
from app import db
from app.config import secure


def turn_url(url):
    r = ShowapiRequest("http://route.showapi.com/1456-1", "71245", "c95f0f43d8ed4896a49c7d188f89c4f9")
    r.addBodyPara("url", url)
    r.addBodyPara("account", "cs-teacher")
    res = r.post()
    res = res.json()
    if res["showapi_res_code"] == 0:
        return res["showapi_res_body"]["url"]
    else:
        return ""


def spider_gzh():
    url = "http://api01.bitspaceman.com:8000/post/weixin?uid=cs-teacher&range=d&apikey=" + secure.API_KEY
    headers = {
        "Accept-Encoding": "gzip",
        "Connection": "close"
    }
    r = requests.get(url, headers=headers)
    json_obj = r.json()
    if json_obj["retcode"] != "100002":
        data = json_obj["data"]
        for d in data:
            title = d["title"]
            author = d["writers"][0]["name"]
            img_url= d["coverUrls"]
            time_array = time.localtime(d["publishDate"])
            publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            content_url = turn_url(d["url"])
            if content_url == "":
                break

            article = GzhArticle(
                title=title,
                author=author,
                img_url=img_url,
                content_url=content_url,
                publish_time=publish_time
            )
            db.session.add(article)
        db.session.commit()


def test():
    print("test--------------"+datetime.now)


# if __name__ == "__main__":
    # spider_gzh()

schedule.every().day.at("10:30").do(spider_gzh)

while True:
    schedule.run_pending()
    time.sleep(1)