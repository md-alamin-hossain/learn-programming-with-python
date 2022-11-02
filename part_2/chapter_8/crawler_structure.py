import logging
import sys
import requests
import re
import csv

def get_category_list(content):
    """get_category_list takes content of home page and returns a list of categories and their urls"""
    pass

def get_book_list(content):
    """get_book_list takes content of a book list page and returns a list of books (name and url)"""
    pass

def get_product_details(content):
    """get_product_details takes content of a product page, parses the page and returns details about a product"""
    pass

def get_page_content(url):
    """get_page_content takes a url and returns the content of the page"""
    pass

def get_next_page(content):
    """check the content the of a book list page and returns links of the next page, returns none if there is no more pages"""
    pass

def scrape_book_info(book_info, category_name):
    """get the content of a book details page, and parses different components and stores and info"""
    pass

def crawl_category(category_name, category_url):
    """crawls a particular category of books"""
    while True:
        content = get_page_content(category_url)
        book_list = get_book_list(content)
        for book in book_list:
            scrape_book_info(book, category_name)

        if get_next_page(content) is None:
            break

def crawl_website():
    """crawl_website is the main website that coordinates the whole crawling task"""
    url = 'http://books.toscrape.com/index.html'
    host_name = 'books.toscrape.com'

    content = get_page_content(url)
    category_list = get_category_list(content)

    for category in category_list:
        category_name, category_url = category
        crawl_category(category_name, category_url)



if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filename='booksotre_crawler.log', level=logging.DEBUG)

    with open('book_list.csv', 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Category', 'UPC', 'URL', 'Imageurl', 'Price', 'Availavaility', 'Description'])
    csv_writer.writeheader()

    crawl_website()



