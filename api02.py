import requests
#新竹市第22屆里長名冊(每年更新)
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/135/1fcbfae6-46d0-4b55-921a-e819c7df4cea.json?1150525160300
def api_02():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/135/1fcbfae6-46d0-4b55-921a-e819c7df4cea.json?1150525160300"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        term = row["屆別"]
        name = row["姓名"]
        title = row["職稱"]
        gender = row["性別"]
        village_name = row["里別"]
        address = row["通訊地址"]
        Tel = row["市內電話"]
        Mobile = row["行動電話"]
        print("-----")
        print(f"屆別: {term or '（無資料）'}")
        print(f"姓名: {name}")
        print(f"職稱: {title or '（無資料）'}")
        print(f"性別(1為男性2為女性): {gender or '（無資料）'}")
        print(f"里別: {village_name}")
        print(f"通訊地址: {address or '（無資料）'}")
        print(f"市內電話: {Tel or '（無資料）'}")
        print(f"行動電話: {Mobile or '（無資料）'}")