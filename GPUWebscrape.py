import requests
from bs4 import BeautifulSoup

url = 'https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia-graphics-cards?page=1'
GPUNames_list = []
GPUprices_list = []

OC_r = requests.get(url)
OC_soup = BeautifulSoup(OC_r.text, 'html.parser')


listing = OC_soup.findAll('div', {'class': 'col position-relative'})
pricing = OC_soup.findAll('div', {'class':'price price--sale-colored h4 mb-0 mt-2 d-inline-block'})

i=0
for list in listing:
    title = list.findAll('a', {'class':'text-inherit text-decoration-none js-gtm-product-link'})[0].text
    GPUNames_list.insert(i,title)
    i+=1

j=0
for price in OC_soup.findAll('span', {'class':'price price--sale-colored h4 mb-0 mt-2 d-inline-block'}):
    pricelist = price.text
    GPUprices_list.insert(j, pricelist)
    j+=1

GPUInfo=[]
i=0
for i in range(len(GPUprices_list)):
    temp = GPUNames_list[i],GPUprices_list[i]
    GPUInfo.insert(i,temp)
    i+=1
print


def message(a,b):
    i=0
    for amount in b:
        new_message = a[i],b[i].strip()
        i+=1
        print(new_message)
message(GPUNames_list, GPUprices_list)
