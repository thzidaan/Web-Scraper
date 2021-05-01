# Web-Scraper

A Webscraper that is used to collect data i.e price and description from Amazon,Alibaba,Aliexpress and Chinabrands

# How to Run

## Clone the respository in your local machine

```
git clone https://github.com/thzidaan/Web-Scraper.git
```

## Start the Virtual Environemnt

```
cd Web-Scraper
```
```
source venv/bin/activate
```

## Or Install Dependencies on your local machine

```
pip3 install -r requirements.txt
```

### To Scrape Amazon

```
cd Web-Scraper/webscraper
```
```
scrapy crawl amazon -O amazon.csv
```

Here CSV extension specifies that the ouput file will be compatible with **Excel**

### To Scrape Alibaba

#### Install Docker 

```
sudo docker pull scrapinghub/splash
```

#### Run Docker Image

```
sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```
The port in the spider settings is configured to be on 8050. So if you decide to change it, make sure to change the port number in settings.py as well.

#### Run Alibaba Spider

```
cd Web-Scraper/webscraper
```
```
scrapy crawl alibaba -O alibaba.csv
```
Here CSV extension specifies that the ouput file will be compatible with **Excel**

### To Scrape Aliexpress

```
python aliexpressspider.py
```

Remember that the python that you are using should be from the virtual environment that you created or the interpretor that has all the dependencies installed. 

### To Scrape Chinabrands

```
python chinabrandsspider.py
```

Remember that the python that you are using should be from the virtual environment that you created or the interpretor that has all the dependencies installed. 