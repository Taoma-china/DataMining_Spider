#_*_ coding:utf-8 -*-
import urllib2
def load_page(url):
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    headers = {"User-Agent":user_agent}

    req= urllib2.Requset(url,headers=headers)
    response = urllib2.urlopen(req)
    html = response.read()
    return html
def tieba_spider(url,begin_page,end_page):

    for i in range(begin_page,end_page+1):
        pn = 50 *(i-1)

        my_url = url+str(pn)

        html = load_page(url)

       # print "==========%d==========="%(i)
       # print html
       # print "=========%d============"%(i)
        file_name = str(i)+ ".html"
        write_to_file(file_name,html)
def write_to_file(file_name,txt):
    print "storing file"+file_name
    f = open(file_name,'w')
    f.write(txt)
    f.close()
    







if __name__ == "__main__":




    print "aaa"
    url = raw_input("input  url ")
    print url

    begin_page = int(raw_input("begin page"))
    end_page = int(raw_input("end page"))

    tieba_spider(url,begin_page,end_page)
