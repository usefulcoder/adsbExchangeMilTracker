from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

from time import sleep
focus_code = """test_coords = ol.proj.fromLonLat([-77.03637,38.89511000]); OLMap.setView(new ol.View({center: test_coords,zoom: 8}));"""


display = Display(visible=1, size=(800, 600))
display.start()
options = Options()
# options.add_argument("--headless=new")
options.add_argument('--user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
options.add_argument("--incognito")
options.add_argument("--nogpu")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1280")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')


driver=webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.get("https://globe.adsbexchange.com")


driver.execute_script(focus_code)
sleep(10)
planes = driver.execute_script("""return g.planes""")
driver.quit()
display.stop()
for plane in planes:
    if planes[plane]["military"]:
        print(planes[plane])
