#!/usr/bin/python3
# --*-- utf-8 --*--
# Author : "Emu" Lou 
# @Date : 2022.08.18 
# @Time : 12:37
# @Project_name : Note-of-Python-Carsh-Course-2nd-Edition
# @Name : 123

# 使用API调用请求数据

import requests

# 执行api并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=star"
# 最新的Github API版本为第三版，因此通过指定header要求使用这个版本的API，再使用requests调用API
# HTTP Headers是HTTP请求和相应的核心，它承载了关于客户端浏览器，请求页面，服务器等相关的信息。
# https://kb.cnblogs.com/page/119118/
headers = {"accept": "application/vnd.github.v3+json"}
# 这个API返回JSON格式的信息，因此使用方法JSON()将这些信息转换为一个python字典，并将结果存在respomse_dict中
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

print(type(r))
# 将API相应赋值给一个变量
# 并将其json字典化
response_dict = r.json()
# 处理结果
print(response_dict["total_count"])
# 返回结果为：dict_keys(['total_count', 'incomplete_results', 'items'])
# 网页结构树最根部的三项
print("#############")

repo_dicts = response_dict["items"]
print(len(repo_dicts))

print("#############")
# 研究第一个仓库
first_repo_dict = repo_dicts[0]
print(len(first_repo_dict))
for key in sorted(first_repo_dict.keys()):
    print(key)

print("#############")
# 寻找要返回的键值对内容
print(f'Name:{first_repo_dict["name"]}')
# 查看字典下的子字典用【】的【】
print(f'Owner:{first_repo_dict["owner"]["login"]}')
print(f'ID:{first_repo_dict["owner"]["id"]}')
print(f'Stars:{first_repo_dict["stargazers_count"]}')
print(f'Created time:{first_repo_dict["created_at"]}')
print(f'Updated time:{first_repo_dict["updated_at"]}')

print("#############")
for repo_dict in repo_dicts:
    print("|||||")
    print(f'Name:{repo_dict["name"]}')
    print(f'Owner:{repo_dict["owner"]["login"]}')
    print(f'ID:{repo_dict["owner"]["id"]}')
    print(f'Stars:{repo_dict["stargazers_count"]}')
    print(f'Created time:{repo_dict["created_at"]}')
    print(f'Updated time:{repo_dict["updated_at"]}')
