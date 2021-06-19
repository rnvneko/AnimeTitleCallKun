# coding: utf-8
import requests
import json

# print("指定された年・クールのアニメを表示します。")
# year = input("西暦（YYYY）※半角※：")
# cours = input("クール（1.冬, 2.春, 3.夏, 4.秋, 5.通年）：")

def titlecall(year, cours):
    api_url_yearcours = "http://api.moemoe.tokyo/anime/v1/master/" + year + "/" + cours
    # クール指定まであった場合のURL

    api_url_yearonly = "http://api.moemoe.tokyo/anime/v1/master/" + year
    # クール指定がなかった場合URL

    if cours == "5":
        result = requests.get(api_url_yearonly).text
        # jsonをテキストデータで取ってくる
        # print(result)
        data = json.loads(result)
        return data

    else:
        result = requests.get(api_url_yearcours).text
        # print(result)
        data = json.loads(result)
        return data




