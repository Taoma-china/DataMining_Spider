import urllib2
import re
class Spider:

    def __init__(self):
        self.enable = True
        self.page=1

    def load_page(self,page):

        url = "http://www.neihan8.com/article/list_5_"+ str(page)+".html"
        user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
        headers = {"User-Agent": user_agent}
        
        req = urllib2.Request(url, headers=headers)

        response = urllib2.urlopen(req)

        html = response.read()

        new_html = html.decode("gbk").encode("utf-8")
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        item_list = pattern.findall(new_html)
        return item_list
    def deal_one_page(self,item_list,page):
        
        for item in item_list:
            print item.replace(r"</p>"," ")
            self.write_to_file(item)
    def write_to_file(self,txt):
        f = open('./myStory.txt','a')
        f.write(txt)
        f.write('------------------')
        f.close()
    def do_work(self):
        while self.enable:
            print "enter to continue"
            print "quit to quit"
            command = raw_input()
            if (command == "quit"):
                self.enable = False
                break;
            item_list = self.load_page(self.page)
            self.deal_one_page(item_list,self.page)
            self.page +=1
if __name__=="__main__":
    mySpider = Spider()
    mySpider.do_work()
    
