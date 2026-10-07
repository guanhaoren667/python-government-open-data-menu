import requests
#新北市機車定檢站名單(站號、站名、電話、地址)
#目標網址:https://data.ntpc.gov.tw/api/datasets/d24fd22c-671d-4d01-b04d-6cc7328d7530/json?page=0&size=1000

def api_06():
    url = "https://data.ntpc.gov.tw/api/datasets/d24fd22c-671d-4d01-b04d-6cc7328d7530/json?page=0&size=1000"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data[:200]:#店數太多、超過600間，故取其中200間做顯示
        code = row["station number"]
        name = row["name of scheduled inspection station"]
        Tel = row["telephone"]
        zipcode = row["postal code"]
        address = row["address"]
        
        print("-----")
        print(f"定檢站代碼: {code}")
        print(f"定檢站站名: {name}")
        print(f"連絡電話: {Tel}")
        print(f"郵遞區號: {zipcode}")
        print(f"地址: {address}")        