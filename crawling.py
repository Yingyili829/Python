##crawl some data down
import urllib.request as req
url='https://www.ptt.cc/bbs/movie/index.html'
#to make it look like human browsing, need to make it a little bit complex
#create a Request object plus request Headers info
#purpose is for NOT opening the url directly, use request
request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

})
#use request instead of url itself
with req.urlopen(request) as response:
    data=response.read().decode('utf-8')

##interpret data and find out all the titles on the website
import bs4
#throw data(above)to beautifulsoup and have them interpret for html data
#html.parser - fix wording
root=bs4.BeautifulSoup(data,'html.parser')

#1st try-root's title(title here refers to html title like <title></title>)
#print(root.title)

#2nd try-get title's string
#print(root.title.string)

#3rd try-find <div>(this is called tag) class='title'(filter by)
#titles=root.find("div",class_="title")
#print(titles.a.string)

#4th try=find all the titles
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a !=None:
        print(title.a.string)





#TAKEAWAYS

# .title
# .find()