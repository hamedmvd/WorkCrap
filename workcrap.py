from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys

t = str(datetime.datetime.now()).split(" ")
print(t[0])

class App:
    def __init__(self, que=input('\nEnter: ').replace(" ", "+")):
        self.que = que
        self.base_url = f'https://www.indeed.com/jobs?q={self.que}&l='
        self.req = requests.get(self.base_url)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')

    def start_reqing(self):
        self.data = {}
        for x in self.soup.find_all('a', {'data-tn-element':'jobTitle'}):
            self.data[x.text] ="https://wwww.indeed.com"+x['href']
        self.new_data = {k.replace('\n', ''):v for k, v in self.data.items()}
    def showing_perfect(self, i = 0):
        self.link_data_new = dict(enumerate(self.new_data.values()))
        for x in self.new_data:
            print(f"{i}: {x}")
            i +=1
        self.inp = input("Enter: ")
        self.linking = self.link_data_new[int(self.inp)]

    def selenium(self, driver = webdriver.Chrome('/home/ubuntu/whoami/WorkCrap/chromedriver')):
        self.get = driver.get(self.linking)

p = App()
p.start_reqing()
p.showing_perfect()
p.selenium()
