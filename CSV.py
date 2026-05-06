import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    # Fetch information from the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: collecting product names and prices
    items = []
    
    # Target elements with class 'product-card'
    for product in soup.find_all('div', class_='product-card'):
        name = product.find('h2').text
        price = product.find('span', class_='price').text
        items.append({'Product Name': name, 'Price': price})

    # Convert to Excel (CSV)
    df = pd.DataFrame(items)
    df.to_csv('scraped_data.csv', index=False)
    print("Data successfully saved to scraped_data.csv")

# Usage
# scrape_data('https://example-shop.com')