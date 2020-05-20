"""
参考:
文档打开类型标识符（r, r+ ...）:https://www.runoob.com/python/file-methods.html
"""
import json

with open('config.json', 'w') as config:
    d = { "test1": 'a', "test2": 'b' }
    config.write(json.dumps(d))

with open('config.json') as config:
    d = json.load(config)
    print(d)

with open("config.json", 'r') as config:
    d = json.loads(config.read())
    print(d)