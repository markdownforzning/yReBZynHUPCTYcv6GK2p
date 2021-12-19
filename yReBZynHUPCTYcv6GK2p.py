import requests
import urllib.request
import sys
import argparse

# the main get content codes
def get_url(url):
    # himalaya server requests need headers, otherwise return empty
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }
    page = requests.get(url, headers = headers).content
    # convert to str within utf-8 encoding
    page = page.decode('utf-8')
    return page


if __name__ == '__main__':
    # need system args input
    arg_prsr = argparse.ArgumentParser()
    arg_prsr.add_argument('-l','--url', required=True, action='append', help = 'Required. Which one RSS Xml do you want to convert.')
    args = arg_prsr.parse_args(sys.argv[1:])
    url = args.url

    for i in url:
        url_content = get_url(i)
        url_content = url_content.splitlines()
        down_list = []

        for i in url_content:
            if(i.find("url=\"https://jt.ximalaya.com/")!=-1 or i.find("<itunes:subtitle><![CDATA[")!=-1):
                down_list.append(i.strip().replace("url=","").replace("\"","")
                    .replace("<itunes:subtitle><![CDATA[","")
                    .replace("]]></itunes:subtitle>",""))

        for i in down_list:
            if down_list.index(i)!=0 and down_list.index(i)%2==1:
                urllib.request.urlretrieve(down_list[down_list.index(i)+1], i+".m4a")
