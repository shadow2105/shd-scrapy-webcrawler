# shd-scrapy-webcrawler
Scrapy-based web crawler to scrape static web page content

```
********************* Instructions to execute the Project *********************

1. Extract/unzip the shared .zip file to the (PyCharm) Project folder - 'scrapyProject'

2. In Terminal/Powershell, navigate to the extracted Project folder -

PS C:\Users> cd .\scrapyProject\
PS C:\Users\scrapyProject> ls


    Directory: C:\Users\ashwi\OneDrive\Desktop\scrapyProject

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        01-01-2022     19:17                .idea
d-----        02-01-2022     16:21                repCrawl
d-----        01-01-2022     18:44                venv


3. Activate virtual (Python) environment - 

PS C:\Users\scrapyProject> .\venv\Scripts\activate



4. Navigate to (scrapy) Project folder - 

(venv) PS C:\Users\scrapyProject> cd .\repCrawl\
(venv) PS C:\Users\scrapyProject\repCrawl> tree /F
Folder PATH listing
Volume serial number is ****-****
C:.
│   reps.json
│   scrapy.cfg
│
└───repCrawl
    │   items.py
    │   middlewares.py
    │   pipelines.py
    │   settings.py
    │   __init__.py
    │
    ├───spiders
    │   │   mySpider.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           mySpider.cpython-39.pyc
    │           __init__.cpython-39.pyc
    │
    └───__pycache__
            items.cpython-39.pyc
            pipelines.cpython-39.pyc
            settings.cpython-39.pyc
            __init__.cpython-39.pyc


5. ./reps.json is the expected JSON output file generated after running the command -
(running the command again will overwrite the existing output file)

(venv) PS C:\Users\scrapyProject\repCrawl> python -m scrapy crawl mySpider


here, 'mySpider' is the name attribute of class 'MySpider' in .\repCrawl\spiders\mySpider.py

'reps.json' is the file defined/opened in .\repCrawl\pipelines.py to be written with the scraped data in JSON format.
```

