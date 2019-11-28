### 期刊爬虫
### 抓取期刊信息

import requests
import json
from bs4 import BeautifulSoup

# C级期刊中有一个会议 Networks

def get_ID(url,conf_name):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')
    div = soup.find('div',{"id":"yw5"})
    tbody = div.find('tbody')
    trs = tbody.find_all('tr')
    if len(trs) > 1:
        for tr in tbody.find_all('tr'):
            tds = tr.find_all('td')
            if tds[0].text == '':
                continue
            ccf_class = tds[0].text
            full_name = tds[1].text
            impact = tds[2].text
            publisher = tds[3].text
            ISSN = tds[4].text

            tmp = tds[1].find('a')
            id = tmp['href'].split('/')[-1]
            return [ccf_class,conf_name,full_name,impact,publisher,ISSN,id]
    else:
        tds = trs[0].find_all('td')
        ccf_class = tds[0].text
        full_name = tds[1].text
        impact = tds[2].text
        publisher = tds[3].text
        ISSN = tds[4].text

        tmp = tds[1].find('a')
        id = tmp['href'].split('/')[-1]
        return [ccf_class, conf_name, full_name, impact, publisher, ISSN, id]
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
        name = tds[0].text.replace(':', '')
        info[name] = tds[1].text
    pre = soup.find('pre')
    if hasattr(pre,'text'):
        call_for_paper = pre.text
    else:
        call_for_paper = ""
    return [full,url,info,call_for_paper]

def get_all_info(namelist):
    result = {}
    search_url = "https://www.myhuiban.com/search?SearchForm%5Bkey%5D={}"
    info_url = "https://www.myhuiban.com/journal/{}"  # 可以选择语言参数
    for conf_name in namelist:
        sim_info = get_ID(search_url.format(conf_name), conf_name)
        if sim_info is not 0:
            ID = sim_info[-1]
            detail_info = get_info(info_url.format(ID))
            result[conf_name] = [sim_info, detail_info]
        print("########finished:{}###########".format(conf_name))
    return result

def update_jour():
    ### 期刊抓取部分，部分期刊用简写无法搜索到结果
    conf_name_path = './static/data/journel_abbr_list.txt'
    names = []
    with open(conf_name_path,'r') as f:
        for line in f.readlines():
            names.append(line.replace('\n',''))
    ### 使用全称获取会议结果
    conf_name_path = './static/data/journel_full_list.txt'
    with open(conf_name_path,'r') as f:
        for line in f.readlines():
            names.append(line.replace('\n',''))

    result = get_all_info(namelist=names)
    print(result)

    with open('./static/data/journel_info.json','w') as f:
        # string = json.dump(str(result),f)
        f.write(json.dumps(result))
