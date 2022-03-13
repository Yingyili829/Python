##crawl some data down
#Json 

import urllib.request as req
url='https://www.sabrepc.com/CPUs-Processors'
request=req.Request(url,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

})
#use request instead of url itself
with req.urlopen(request) as response:
    data=response.read().decode('utf-8')

##interpret data and find out all the titles on the website
