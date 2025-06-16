from bs4 import BeautifulSoup
import requests
from reviewer import review_text  # 👈 Connect to reviewer

url = input("Enter the chapter URL: ")
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.title.string.strip()
main_text = soup.find('body').get_text(separator="\n", strip=True)

print("\n📝 Title:", title)
print("\n📚 Original Content:\n", main_text[:500])  # show first 500 chars

# 👇 Run through Reviewer
reviewed = review_text(main_text[:1000])  # Limit for testing
print("\n✅ Reviewed Content:\n", reviewed)
