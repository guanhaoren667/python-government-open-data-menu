import requests
#新竹市火災及爆炸災害潛勢公開資料管制量30倍之公共危險物品製造儲存或處理場所
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/916/25180a85-4f65-40d3-8cb0-9f8c17878d6a.json?1150702185054

def api_01():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/916/25180a85-4f65-40d3-8cb0-9f8c17878d6a.json?1150702185054"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()

    #print(type(data))
    #print(len(data))
    #print(data[0])

    for row in data:
        ROCdate = row['民國年月日']
        locname = row['場所名稱']
        address = row['地址']
        Notes = row['說明']
        print("-----")
        print(f"民國年月日: {ROCdate}")
        print(f"場所名稱: {locname}")
        print(f"地址: {address}")
        print(f"說明: {Notes}")