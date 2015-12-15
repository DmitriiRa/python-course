from lxml import etree
import requests
import timeit
import re

url = "https://en.wikipedia.org/wiki/Coregonus_lavaretus"
regex = "'/wiki/[\w\(\)]+'"
visited_links = ["https://en.wikipedia.org/wiki/Main_Page"]


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
        return(start, finish)
    else:
        print("not in the first click")
    add_link(visited_links, start)
    return(start, second_click(links, finish), finish)


def second_click(links1, finish):
    links2 = {}
    for link in links1:
        print("second click")
        l = links_from_page(link)
        add_link(visited_links, link)
        if finish in l:
            return(link)
        else:
            links2[link] = l
    print("not in the second click")
    return(third_click(links2, finish))


def third_click(links2, finish):
    for element in links2.keys():
        print("##########################")
        print(element)
        for link in links2[element]:
            print("third click")
            l = links_from_page(link)
            add_link(visited_links, link)
            if finish in l:
                return(element, link)
            
    print("not in the third click")
    return()
    

#links_from_page("https://en.wikipedia.org/wiki/Coregonus_lavaretus")
start = "https://en.wikipedia.org/wiki/Straton_tube"
finish = "https://en.wikipedia.org/wiki/Waveform_monitor"
#for i in first_click(start, finish):
#    print(i)
print(first_click(start, finish))
