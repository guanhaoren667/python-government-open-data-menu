import requests
#新竹市各級工會團體組織名冊
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/225/3fe2936d-ac2d-4296-847a-baabb5b10d66.json?1150804110700

def api_07():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/225/3fe2936d-ac2d-4296-847a-baabb5b10d66.json?1150804110700"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        
        name = row['團體名稱']
        person_in_charge = row['負責人']
        Tel = row['聯絡電話']
        Mobile = row['行動號碼']
        address = row['聯絡地址']
        
        print("-----")
        print(f"團體名稱: {name}")
        print(f"負責人: {person_in_charge}")
        print(f"市內電話: {Tel or '（無資料）'}")
        print(f"行動電話: {Mobile or '（無資料）'}")
        print(f"地址: {address}")   