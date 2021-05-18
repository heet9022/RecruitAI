from lxml.html import fromstring
import requests
from proxy_checker import ProxyChecker

def get_proxy():

    """This function performs a search and tests a pool of proxies and then returns a valid & working proxy address.

    Returns:
        str: Proxy in the form of <ipaddress:port>
    """
 
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    print("Checking for Proxies")
    for proxy in proxies:
        checker = ProxyChecker()
        test = checker.check_proxy(proxy)
        print(f'{proxy}:{test}')
        if test:
            return proxy

if __name__ == "__main__":

    proxy = get_proxy()
    print(proxy)
