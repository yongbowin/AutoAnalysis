#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 10/26/18 2:15 PM
# @Author: Yongbo Wang
# @Email : yonwang@redhat.com
# @File  : crawl_text.py
# @Desc  :
import requests

URL = 'http://beaker-archive.host.prod.eng.bos.redhat.com/beaker-logs/2018/10/30035/3003591/5994360/console.log'


class CrawlText:

    def __init__(self):
        pass

    def req_content(self):
        response = requests.get(URL)
        response.encoding = 'utf-8'
        text_list = response.text.split('\n')

        count = 0
        start_list = []
        mid_list = []
        end_list = []
        for line in text_list:
            if line.find("cut here") > 0:
                start_list.append(count)
            if line.find("Call Trace") > 0:
                mid_list.append(count)
            if line.find("end trace") > 0:
                end_list.append(count)

            count += 1

        if len(start_list) == len(mid_list) and len(mid_list) == len(end_list):
            if len(start_list) > 0 and len(mid_list) > 0 and len(end_list) > 0:
                for i in range(len(start_list)):
                    print("\n========================== Call Trace " + str(i+1) + " ========================")
                    sub_list = text_list[start_list[i]:(end_list[i] + 1)]
                    for j in sub_list:
                        print(j)
            else:
                print("============> No bug!")
        else:
            print("============> Need to check log by hand!")

        # print(start_list, mid_list, end_list)


if __name__ == '__main__':
    ct = CrawlText()
    ct.req_content()
