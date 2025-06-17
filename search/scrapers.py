import requests #send https requests (get, post)
import base64 # Encodes your credentials to Base64 (required by eBay)
import os #access environment variables
import json #handles json data
from dotenv import load_dotenv
load_dotenv() # Loads variables from a .env file into the environment

# STEP 1: Fetch the eBay Production OAuth token
def get_ebay_token():
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope",
    }

    response = requests.post("https://api.ebay.com/identity/v1/oauth2/token", headers=headers, data=data)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("OAuth error:", response.status_code, response.text)
        return None

# STEP 2: Search for a product using Browse API
def search_ebay(query, marketplace_id):
    access_token = get_ebay_token()
    if not access_token:
        return [], []
    
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }

    endpoint = f"https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit=50"
    response = requests.get(endpoint, headers=headers)

    if response.status_code != 200:
        print("eBay API error:", response.status_code, response.text)
        return [], []

    data = response.json()
    items = data.get("itemSummaries", [])

    results = []
    for item in items:
        title = item.get("title", "")
        price = item.get("price", {}).get("value")
        url = item.get("itemWebUrl", "")
        seller_info = item.get("seller", {})  
        seller_rating = seller_info.get("feedbackPercentage", 0.0)
        seller_name = seller_info.get("username", "Unknown")



        if title and price and url:
            results.append({
                "title": title,
                "price": float(price),
                "url": url,
                "rating": float(seller_rating),  # Seller's feedback percentage
                "seller_name": seller_name,
            })

    # Sort two ways
    cheapest = sorted(results, key=lambda x: x["price"]) #sort using price
    best_reviewed = sorted(results, key=lambda x: x["rating"], reverse=True) #sort using rating from greatest to least

    return cheapest, best_reviewed
