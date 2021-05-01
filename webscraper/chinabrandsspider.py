from requests_html import HTMLSession
import csv

url = 'https://www.chinabrands.com/dropshipping-xiaomi.html?searchUrl=%2Fsearch%2Fkeywords-notice.html&cat_id='

session = HTMLSession()

response = session.get(url)

file = open('chinabrands.csv','w')
writer = csv.writer(file)

writer.writerow(['Link','Name', 'Price'])

response.html.render(sleep=1)

print(response.status_code)

notFoundStr = 'Not Found'

products = response.html.xpath('//*[@id="pro-list"]/ul', first=True)

for item in products.absolute_links:
    product_response = session.get(item) #Gets all the links for the products and goes to the ur
    link = str(item)
    product_response.html.render(sleep=0.2)
    if(product_response.html.find('h3.goods-title.f18.mb15',first=True)):
        name = product_response.html.find('h3.goods-title.f18.mb15',first=True).text 
    else:
        name = notFoundStr

    if(product_response.html.find('span.my_shop_price.fb', first=True)):
        price = product_response.html.find('span.my_shop_price.fb', first=True).text
      
    else:
        price = notFoundStr





