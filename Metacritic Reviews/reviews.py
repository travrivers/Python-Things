import requests
from bs4 import BeautifulSoup

def get_reviews():
    try:
        reviews = []
        media = input("What do you want look up reviews for?").split(" ")
        media2 = "%20".join([str(x) for x in media])   
        url = f'https://www.metacritic.com/search/all/{media2}/results'
        response = requests.get(
        url, 
        headers={"Accept":"html", 
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"},
        params={"term": media})
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup.ul.find_all("li", recursive=True): 
            reviews.append({
                    "Title":tag.find(class_="product_title basic_stat").get_text(strip=True),
                    "Media":tag.find("p").get_text(strip=True),
                    "Score":tag.find("span").get_text(strip=True)             

                })
        print("Here are your results:\n")
        num = 0
        while num < len(reviews):
            print(f"{num+1}. {reviews[num]['Title']}, a {reviews[num]['Media']}, has a Metacritic score of {reviews[num]['Score']}")
            num += 1
        again = input("Would you like to look up anything else?").lower()
            
        if again[0] == 'y':
            get_reviews()
        elif again[0] != 'y':
            print("Have a good day yo")
        
    except:
        print("Ugh, something happened. Try another title.")

        again = input("Would you like to look up anything else?").lower()
            
        if again[0] == 'y':
            get_reviews()
        elif again[0] != 'y':
            print("Have a good day yo")
        
   
   
get_reviews()