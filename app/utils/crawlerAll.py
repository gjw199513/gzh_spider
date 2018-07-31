# -*- coding: utf-8 -*-
import json
import logging
import time

from app.models.models import GzhArticle
from app.utils import utils
import requests
from app import db
from app.config import settings

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class WeiXinCrawler:
    def crawl(self, offset=0):
        """
        爬取更多文章
        :return:
        """
        url = settings.url.format(offset=offset)  # appmsg_token 也是临时的
        headers = settings.headers

        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            msg_list = msg_list.replace("\/", "/")
            data = json.loads(msg_list)
            msg_list = data.get("list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
            for msg in msg_list:
                p_date = msg.get("comm_msg_info").get("datetime")
                msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
                if msg_info:
                    multi_msg_info = msg_info.get("multi_app_msg_item_list")
                    for msg_item in multi_msg_info:
                        time_array = time.localtime(p_date)
                        publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                        r = GzhArticle(
                            title=msg_item["title"],
                            author=msg_item["author"],
                            img_url=msg_item["cover"],
                            content_url=msg_item["content_url"],
                            publish_time=publish_time
                        )
                        db.session.add(r)
            # 递归调用
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                next_offset = result.get("next_offset")
                time.sleep(2)
                self.crawl(next_offset)
            db.session.commit()
        else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
            logger.error("无法正确获取内容，请重新从Fiddler获取请求参数和请求头")
            exit()


if __name__ == '__main__':
    crawler = WeiXinCrawler()
    crawler.crawl()