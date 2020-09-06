from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def crawl():
    from googlesearch import search
    query=request.args.get("name")
    query="privacy and cookie policy of "+query
    results=search(query,tld="co.in",num=5,stop=10,pause=2)
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    finaloutput=list()
    for urls in results:
        html=urlopen(urls)
        x=html.read()
        soup = BeautifulSoup(x,"html.parser")
        containers=soup.findAll("p")
        for container in containers:
          finaloutput.append(str(container.text))
    match=set()
    keywords=["cookie","preferences","actions","browsing history","operating system","facebook account","fnkdkdm","facebook profile","browser type","internet protocol (ip) address","internet service provider","data/time stamp","clicks","user e-mail address","cache"]
    for line in finaloutput:
          for keyword in keywords:
             if line.lower().find(keyword)!=-1:
                match.add(keyword)
    return list(match)

if __name__==" __main__ ":
    app.run()




