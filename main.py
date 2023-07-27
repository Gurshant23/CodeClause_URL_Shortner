import pyshorteners
url = input("Enter the url : ")
def shortenurl():
    s = pyshorteners.Shortener()
    print("The short url : "+ s.tinyurl.short(url))
shortenurl()
