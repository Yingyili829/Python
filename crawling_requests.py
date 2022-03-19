##make request to download .pdf/.jpg

# import requests as req
# url = 'https://tw.appledaily.com/home/'
# r = req.get(url)

# with open('bcg.pdf',mode='wb') as file:
#     file.write(r.content)

import requests as req
url = 'https://web-assets.bcg.com/img-src/BCG-Most-Innovative-Companies-2020-Jun-2020-R-4_tcm9-251007.pdf'
r = req.get(url)

with open('bcg.pdf',mode='wb') as file:
    file.write(r.content)