from requests_html import HTMLSession

#Number of Pages cant be found using the links in Aliexpress
url = 'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=chair&ltype=wholesale&SortType=default&page=1'

session = HTMLSession()

response = session.get(url)

response.html.render(sleep=1)

print(response.status_code)

products = response.html.xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul', first=True)

for item in products.absolute_links:
    product_response = session.get(item) #Gets all the links for the products and goes to the url
    print('\nLink: ' + item)
    product_response.html.render(sleep=0.2)
    if(product_response.html.find('h1.product-title-text',first=True)):
        print('Name: ' + product_response.html.find('h1.product-title-text',first=True).text)
    else:
        print('Name: Not Found')
    if(product_response.html.find('span.product-price-value',first=True)):
        print('Price:' + product_response.html.find('span.product-price-value',first=True).text)
    else:
        print('Price: Not Found')
    if(product_response.html.find('span.overview-rating-average',first=True)):
        print('Rating: ' + product_response.html.find('span.overview-rating-average',first=True).text )
        #print('Description: ' + product_response.html.find('span.product-price-value',first=True).text )
    else:
        print('Price: Not Found')
    if(product_response.html.find('span.product-reviewer-reviews.black-link',first=True)):
        print('Reviews: ' + product_response.html.find('span.product-reviewer-reviews.black-link',first=True).text + '\n')
    else:
        print('Reviews: Not Found\n')



