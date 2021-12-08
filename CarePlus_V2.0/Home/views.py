from django.shortcuts import render, HttpResponse, redirect
import requests
import json

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
import requests
from bs4 import BeautifulSoup
#from newsapi import NewsApiClient
#import covidstats


# Create your models here.
def home_view(request):
    return render(request, 'home/start.html')

@login_required(login_url='login')
def homePage(request):
    #vietnam_case =  covidstats.Coronavirus().get_stats("Vietnam")
    vietnam_case = [{'Country': 'Vietnam', 'TotalCases': '1,181,337', 'NewCases': '', 'TotalDeaths': '24,544 ', 'NewDeaths': '', 'TotalRecovered': '955,256', 'ActiveCases': '603,234', 'CriticalCases': '201,537'}]

    vietnam_totalcase = vietnam_case[0]['TotalCases']
    vietnam_deaths = vietnam_case[0]['TotalDeaths']
    vietnam_recovered = vietnam_case[0]['TotalRecovered']
    vietnam_active = vietnam_case[0]['ActiveCases']

    #newsapi = NewsApiClient(api_key='e6702efb133e48418f78ea26f4620e20') 

    # top_headlines = newsapi.get_top_headlines(q='covid',
    #                                       category='business',
    #                                       language='en',
    #                                       country='us')
    
    #data = top_headlines['articles']
    response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll('h3', class_='title-news')
    links = [link.find('a').attrs["href"] for link in titles]

    new = ['Không khí lạnh tăng cường miền Bắc mưa rét, Thanh Hóa đến Khánh Hòa mưa rào', "Atletico Madrid 'lách qua khe cửa hẹp', giành vé đi tiếp ở Champions League", 'Mbappe phá kỉ lục của Messi tại Champions League']
    desc = ['TTO - Do ảnh hưởng của không khí lạnh, từ đêm nay (8-12) ở Bắc Bộ có mưa nhỏ rải rác, khu vực Thanh Hóa đến Khánh Hòa có mưa rào và dông, cục bộ có mưa vừa, mưa to.', 'TTO - Rạng sáng 8-12, Atletico Madrid đã đánh bại Porto 3-1 trên sân khách ở lượt trận cuối cùng bảng B Champions League. Kết quả này cộng với việc Liverpool hạ AC Milan 2-1, Atletico Madrid "lách qua khe cửa hẹp" giành vé đi tiếp.', 'TTO - Với cú đúp vào lưới Club Brugge sáng 8-12, tiền đạo Kylian Mbappe của CLB Paris Saint-Germain (PSG) đã xác lập kỉ lục mới tại Champions League.']  
    img = ['https://cdn.tuoitre.vn/thumb_w/586/2020/3/10/sa-pa-15838201764471657314242.jpg', 'https://cdn.tuoitre.vn/thumb_w/586/2021/12/8/2021-12-07t220355z1068590365up1ehc71pahovrtrmadp3soccer-champions-por-atm-report-16389170873611298800606.jpg', 'https://cdn.tuoitre.vn/zoom/150_120/2021/11/25/18b-1637851160009314216630-crop-16378512284001120841496.jpg']
    urls = ['https://tuoitre.vn/khong-khi-lanh-tang-cuong-mien-bac-mua-ret-thanh-hoa-den-khanh-hoa-mua-rao-20211208071826166.htm', 'https://tuoitre.vn/atletico-madrid-lach-qua-khe-cua-hep-gianh-ve-di-tiep-o-champions-league-20211208055537931.htm', 'https://tuoitre.vn/mbappe-pha-ki-luc-cua-messi-tai-champions-league-20211208054807325.htm']

    # for i in range(7):
    #     news = requests.get("https://tuoitre.vn" + links[i])
    #     soup = BeautifulSoup(news.content, "html.parser")
    #     title = soup.find("h1", class_="article-title").text
    #     abstract = soup.find("h2", class_="sapo").text
    #     body = soup.find("div", id="main-detail-body")
    #     content = body.findChildren("p", recursive=False)[0].text + body.findChildren("p", recursive=False)[1].text
    #     image = body.find("img").attrs["src"]
    #     url = "https://tuoitre.vn" + links[i]

    #     #print("Tiêu đề: " + title)
    #     new.append(title)

    #     #print("Mô tả: " + abstract)
    #     desc.append(abstract)
    #     #print("Nội dung: " + content)
    #     img.append(image)
    #     #print("Ảnh minh họa: " + image)
    #     urls.append(url)
    #     #print("Url : " + url)

    #print("_________________________________________________________________________")


    print(new)
    print(desc)
    print(img)
    print(urls)

    mylist = zip(new, desc, img, urls)

    context = {
        'vietnam_totalcase': vietnam_totalcase,
        'vietnam_deaths': vietnam_deaths,
        'vietnam_recovered': vietnam_recovered,
        'vietnam_active': vietnam_active,
        'mylist': mylist,
    }

    return render(request, 'home/home.html', context)
