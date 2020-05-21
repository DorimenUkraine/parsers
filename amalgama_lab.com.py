import requests
from lxml import etree
import lxml.html
import csv


# Parser text from URL and write to csv
def parser_url(url):
    try:
        api = requests.get(url)
    except:
        pass
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/')

    with open("text.csv", "w", newline='') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            write.writerow(text_original[i])
            write.writerow(text_translate[i])


# Parser URI from URL for name of csv
def parser_uri(url):
    pass


def main():
    parser_url("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")


if __name__ == "__main__":
    main()


