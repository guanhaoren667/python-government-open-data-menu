import requests
#新竹市代收稅款金融機構服務據點
#目標網址:https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/171/0a88ec35-6835-404f-b179-e9fef2b67047.json?1150730110311

def api_09():
    url = "https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/171/0a88ec35-6835-404f-b179-e9fef2b67047.json?1150730110311"
    resp = requests.get(url, verify=False, timeout=15)# 因資料來源的 SSL 憑證目前無法通過本機 Python 驗證，測試期間暫時關閉 HTTPS 憑證驗證。
    #print(resp)#確認回傳200
    data = resp.json()
    
    #print(type(data))
    #print(len(data))
    #print(data[0])
    
    for row in data:
        unit_name = row['單位名稱']
        branch_name = row['分行名稱']
        branch_code = row['金融機構代號']
        location = row['地址']    
        Tel = row['電話']
        
        print("-----")
        print(f"單位名稱: {unit_name}")
        print(f"分行名稱: {branch_name}")
        print(f"金融機構代號: {branch_code}")
        print(f"地址: {location}") 
        print(f"電話: {Tel}")