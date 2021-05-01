from requests_html import HTMLSession
import csv

#Number of Pages cant be found using the links in Aliexpress and cant go to next page using the Next button as only :before and :after is there in the 'Next' link
url = 'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=chair&ltype=wholesale&SortType=default&page=1'

session = HTMLSession()

response = session.get(url)

file = open('aliexpress.csv','w')
writer = csv.writer(file)

writer.writerow(['Link','Name', 'Price', 'Rating', 'Reviews'])

response.html.render(sleep=1)

print(response.status_code)

notFoundStr = 'Not Found'

products = response.html.xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul', first=True)

for item in products.absolute_links:
    product_response = session.get(item) #Gets all the links for the products and goes to the url
    link = str(item)
    product_response.html.render(sleep=0.2)
    if(product_response.html.find('h1.product-title-text',first=True)):
        name = product_response.html.find('h1.product-title-text',first=True).text 
    else:
        name = notFoundStr
    if(product_response.html.find('span.product-price-value',first=True)):
        price = product_response.html.find('span.product-price-value',first=True).text
    else:
        price = notFoundStr
    if(product_response.html.find('span.overview-rating-average',first=True)):
        rating = product_response.html.find('span.overview-rating-average',first=True).text 
        #print('Description: ' + product_response.html.find('span.product-price-value',first=True).text )
    else:
        rating = notFoundStr
    if(product_response.html.find('span.product-reviewer-reviews.black-link',first=True)):
        reviews = product_response.html.find('span.product-reviewer-reviews.black-link',first=True).text 
    else:
        reviews = notFoundStr


    writer.writerow([link,name,price,rating,reviews])


file.close()