import requests

# Extracted from the JSON
collection_ids = ["183601", "180933", "134754", "134068", "130673", "171241"]
store_id = "1062416"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.swiggy.com/instamart",
    "Origin": "https://www.swiggy.com"
}

for cid in collection_ids:
    print(f"\n📦 Fetching products for collectionId: {cid}")
    
    url = f"https://www.swiggy.com/api/instamart/storeitemcollectionv2?collectionId={cid}&storeId={store_id}"
    
    response = requests.get(url, headers=headers)

    print(f"🔍 Status Code: {response.status_code}")
    print("🔍 Raw Response Text (preview):")
    print(response.text[:300])  # Print first 300 chars to see what you got

    if response.status_code == 200:
        if not response.text.strip():
            print("⚠️ Empty response body.")
            continue
        try:
            data = response.json()

            cards = data.get("data", {}).get("cards", [])

            if not cards:
                print("⚠️ No products found in response.")
                continue

            for card in cards:
                product = card.get("card", {}).get("info", {})
                name = product.get("name", "N/A")
                price = product.get("price", "N/A")
                print(f"🛒 {name} | ₹{price/100 if isinstance(price, int) else price}")
        
        except Exception as e:
            print(f"❌ Error parsing JSON for {cid}: {e}")
    else:
        
        print(f"❌ Failed to fetch collectionId {cid}.")
