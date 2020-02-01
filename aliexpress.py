import requests
from lxml import html
from selenium import webdriver
import re
import urllib
import time

f = open('aliexpress.csv','w')
f.write('product_url,title,price,img_url,shipping_price,shipping_info')

Url = 'https://www.aliexpress.com/category/1420/tools.html?spm=a2g0o.home.113.3.650c2145ANssXM&site=glo&shipCountry=BR&isrefine=y&shipFromCountry=BR'
try:
    driver.find_element_by_xpath('//*[@class="next-dialog next-closeable ui-newuser-layer-dialog"]/a').click()
    time.sleep(5)
except:
    pass
driver = webdriver.Chrome('/home/administrator/Downloads/ailexpress/chromedriver')
driver.get(Url)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('lijinho@yandex.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('kgsjhj')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()
time.sleep(30)
try:
    driver.find_element_by_xpath('//*[@class="next-dialog next-closeable ui-newuser-layer-dialog"]/a').click()
    time.sleep(5)
except:
    pass
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[3]/button[1]').click()
# driver.get(Url)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="switcher-info"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="nav-global"]/div[4]/div/div/div/div[1]/div/a[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="nav-global"]/div[4]/div/div/div/div[1]/div/div[1]/ul/li[31]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="nav-global"]/div[4]/div/div/div/div[2]/div/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="nav-global"]/div[4]/div/div/div/div[2]/div/ul/li[1]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="nav-global"]/div[4]/div/div/div/div[4]/button').click()

driver.execute_script("window.scrollTo(5000, 5200);")
time.sleep(2)
driver.execute_script("window.scrollTo(5200, 5400);")
time.sleep(2)
driver.execute_script("window.scrollTo(5400, 5600);")
time.sleep(2)
driver.execute_script("window.scrollTo(5600, 5800);")
time.sleep(2)
driver.execute_script("window.scrollTo(5800, 6000);")
time.sleep(2)
driver.execute_script("window.scrollTo(6000, 6200);")
time.sleep(2)
driver.execute_script("window.scrollTo(6200, 6400);")
time.sleep(2)
driver.execute_script("window.scrollTo(6400, 6600);")
time.sleep(2)
driver.execute_script("window.scrollTo(6600, 6800);")
time.sleep(2)
driver.execute_script("window.scrollTo(6800, 7000);")
time.sleep(2)
driver.execute_script("window.scrollTo(7000, 7200);")
time.sleep(2)
driver.execute_script("window.scrollTo(7200, 7400);")
time.sleep(2)
driver.execute_script("window.scrollTo(7400, 7600);")
time.sleep(2)
driver.execute_script("window.scrollTo(7600, 7800);")
time.sleep(2)
driver.execute_script("window.scrollTo(7800, 8000);")
time.sleep(2)
driver.execute_script("window.scrollTo(8000, 8200);")
time.sleep(2)
driver.execute_script("window.scrollTo(8200, 8400);")
time.sleep(2)
driver.execute_script("window.scrollTo(8400, 8600);")
time.sleep(2)
driver.execute_script("window.scrollTo(8600, 8800);")
time.sleep(2)
driver.execute_script("window.scrollTo(8800, 9000);")
time.sleep(2)
driver.execute_script("window.scrollTo(9000, 9200);")
time.sleep(2)
driver.execute_script("window.scrollTo(9200, 9400);")
time.sleep(2)
driver.execute_script("window.scrollTo(9400, 9600);")
time.sleep(2)
driver.execute_script("window.scrollTo(9600, 9800);")
time.sleep(2)
driver.execute_script("window.scrollTo(9800, 10000);")
time.sleep(2)
driver.execute_script("window.scrollTo(10000, 10200);")
time.sleep(2)
driver.execute_script("window.scrollTo(10200, 10400);")
time.sleep(2)
driver.execute_script("window.scrollTo(10400, 10600);")
time.sleep(2)
driver.execute_script("window.scrollTo(10600, 10800);")
time.sleep(2)
driver.execute_script("window.scrollTo(10800, 11000);")
time.sleep(2)
driver.execute_script("window.scrollTo(11000, 11200);")
time.sleep(2)
driver.execute_script("window.scrollTo(11200, 11400);")
time.sleep(2)
driver.execute_script("window.scrollTo(11400, 11600);")
time.sleep(2)
driver.execute_script("window.scrollTo(11600, 11800);")
time.sleep(2)
driver.execute_script("window.scrollTo(11800, 12000);")
time.sleep(2)
driver.execute_script("window.scrollTo(12000, 12200);")
time.sleep(2)
driver.execute_script("window.scrollTo(12200, 12400);")
time.sleep(2)
driver.execute_script("window.scrollTo(12400, 12600);")
time.sleep(2)
driver.execute_script("window.scrollTo(12600, 12800);")
time.sleep(2)

ALl_main_data = []

i = 0

first = True
next = True
while i <= 14:
    try:
        i = i + 1
        if first:
            respose = html.fromstring(driver.page_source)
            all_link = respose.xpath('//*[@class="list-items"]/li')
            first = False
        else:

            try:
                time.sleep(5)
                try:
                    time.sleep(2)
                    driver.find_element_by_xpath(
                        '//*[@class="next-dialog next-closeable ui-newuser-layer-dialog"]/a').click()
                    time.sleep(2)
                except:
                    pass
                driver.find_element_by_xpath('//*[@class="next-btn next-medium next-btn-normal next-pagination-item next-next"]').click()
                driver.execute_script("window.scrollTo(0, 200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(200, 400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(400, 600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(600, 800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(800, 1000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(1000, 1200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(1200, 1400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(1400, 1600);")

                time.sleep(2)
                driver.execute_script("window.scrollTo(3800, 4000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(4000, 4200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(4200, 4400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(4400, 4600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(4600, 4800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(4800, 5000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(5000, 5200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(5200, 5400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(5400, 5600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(5600, 5800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(5800, 6000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(6000, 6200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(6200, 6400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(6400, 6600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(6600, 6800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(6800, 7000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(7000, 7200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(7200, 7400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(7400, 7600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(7600, 7800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(7800, 8000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(8000, 8200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(8200, 8400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(8400, 8600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(8600, 8800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(8800, 9000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(9000, 9200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(9200, 9400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(9400, 9600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(9600, 9800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(9800, 10000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(10000, 10200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(10200, 10400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(10400, 10600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(10600, 10800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(10800, 11000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(11000, 11200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(11200, 11400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(11400, 11600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(11600, 11800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(11800, 12000);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(12000, 12200);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(12200, 12400);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(12400, 12600);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(12600, 12800);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(12800, 13000);")
                time.sleep(5)
                respose = html.fromstring(driver.page_source)
                all_link = respose.xpath('//*[@class="list-items"]/li')
            except:
                next = False
                all_link = []

        for data in all_link:
            try:
                try:
                    product_url = data.xpath('.//a[@class="item-title"]/@href')[0]
                except:
                    product_url = ''

                try:
                    title = data.xpath('.//a[@class="item-title"]/text()')[0]
                except:
                    title = ''
                print(title)
                try:
                    price = data.xpath('.//span[@class="price-current"]/text()')[0]
                except:
                    price = ''
                try:
                    img_url = data.xpath('.//img[@class="item-img"]/@src')[0]
                except:
                    img_url = ''
              
                try:
                    shipping_price = data.xpath('.//span[@class="shipping-value"]/text()')[0]
                except:
                    shipping_price = ''
                shipping_info = 'to Brazil via SF eParcel'
                if product_url and title:
                    ALl_main_data.append({'product_url': str(product_url), 'title': str(title), 'price': str(price), 'img_url': str(img_url), 'shipping_price': str(shipping_price), 'shipping_info': str(shipping_info) })
                   ite(str(product_url)+','+str(title)+','+str(price)+','+str(img_url)+','+str(shipping_price)+','+str(shipping_info))
            except Exception as e:
                print(e)


    except Exception as e:
        print(e)

for data in ALl_main_data:
    driver.get('https:'+data['product_url'])
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@class="next-dialog next-closeable ui-newuser-layer-dialog"]/a').click()
        time.sleep(5)
    except:
        pass

    try:
        driver.find_element_by_xpath('//*[@class="sku-property-text"]//*[contains(text(),"Brazil")]').click()
        time.sleep(2)
    except:
        pass

    for image_link in driver.find_elements_by_xpath('//*[@class="sku-wrap"]/div[2]/ul/li/div/img'):
        try:
            try:
                image_link.click()
            except:
                pass
            time.sleep(4)
            imge = driver.find_element_by_xpath('//*[@class="magnifier-image"]').get_attribute("src")
            price = driver.find_element_by_xpath('//*[@class="product-price-value"]').text
            print(imge)

            print(price)
            f.write('\n')
            f.write(str(data['product_url'])+','+str(data['title'])+','+str(price)+','+str(imge)+','+str(data['shipping_price'])+','+str(data['shipping_info']))
        except:
            pass


f.close()
driver.close()





