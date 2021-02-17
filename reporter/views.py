from django.shortcuts import render


# bs4
from bs4 import BeautifulSoup
import requests



def content(request , content ):
    url = "https://www.thereporterethiopia.com/article/" + content
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.article
    
    img=contents.find("div", class_='post-thumbnail post-standard')
    if img == None :
        images = ""
    else:
        images = img.img.get('src')

    categories = contents.find("span", class_='post-categories').get_text()
    title = contents.find("h1", class_='post-title').get_text()
    date = contents.find("span", class_='post-created').get_text()
    author = contents.find("a", class_='username').get_text()
    ps = contents.find("div", class_='field field--name-body field--type-text-with-summary field--label-hidden field__item').find_all('p')
    p=[]
    for pl in ps:
        p.append(pl.get_text())



    all={   
        'image': images,
        'categories':categories,
        'title': title,
        'date':date,
        'author':author,
        'body': p
    }

    return render(request, 'content.html' , {"news":all})


def news(request):
    cate = 'News'
    page = requests.get("https://www.thereporterethiopia.com/news")
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find("div", class_='categories-view-content view-content-wrap layout-list')
    articles = contents.find_all("div", class_='item')
    # date = contents.find_all("span", class_='post-created')
    # a= []
    date =[]
    title =[]
    discription =[]
    image =[]
    link =[]
    newss =[]
    
    for article in articles:
        date.append( article.find("span", class_='post-created').get_text())
        title.append( article.find("h3", class_='post-title').a.span.get_text())
        discription.append( article.find("div", class_='post-body').get_text())
        
        img =article.find("div", class_='post-thumbnail post-image post-standard').img
        if img == None :
            image.append("")
        else:
            images = img.get('src')
        
        link = article.find("h3", class_='post-title').a.get('href')
        updated_link = link[9:]
        news ={
            'title': article.find("h3", class_='post-title').a.span.get_text(),
            'date': article.find("span", class_='post-created').get_text(),
            'discription': article.find("div", class_='post-body').get_text(),
            'image': images,
            'link': updated_link
        }
        images =""
        newss.append(news)
        


    return render(request, 'news.html' , {"soup":newss , 'cate':cate})


def business(request):
    cate = 'Business'
    page = requests.get("https://www.thereporterethiopia.com/business")
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find("div", class_='categories-view-content view-content-wrap layout-list')
    articles = contents.find_all("div", class_='item')
    # date = contents.find_all("span", class_='post-created')
    # a= []
    date =[]
    title =[]
    discription =[]
    image =[]
    link =[]
    newss =[]
    
    for article in articles:
        date.append( article.find("span", class_='post-created').get_text())
        title.append( article.find("h3", class_='post-title').a.span.get_text())
        discription.append( article.find("div", class_='post-body').get_text())
        
        img =article.find("div", class_='post-thumbnail post-image post-standard').img
        if img == None :
            image.append("")
        else:
            images = img.get('src')
        
        link = article.find("h3", class_='post-title').a.get('href')
        updated_link = link[9:]
        news ={
            'title': article.find("h3", class_='post-title').a.span.get_text(),
            'date': article.find("span", class_='post-created').get_text(),
            'discription': article.find("div", class_='post-body').get_text(),
            'image': images,
            'link': updated_link
        }
        images =""
        newss.append(news)
        
        


    return render(request, 'news.html' , {"soup":newss , 'cate':cate})


def sport(request):
    cate='Sport'
    page = requests.get("https://www.thereporterethiopia.com/sport")
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find("div", class_='categories-view-content view-content-wrap layout-list')
    articles = contents.find_all("div", class_='item')
    # date = contents.find_all("span", class_='post-created')
    # a= []
    date =[]
    title =[]
    discription =[]
    image =[]
    link =[]
    newss =[]
    
    for article in articles:
        date.append( article.find("span", class_='post-created').get_text())
        title.append( article.find("h3", class_='post-title').a.span.get_text())
        discription.append( article.find("div", class_='post-body').get_text())
        
        img =article.find("div", class_='post-thumbnail post-image post-standard').img
        if img == None :
            image.append("")
        else:
            images = img.get('src')
        
        link = article.find("h3", class_='post-title').a.get('href')
        updated_link = link[9:]
        news ={
            'title': article.find("h3", class_='post-title').a.span.get_text(),
            'date': article.find("span", class_='post-created').get_text(),
            'discription': article.find("div", class_='post-body').get_text(),
            'image': images,
            'link': updated_link
        }
        images =""
        newss.append(news)
        
        


    return render(request, 'news.html' , {"soup":newss , 'cate':cate})


def entertainment(request):
    cate='Entertainment'
    page = requests.get("https://www.thereporterethiopia.com/entertainment")
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find("div", class_='categories-view-content view-content-wrap layout-list')
    articles = contents.find_all("div", class_='item')
    # date = contents.find_all("span", class_='post-created')
    # a= []
    date =[]
    title =[]
    discription =[]
    image =[]
    link =[]
    newss =[]
    
    for article in articles:
        date.append( article.find("span", class_='post-created').get_text())
        title.append( article.find("h3", class_='post-title').a.span.get_text())
        discription.append( article.find("div", class_='post-body').get_text())
        
        img =article.find("div", class_='post-thumbnail post-image post-standard').img
        if img == None :
            image.append("")
        else:
            images = img.get('src')
        
        link = article.find("h3", class_='post-title').a.get('href')
        updated_link = link[9:]
        news ={
            'title': article.find("h3", class_='post-title').a.span.get_text(),
            'date': article.find("span", class_='post-created').get_text(),
            'discription': article.find("div", class_='post-body').get_text(),
            'image': images,
            'link': updated_link
        }
        images =""
        newss.append(news)
        
        


    return render(request, 'news.html' , {"soup":newss , 'cate':cate})


def lifestyle(request):
    cate='Lifestyle'
    page = requests.get("https://www.thereporterethiopia.com/lifestyle")
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find("div", class_='categories-view-content view-content-wrap layout-list')
    articles = contents.find_all("div", class_='item')
    # date = contents.find_all("span", class_='post-created')
    # a= []
    date =[]
    title =[]
    discription =[]
    image =[]
    link =[]
    newss =[]
    
    for article in articles:
        date.append( article.find("span", class_='post-created').get_text())
        title.append( article.find("h3", class_='post-title').a.span.get_text())
        discription.append( article.find("div", class_='post-body').get_text())
        
        img =article.find("div", class_='post-thumbnail post-image post-standard').img
        if img == None :
            image.append("")
        else:
            images = img.get('src')
        
        link = article.find("h3", class_='post-title').a.get('href')
        updated_link = link[9:]
        news ={
            'title': article.find("h3", class_='post-title').a.span.get_text(),
            'date': article.find("span", class_='post-created').get_text(),
            'discription': article.find("div", class_='post-body').get_text(),
            'image': images,
            'link': updated_link
        }
        images =""
        newss.append(news)
        


    return render(request, 'news.html' , {"soup":newss , 'cate':cate})


