from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

coin_types = {
    "TRY": "土耳其里拉",
    "HKD": "港币",
    "USD": "美元",
    "CHF": "瑞士法郎",
    "DEM": "德国马克",
    "FRF": "法国法郎",
    "SGD": "新加坡元",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "JPY": "日元",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "EUR": "欧元",
    "MOP": "澳门元",
    "PHP": "菲律宾比索",
    "THB": "泰国铢",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "RUB": "卢布",
    "MYR": "林吉特",
    "TWD": "新台币",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "FIM": "芬兰马克",
    "INR": "印度卢比",
    "IDR": "印尼卢比",
    "BRL": "巴西里亚尔",
    "AED": "阿联酋迪拉姆",
    "ZAR": "南非兰特",
    "SAR": "沙特里亚尔"
}


def get_exchange_rate(date, currency_code):
    # configure webdriver
    options = Options()
    options.headless = True  # hide GUI
    options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
    options.add_argument("start-maximized")  # ensure window is full-screen

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.boc.cn/sourcedb/whpj/")
    
    # 选择起始日期
    start_date_input = driver.find_element(By.NAME, "erectDate")
    start_date_input.clear()
    start_date_input.send_keys(date)

    # 选择结束日期
    end_date_input = driver.find_element(By.NAME, "nothing")
    end_date_input.clear()
    end_date_input.send_keys(date)

    # 选择货币
    currency_input = driver.find_element(By.NAME, "pjname")
    currency_input.send_keys(coin_types[currency_code])

    # 点击查询按钮
    driver.implicitly_wait(5)
    query_button = driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
    query_button.click()
    time.sleep(5)

    # 获取现汇卖出价
    exchange_rate = driver.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text

    # 关闭浏览器
    driver.quit()
    
    return exchange_rate

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2]

    try:
        exchange_rate = get_exchange_rate(date, currency_code)
        print(f"{date} {currency_code}: {exchange_rate}")

        # 将数据保存到result.txt文件中
        with open("result.txt", "w") as f:
            f.write(f"{date} {currency_code}: {exchange_rate}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()