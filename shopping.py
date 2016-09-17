import requests
from bs4 import BeautifulSoup
import argparse
import json

def getCount(keyword):
    try:
        url = "http://www.shopping.com/products?KW="+keyword
        response = requests.get(url)
        #print response.text
        resp_code = response.status_code
    except Exception as e:
        print str(e)
        return "Error while requesting "+ str(e)
    if resp_code == 200:
        b = BeautifulSoup(response.text,"lxml")
    else:
        b = ''
    if b:
        filterbox = b.find("div",{"id":"sortFiltersBox"})
        if filterbox:
            span =  filterbox.find("span")
            results_count = span.attrs["name"].split(":")[1]
            output = {"keyword":keyword, "no. of result":results_count}
            return json.dumps(output)
        else:
            return "Result not Found for this keyword"
    else:
        return "Bad request"


def getCountFromPage(keyword, pagenumber):
    try:
        try:
            url = "http://www.shopping.com/products~PG-"+pagenumber+"?KW="+keyword
            response = requests.get(url)
            resp_data = response.text
            b = BeautifulSoup(resp_data,"lxml")
            divdata = b.find_all("div",{"class":"gridBox"})
            if divdata:
                item_list = []
                for i in divdata:
                    dict_temp = {}
                    try:
                        item_price = i.find("input",{"name":"itemPrice"}).get('value')
                        item_title = i.find("img").get('title')
                        dict_temp["name"] = item_title
                        dict_temp["price"] = item_price
                        item_list.append(dict_temp)
                    except Exception as e:
                        pass
                data = {}
                data["Keyword"] = keyword
                data["Page Number"] = pagenumber
                data["Number of items"] = len(item_list)
                data["data"] = item_list
                return json.dumps(data)
            else:
                return "No data Found for this input"
        except Exception as e:
            print str(e)
            return "Error while requesting "+ str(e)
    except Exception as e:
        print "Error in getCountFromPage: "+str(e)
        return "Error....!!!"
        



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--KW', help="Enter keyword to search")
parser.add_argument('--PN', help="Enter Page Number ")
args = parser.parse_args()
keyword = args.KW
pagenumber = args.PN
if not pagenumber:
    response_1 = getCount(keyword)
    print response_1
else:
    response_2 = getCountFromPage(keyword, pagenumber)
    print response_2
