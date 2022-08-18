#!/usr/bin/python3
# --*-- utf-8 --*--
# Author : "Emu" Lou 
# @Date : 2022.08.18 
# @Time : 18:22
# @Project_name : Note-of-Python-Carsh-Course-2nd-Edition
# @Name : python_repo_visual

import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

# import matplotlib.pyplot as plt

# 数据请求
url = "https://api.github.com/search/repositories?q=language:python&sort=star"
headers = {"accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()

repo_dicts = response_dict['items']
repo_names, repo_stars ,labels = [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    repo_stars.append(int(repo_dict['stargazers_count']))

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# 可视化
# 添加自定义工具提示
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': repo_stars,
    # 说明“hovertext”
    'hovertext':labels,
    # 透明度
    'opacity':0.6,
}]

my_layout = {
    "title": "most stars on Github",
    "xaxis": {'title': 'Repository'},
    "yaxis": {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="python_repos.html")

# plt.bar(range(len(repo_stars),repo_stars,tick_label= repo_names)
