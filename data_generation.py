import pandas as pd
import random
from faker import Faker

fake = Faker('pl_PL')

CATEGORIES = {
    "Food": ["ZABKA", "BIEDRONKA", "LIDL", "KAUFLAND", "MCDONALDS", "KFC", "BAKERY", "CARREFOUR"],
    "Transport": ["PKP INTERCITY", "UBER", "BOLT", "ORLEN", "BP", "MPK", "KOLEJE MAZ", "SHELL"],
    "Entertainment": ["NETFLIX", "SPOTIFY", "CINEMA CITY", "MULTIKINO", "STEAM", "PLAYSTATION"],
    "Healthcare": ["PHARMACY", "DOZ", "ZIKO", "LUXMED", "MEDICOVER", "ROSSMANN"],
    "Bills": ["PGE", "TAURON", "PGNIG", "UPC", "ORANGE", "PLAY", "T-MOBILE", "WATER_UTILITY"]
}

PREFIXES = ["BLIK", "CARD", "TRANSFER", "PURCHASE", "PAYMENT", "POS"]
CITIES = ["WAW", "KRAKOW", "GDANSK", "POZ", "WROC"]

def generate_dirty_title(category):
    
    merchant = random.choice(CATEGORIES[category])
    
    if random.random() > 0.7 and len(merchant) > 4:  
        cut_index = random.randint(4, len(merchant))
        merchant = merchant[:cut_index]
        
    components = []
    
    if random.random() > 0.4:
        components.append(random.choice(PREFIXES))
        
    components.append(merchant)
    
    if random.random() > 0.5:
        components.append(random.choice(CITIES))
        
    if random.random() > 0.2:
        noise = f"Z{random.randint(10, 9999)} {fake.lexify(text='????').upper()}"
        components.append(noise)
        
    if random.random() > 0.5:
        date_str = fake.date_this_year().strftime("%d-%m")
        components.append(date_str)
        
    random.shuffle(components)
    
    return " ".join(components)

data = []

for _ in range(1000): 
    
    category = random.choices(
        list(CATEGORIES.keys()), 
        weights=[40, 20, 15, 10, 15], 
        k=1
    )[0]
    
    title = generate_dirty_title(category)
    data.append({"transfer_title": title, "category": category})

df = pd.DataFrame(data)

print(df.sample(10))
df.to_csv("sample_data.csv", index=False, encoding='utf-8')