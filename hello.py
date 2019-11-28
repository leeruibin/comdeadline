from flask import Flask,render_template, request

app = Flask(__name__)
import yaml
import json
import datetime
import conference_spider as CS
import journey_spider as JS
#数据获取 myhuiban

# TODO 抓取数据 https://www.myhuiban.com/
# def get_data():
#     # confYamlPath = "./templates/_data/conferences.yml"
#     # typeYamlPath = "./templates/_data/types.yml"
#     confJsonPath = "./static/data/conf_info.json"
#     jourJsonPath = "./static/data/journel_info.json"
#     typeYamlPath = "./static/data/types.yml"
#
#     site = {}
#     site['title'] = "comdeadline"
#     site['name'] = "Robin"
#     site['description'] = "The date time come from the https://www.myhuiban.com where we can not get the accurate time. So the actual deadline may differ from the display time. Please refer to the conference website for accurate hour time."
#     site['twitter_username'] = "Robin"
#     site['twitter_hashtag'] = "TODO"
#     site['github_username'] = "leeruibin"
#     site['github_repo'] = "comdeadline"
#     site['url'] = "comdeadline.cc"
#     site['domain'] = "comdeadline"
#     f = open(confYamlPath, 'r')
#     content = f.read()
#     data = yaml.load(content)
#     site['data'] = {}
#     site['data']['conferences'] = data
#     f = open(typeYamlPath, 'r')
#     content = f.read()
#     data = yaml.load(content)
#     site['data']['types'] = data
#     f.close()
#     return site

# TODO 抓取数据 https://www.myhuiban.com/
def get_data():
    dateformat = '%Y-%m-%d'
    right_now = datetime.datetime.utcnow().replace(
        microsecond=0).strftime(dateformat)
    confJsonPath = "./static/data/conf_info.json"
    jourJsonPath = "./static/data/journel_info.json"
    typeYamlPath = "./static/data/types.yml"

    site = {}
    site['title'] = "comdeadline"
    site['name'] = "Robin"
    site['description'] = "The date time come from the https://www.myhuiban.com where we can not get the accurate time. So the actual deadline may differ from the display time. Please refer to the conference website for accurate hour time."
    site['twitter_username'] = "Robin"
    site['twitter_hashtag'] = "TODO"
    site['github_username'] = "leeruibin"
    site['github_repo'] = "comdeadline"
    site['url'] = "comdeadline.cc"
    site['domain'] = "comdeadline"
    conf_data = ""
    with open(confJsonPath,'r') as f:
        conf_data = json.load(f)
    conf_data = sorted(conf_data.items(), key=lambda x: x[1][0][3])
    conf_data.sort(key=lambda x: x[1][0][3] < right_now)
    # conf_data = sorted(conf_data.items(), key=lambda x: x[1][0][3] < right_now)
    # f = open(confYamlPath, 'r')
    # content = f.read()
    # data = yaml.load(content)
    site['data'] = {}
    site['data']['conferences'] = conf_data
    jour_data = ""
    with open(jourJsonPath,'r') as f:
        jour_data = json.load(f)
    site['data']['journal'] = jour_data

    f = open(typeYamlPath, 'r')
    content = f.read()
    data = yaml.load(content)
    site['data']['types'] = data
    f.close()

    return site



@app.route('/')
def hello_world():
    data = get_data()
    return render_template("all.html", site=data)

@app.route('/all')
def test():
   data = get_data()
   return render_template("all.html", site=data)

@app.route('/single')
def demo():
    data = get_data()
    return render_template("single.html", site=data)

@app.route('/conference')
def conference():
    conf = {}
    conf['id'] = request.args.get('id')
    site = get_data()
    return render_template("single.html", site=site, conf_id=conf)

@app.route('/update')
def update_conf():
    # 通过爬虫更新会议与期刊列表信息
    CS.update_conf()
    JS.update_jour()
    return "Finish update"

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)