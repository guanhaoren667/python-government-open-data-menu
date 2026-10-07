# 主選單系統：讓使用者選擇要查詢的政府開放資料 API
import urllib3 
# 暫時隱藏因 verify=False 產生的 HTTPS 憑證警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import api01#導入引用10支api功能
import api02
import api03
import api04
import api05
import api06
import api07
import api08
import api09
import api10

def menu_print():#建立一個方法，顯示主選單與 10 項 API 查詢功能
    print('"""""歡迎來到不正常人類研究中心大平台"""""')
    print('請輸入資訊代碼(請輸入阿拉伯數字)，來查詢您要的資料')
    print('0.*****離開此程式*****')
    print('1.新竹市火災及爆炸災害潛勢公開資料管制量30倍之公共危險物品製造儲存或處理場所')
    print('2.新竹市第22屆里長名冊(每年更新)')
    print('3.114學年度新竹市立國中小通訊資料')
    print('4.115年竹風藝文饗宴節目表')
    print('5.新竹市預防接種合約院所名冊')
    print('6.新北市機車定檢站名單(站號、站名、電話、地址)')
    print('7.新竹市各級工會團體組織名冊')
    print('8.新竹市警察局測速照相固定桿設置地點概述')
    print('9.新竹市代收稅款金融機構服務據點')
    print('10.新竹市立案表演團體名冊')

def main():#建立方法並呼叫menu，接收使用者輸入並執行對應的 API 查詢功能
    n = 0 #建立防呆機制
    while True: # 持續顯示主選單，直到使用者選擇離開或累積輸錯 3 次
        menu_print()
        menu_use=input('請輸入資訊代碼(請輸入阿拉伯數字)，來查詢您要的資料:')
        if menu_use == '1':
            print("\n" + "=" * 60)
            api01.api_01()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='2':
            print("\n" + "=" * 60)
            api02.api_02()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='3':
            print("\n" + "=" * 60)
            api03.api_03()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='4':
            print("\n" + "=" * 60)
            api04.api_04()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='5':
            print("\n" + "=" * 60)
            api05.api_05()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='6':
            print("\n" + "=" * 60)
            api06.api_06()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='7':
            print("\n" + "=" * 60)
            api07.api_07()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='8':
            print("\n" + "=" * 60)
            api08.api_08()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='9':
            print("\n" + "=" * 60)
            api09.api_09()
            print("=" * 60 + "\n")
            continue
        elif menu_use =='10':
            print("\n" + "=" * 60)
            api10.api_10()
            print("=" * 60 + "\n")
            continue
        elif menu_use == '0':
            print('\n')
            print('感謝使用!您將離開本系統~~~')
            print('\n')
            break
        else:
            n += 1 #建立錯誤機制判斷規則
            print("\n" + "=" * 60)
            if n < 3:
                print('*****無此資料代碼，請重新輸入*****')
                print("=" * 60 + "\n")
                continue
            else:
                print('*****您輸入錯誤次數過多，系統將自動離開*****')
                print("=" * 60 + "\n")
                break
                
if __name__ == '__main__':
    main()