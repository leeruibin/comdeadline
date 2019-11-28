### 会议爬虫
### 抓取会议信息
####################   爬虫抓取数据代码段
import requests
import json
from bs4 import BeautifulSoup

def get_ID(url,conf_name):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')
    div = soup.find('div',{"id":"yw2"})
    tbody = div.find('tbody')
    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        if tds[3].text != conf_name:
            continue
        ccf_class = tds[0].text
        abbr = tds[3].text
        full = tds[4].text
        paper_date = tds[5].text
        info_date = tds[6].text
        hold_date = tds[7].text
        tmp = tds[4].find('a')
        id = tmp['href'].split('/')[-1]
        return [ccf_class,abbr,full,paper_date,info_date,hold_date,id]
    return 0

def get_info(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find('div',{"id":"yw0"})
    div = div.find('div',{"align":"center"})
    full = div.find('h5').text
    url = div.find('a').text
    table = div.find('table')
    info = {}
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        name = tds[0].text.replace(':','')
        info[name] = tds[1].text
    pre = soup.find('pre')
    call_for_paper = pre.text
    return [full,url,info,call_for_paper]

def get_all_info(namelist):
    result = {}
    search_url = "https://www.myhuiban.com/search?SearchForm%5Bkey%5D={}"
    info_url = "https://www.myhuiban.com/conference/{}"  # 可以选择语言参数
    for conf_name in namelist:
        sim_info = get_ID(search_url.format(conf_name), conf_name)
        if sim_info is not 0:
            ID = sim_info[-1]
            detail_info = get_info(info_url.format(ID))
            result[conf_name] = [sim_info, detail_info]
        print("########finished:{}###########".format(conf_name))
    return result

def update_conf():
    conf_name_path = './static/data/conference_list.txt'
    names = []
    with open(conf_name_path,'r') as f:
        for line in f.readlines():
            names.append(line.replace('\n',''))
    result = get_all_info(namelist=names)
    print(result)
    with open('./static/data/conf_info.json','w') as f:
        # string = json.dump(str(result),f)
        f.write(json.dumps(result))





