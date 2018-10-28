import sys
import lxml
from requests_html import HTMLSession

session = HTMLSession()
firstChapter = session.get('https://www.fictionpress.com/s/2961893/1/Mother-of-Learning')
if not 'Good Morning Brother' in firstChapter.text:
    raise Exception('GM not found')
else:
    options = firstChapter.html.find('#chap_select:first option')
    chapters = [option.attrs['value'] for option in options]
    for chapter in chapters:
        print(f'Processing {chapter} of {len(chapters)} chapters...', file=sys.stderr)
        url = f'https://www.fictionpress.com/s/2961893/{chapter}/Mother-of-Learning'
        chapterHtml = session.get(url)
        chapterElement = chapterHtml.html.find('#storytext', first=True).element
        print(chapterElement.text or '')
        for kid in chapterElement.iterchildren():
            print(lxml.html.tostring(kid, encoding='unicode'))