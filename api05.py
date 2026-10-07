import requests
#新竹市預防接種合約院所名冊
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/213/564bbfbe-8f9e-40ec-9187-90826100b709.json?1140623164503
def api_05():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/213/564bbfbe-8f9e-40ec-9187-90826100b709.json?1140623164503"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        name = row['合約醫療院所名稱']
        code = row['十碼章']
        Tel = row['電話']
        address = row['地址']
        print("-----")    
        print(f"醫療院所名稱: {name}")
        print(f"醫療機構代碼: {code}")
        print(f"電話: {Tel}")
        print(f"地址: {address}")