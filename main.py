from bs4 import BeautifulSoup, SoupStrainer
import requests
import xmltodict
import json
import os


def getUrl(url):
    """
    Sends a get request to the gievn url.
    """

    response = requests.get(url)
    print('Called:', url)
    print('Status Code:', response.status_code)

    return response.content


def getAndCallAssets(content):
    """
    Parse the given HTML content for assets like CSS, JS, Images and send an HTTP Get request.
    """

    soup = BeautifulSoup(content, 'html.parser')

    # call to img tags
    for img in soup.find_all('img', src=True):
        try:
            images = img['data-srcset']
            images = [images.strip().split(' ')[0] for image in images.split(',')]

            for image_url in images:
                getUrl(image_url)
        except KeyError:
            pass

    # call to script tags
    for script in soup.find_all('script', src=True):
        try:
            script = script['src']
            getUrl(script)
        except KeyError:
            pass

    # call to link tags
    for link in soup.find_all('link'):
        try:
            link = link['href']
            getUrl(link)
        except KeyError:
            pass


def parseSitemapForLinks(sitemap_url):
    """
    Scrap the given sitemap url and return the website links.
    """

    response = requests.get(sitemap_url)
    sitemap = xmltodict.parse(response.content)
    urls = sitemap.get('urlset').get('url')

    target_urls = []
    for url in urls:
        target_urls.append(url.get('loc'))

    return target_urls


def main():
    sitemap_url = os.getenv('INPUT_SITEMAP_URL')
    target_urls = parseSitemapForLinks(sitemap_url)

    for url in target_urls:
        content = getUrl(url)
        getAndCallAssets(content)


if __name__ == '__main__':
    main()
