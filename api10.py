import requests
#新竹市立案表演團體名冊
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/80/fef44490-8b50-42e2-8c4e-5b2172ed5e14.json?1140630195058

def api_10():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/80/fef44490-8b50-42e2-8c4e-5b2172ed5e14.json?1140630195058"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #resp = requests.get(url)
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        band_name = row['演藝團體名稱']
        leader = row['負責人']
        date_of_registration = row['立案時間日期']
        kind = row['表演類型']
        
        print("-----")
        print(f"演藝團體名稱: {band_name}")
        print(f"負責人: {leader}")
        print(f"立案日期: {date_of_registration}")
        print(f"表演類型: {kind}")