# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/7/30 22:15'
import html


def str_to_dict(headers):
    """
    将"Host: mp.weixin.qq.com"格式的字符串转换成字典类型
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


def sub_dict(d, keys):
    return {k: html.unescape(d[k]) for k in d if k in keys}