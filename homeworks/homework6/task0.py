from lxml import etree
import requests
import timeit
import re


regex = "'/wiki/[\w\(\)-]+'"
visited_links = ["https://en.wikipedia.org/wiki/Main_Page"]
way = []


def add_link(links, link):
    if (link in links) == False:
        if (link in visited_links) == False:
            links.append(link)
    return links


def links_from_page(url):
    data = requests.get(url).text
    parser = etree.HTMLParser()
    tree = etree.fromstring(data, parser)
    links = []
    for element in tree.iter('a'):
        list_of_atr = str(element.attrib).split(", ")
        for word in list_of_atr:
            link = re.findall(regex, word)
            if link != []:
                link = link[0]
                link = "https://en.wikipedia.org" + link[1:-1]
                add_link(links, link)
    return(links)


def first_click(start, finish):
    links = links_from_page(start)
    if (finish in links) == True:
        return(1)
    add_link(visited_links, start)
    second_click(links, finish)
    return()


def second_click(links1, finish):
    links2 = {}
    for link in links1:
        l = links_from_page(link)
        add_link(visited_links, link)
        if finish in l:
            way.append(link)
            return(1)
        else:
            links2[link] = l
    third_click(links2, finish)
    return()


def third_click(links2, finish):
    for element in links2.keys():
        for link in links2[element]:
            print("third click")
            l = links_from_page(link)
            add_link(visited_links, link)
            if finish in l:
                way.append(elemet)
                way.append(link)
                return()
    print("Sorry, man(((")
    return()


start = "https://en.wikipedia.org/wiki/Gone_Maggie_Gone"
finish = "https://en.wikipedia.org/wiki/Theia_(planet)"
way.append(start)
first_click(start, finish)
way.append(finish)

for article in way:
    print(article)
