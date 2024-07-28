import requests
from bs4 import BeautifulSoup

# URL of the webpage
url_migros = "https://www.migros.com.tr/icecek-c-6"
url_sok = "https://www.sokmarket.com.tr/"

# Send a request to fetch the content of the webpage
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url_sok, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    webpage = response.content
    
    # Parse the webpage content
    soup = BeautifulSoup(webpage, "html.parser")

    # Find all product containers (adjust the selector based on the page structure)
    product_containers = soup.find_all("div")
    
    # Loop through the product containers and extract the name and price
    for container in product_containers:
        # sok_market icin gecerli
        name = container.find("h2", class_="CProductCard-module_title__u8bMW")
        price = container.find("span", class_="CPriceBox-module_price__bYk-c")

        if name and price:
            name_text = name.get_text(strip=True)
            price_text = price.get_text(strip=True)
            price_float = float(price_text[:-1].replace(',','.'))
            print(f"Product: {name_text}, Price: {price_text}  -  {str(price_float)}")

                  
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
