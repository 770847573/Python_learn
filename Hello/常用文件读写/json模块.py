#json 序列化： 将python中的列表或字典转化为字符串或json格式的字符串写入磁盘
#反序列化：将磁盘中的字符串或json字符串转化为python中的列表或字典对象
import json
info = {
    "name": "中国",
    "province": [{
        "name": "黑龙江",
        "cities": {
            "city": ["哈尔滨", "大庆"]
        }
    }, {
        "name": "广东",
        "cities": {
            "city": ["广州", "深圳", "珠海"]
        }
    }, {
        "name": "台湾",
        "cities": {
            "city": ["台北", "高雄"]
        }
    }, {
        "name": "新疆",
        "cities": {
            "city": ["乌鲁木齐"]
        }
    }]
}
#序列化：将字典或列表转换成Json字符串
json1 = json.dumps(info,ensure_ascii=False)
print(type(json1))
print(json1)
#反序列化：将json字符串转化成python中的列表或字典
print(json.loads(json1))

print("*" * 30)



#写入文件（序列化）:
with open(r"info.json","w",encoding="utf-8") as j1:
  json.dump(info,j1,ensure_ascii=False)
  print(j1)
#读取（反序列化）：将磁盘中的字符串转化成json
with open(r"info.json","r",encoding="utf-8") as j2:
    r_json = json.load(j2)
    print(r_json)

