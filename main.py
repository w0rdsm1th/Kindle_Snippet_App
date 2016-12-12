# var/lib/python

import selenium
import getpass

# custom class:
# a snippet object
# attributes: language, keyword(s), original highlighted time,

# methods:
# pull out the keywords, with pygame?
# return a dictionary formatted version of the snip

# detect language automatically, if not over a certain % confidence interval, consult?
# lookup the keywords in a translation dictionary
# lookup the keywords in a commonly used sentence
# extend/increment the length of the number of the keywords counts? b/c that will mean more dict checking
# seen before? check if phrase is already in the dictionary

# printing a sentence on screen, and being able to record which word was clicked
# if multiple button is clicked before hand, wont exit the word selection screen until click 'next'

#_______________________#_______________________#_______________________#_______________________
import getpass
highlight_website = {'username':'aleks_hughes@hotmail.com',
                     'url':'https://kindle.amazon.com/your_highlights'}
highlight_website['password'] = getpass.getpass()

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary)
browser.get(highlight_website['url'])

uname_box = browser.find_elements_by_name('email')
assert type(uname_box) == list and len(uname_box) == 1  # check that found unique email box
uname_box = uname_box[0]
uname_box.clear()
uname_box.send_keys(highlight_website['username'])

pw_box = browser.find_elements_by_name('password')
assert type(pw_box) == list and len(pw_box) == 1
pw_box = pw_box[0]
pw_box.send_keys((highlight_website['password']))

login_button = browser.find_elements_by_id('signInSubmit')
assert type(login_button) is list and len(login_button) == 1
login_button = login_button[0]
login_button.click()


# waits for page to load
# http://selenium-python.readthedocs.io/waits.html#waits

# scrolling down until no new elements??
# scroll down to force to load - do so until find something that indicates reached bottom of page??
while True:
    # if *not* at bottom of page, try to scroll to it
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.implicitly_wait(4)
    curr_y_scroll = browser.execute_script('return window.pageYOffset;')
    page_y_scroll = browser.execute_script('return document.body.scrollHeight;')

    # finishing criterion of the loop
    if abs(curr_y_scroll-page_y_scroll) < 700:
        print('curr_y_scroll: ', curr_y_scroll,
              '\n page_y_scroll: ', page_y_scroll,
            '\n abs: ', abs(curr_y_scroll-page_y_scroll))

        print('Think reached bottom of page')
        break


browser.find_element_by_class_name("highlight")
highlight_set = browser.find_elements_by_class_name("highlight")
highlight_set[-1]
type(highlight_set[-1])
dir(highlight_set[-1])
highlight_set[-2].text
dir(highlight_set[-2].parent)
len(browser.find_elements_by_class_name("highlight"))

book_section_class = "bookMain yourHighlightsHeader"

from bs4 import BeautifulSoup
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
soup.find_all('div', class_=book_section_class)
for each in soup.find_all('div', class_=book_section_class):
    each.find('span', class_='author').text
    each.find('span', class_='title').text
    each.find('div', class_='lastHighlighted').text

while True:
    each.nextSibling.next['class']
    highlight_spans = each.nextSibling.next.find_all('span')

    if each.nextSibling.next.has_key('class') and each.nextSibling.next['class'] == book_section_class:
        break

each.contents
each.find_all('div', class_='highlightRow yourHighlight')
each.find_all('span', class_='highlightRow')

each.find_next('div', class_='highlightRow yourHighlight')
each.find_next('div', class_='highlightRow yourHighlight')

for echild in each.descendants:
    print(echild)

for sibling in each.div.next_siblings:
    print(repr(sibling))
each.find_next_sibling('div', book_section_class)

browser.close()
browser.quit()

# view the snippets
# import the snippets - assign a key, import metadata
# add a note to the highlight in myhighlights saying already been imported?

# buttons:
# toggle between English and Spanish
# toggle to multiple keywords in single phrase/snippet, default single word as problem
# saveable for progress: new word assignments already completed are pickled and saved as dictionary

#_______________________#_______________________#_______________________#_______________________
#NICE TO HAVE
# lookup official OED entry
# automatic English/Spanish detection


class Snippet(object):
    def __init__(self, snip, language, keywords):
        self.snip = snip
        self.language = language
        self.keywords = [keywords]

    def dictionise(self, sp = snip, lang = language, kw = keywords):
        return {'snip':sp,
                'language':lang,
                'keywords':[kw]}


