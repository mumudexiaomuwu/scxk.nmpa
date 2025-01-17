# 测试网站布局和数据组成以及反爬措施.
import requests
import json

citys = [
    "京",
    "津",
    "冀",
    "晋",
    "内",
    "辽",
    "吉",
    "黑",
    "沪",
    "苏",
    "浙",
    "皖",
    "闽",
    "赣",
    "鲁",
    "豫",
    "鄂",
    "湘",
    "粤",
    "桂",
    "琼",
    "川",
    "贵",
    "云",
    "渝",
    "藏",
    "陕",
    "甘",
    "青",
    "宁",
    "新",
    # "港",
    # "澳",
    # "台",
]

# 列表页的测试
list_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
page_num = 50
list_data = {
    "on": "true",
    "page": page_num,
    "pageSize": "15",
    "productName": "",
    "conditionType": "1",
    "applyname": "",
    "applysn": ""
}
response = requests.post(url=list_url, data=list_data)
print(" 页数为", page_num, "时的响应数据:", response.text)
exit()

num = 0
# 测试通过城市查询是否能返回正确条数的数据.
for i in citys:
    list_data = {
        "on": "true",
        "page": 1,
        "pageSize": "15",
        "productName": i,
        "conditionType": "1",
        "applyname": "",
        "applysn": ""
    }

    response = requests.post(url=list_url, data=list_data)
    total_count = response.json()["totalCount"]
    page_count = response.json()["pageCount"]
    # 测试有效的省份简称
    # if total_count == 0:
    #     print(i)

    if page_count > 50:
        print("总页数大于50的区域:", i)
    num += total_count

print(num)

fp = open("./result.json", "a")
