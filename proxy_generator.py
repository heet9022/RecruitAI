from lxml.html import fromstring
from itertools import cycle
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

import requests
import traceback
import logging

logger = logging.getLogger()

def get_proxy():

    logger.info("Generating proxy.....................")   
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:100]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    for proxy in proxies:
        if test_proxy(proxy):
            logger.info(".....................Proxy generated")
            return proxy


def test_proxy(proxy):

    logger.info("Testing Proxy..............")
    url = 'https://httpbin.org/ip'
    try:
        response = requests.get(
            url, proxies={"http": proxy, "https": proxy}, timeout=12)
        logger.info(response.json())
        return True
    except:
        logger.info("Skipping. Connnection error in the proxy")
        return False


if __name__ == "__main__":

    proxies = get_proxy()
    proxy_pool = cycle(proxies)

    url = 'https://httpbin.org/ip'
    for i in range(1, 11):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)

        if(test_proxy(proxy)):
            try:
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = proxy
                # prox.socks_proxy = proxy
                # prox.ssl_proxy = proxy

                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)

                driver = webdriver.Chrome(desired_capabilities=capabilities)
                driver.get("https://www.linkedin.com/login")
            except Exception as e:
                print(e)
