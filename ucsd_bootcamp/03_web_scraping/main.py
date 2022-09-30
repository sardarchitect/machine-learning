from tokenize import maybe
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/p/pl?d=rtx'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "./products.csv"
f= open(filename, "w")
headers = "brand, product_name\n"
f.write(headers)

for container in containers:
    container_info = container.find("div", {"class":"item-info"})
    brand = container_info.div.a.img["title"]
    product_name = (container_info.findAll("a", {"class":"item-title"}))[0].text
    print(brand, "\n" ,product_name, "\n\n")
    f.write(brand+","+product_name.replace(",", "|")+"\n")

f.close()
