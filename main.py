from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import asyncio


class MonkeytypeHacker:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # loads the page
    def load(self, url):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(url)
        wait.until(EC.url_to_be(url))
        self.driver.implicitly_wait(5)
        self.page_source = self.driver.page_source

    # gets the text from the page using BeautifulSoup
    def get_text(self):
        soup = BeautifulSoup(self.page_source, "html.parser")
        words = soup.find_all("div", class_="word")
        all_words = []
        for word in words:
            word_text = ""
            letters = word.find_all("letter")
            for letter in letters:
                word_text += letter.text
            all_words.append(word_text+" ")
        return all_words
   
    # types one word
    async def type_word(self, word, actions):
        for letter in word:
            actions.send_keys(letter)
        actions.perform()

    # types the entire text
    def type(self, words):
        actions = ActionChains(self.driver)
        for word in words:
            asyncio.run(self.type_word(word, actions))

if __name__ == "__main__":
    url = r"https://monkeytype.com/"

    hacker = MonkeytypeHacker()
    hacker.load(url)
    text = hacker.get_text()
    hacker.type(text)

    input()