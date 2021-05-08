from os import remove
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"hiking.jpg",
        "date":date(2021,7,14),
        "author":"Azeem Mirza",
        "title":"Mountains Hiking",
        "excerpt":"There is nothing like the mountain hiking in the world. Initially it was a nightmare but in the end it was fun and I wanna explore it again.",
        "content":'''
         Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
          
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
          
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
        '''
    },
    {
        "slug":"what-is-cloud-computing",
        "image":"cloud.jpg",
        "date":date(2021,3,14),
        "author":"Azeem Mirza",
        "title":"Clound Computing",
        "excerpt":"Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale.",
        "content":'''
         Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
          
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
          
           Lorem ipsum dolor sit, amet consectetur adipisicing elit. Qui dolor
          magnam placeat maiores at perspiciatis nulla fuga quia reiciendis
          dignissimos aut, tempore omnis culpa asperiores iusto ut eveniet
          libero possimus?
        '''
    },
    {
        "slug":"why-you-learn-python",
        "image":"python-logo.png",
        "date":date(2021,1,5),
        "author":"Azeem Mirza",
        "title":"Why you should learn python",
        "excerpt":"Python is one of the most loved programming languages by developers, data scientists, software engineers, and even hackers because of its versatility, flexibility, and object-oriented features. ... Although it's a high-level language and can do complex tasks, Python is easy to learn and has a clean syntax",
        "content":'''
         As a data scientist, my work is contingent on knowing and using Python. What I like about Python, and why I rely on it so much, is that it’s simple to read and understand, and it’s versatile. From cleaning, querying, and analyzing data, to developing models and visualizing results, I conduct all these activities using Python. 

        I also teach data science in Python. My students learn Python to build machine learning models but I’m always excited to hear of the other ways they’ve leveraged the programming language. One of my students told me they used it to web-scrape online basketball statistics just so they could analyze the data to win an argument with friends. Another student decided to expand on her knowledge of Python by learning Django, a popular framework, which she uses to build web apps for small businesses. 

Before taking the plunge into data science, we all had fundamental questions (and concerns) about learning Python. If this sounds like you, don’t worry. Before I started learning Python, I spent several months convincing myself to start. Now that I’ve learned, my only regret was not starting sooner.

If you’re interested in learning Python, I want to share my biggest reasons for why you should. Two of these reasons are inherent to Python; one of them is a benefit of Python that I experienced first-hand, and some of the examples I discuss come from things I have researched. My goal is to give you enough information to help make an educated decision about learning Python, and I really hope that you choose to learn.
        '''
    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_post = sorted(all_posts,key=get_date)
    latest_posts = sorted_post[-3:]
    return render(request,'blog/index.html',{"posts":latest_posts})

def posts(request):
    return render(request,'blog/posts.html',{"posts":all_posts})


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,'blog/post-detail.html',{"post":post})
