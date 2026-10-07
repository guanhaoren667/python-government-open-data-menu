import requests
#新竹市警察局測速照相固定桿設置地點概述
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/156/41121ffc-4357-488a-b14e-9e51f0d7aa74.json?1150904114142

def api_08():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/156/41121ffc-4357-488a-b14e-9e51f0d7aa74.json?1150904114142"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:    
    
        location = row['地點']
        speed_limit = row['速限']
        longitude = row['經度']
        latitude = row['緯度']
           
        print("-----")
        print(f"地點: {location}")
        print(f"速限: {speed_limit}")
        print(f"經度: {longitude}")
        print(f"緯度: {latitude}") 