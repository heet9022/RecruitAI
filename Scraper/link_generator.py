import logging
from googlesearch import search

def generate(category='Digital Media', no_of_results=50):

    """This function queries google and returns a list of links of linkedin profiles depending on the argument given.

    Arguments:

        str: category
            Defines the category to be searched for in linkedin

        int: no_of_results
            The number of links to be fetched.

    Returns:
        list: A list of links of linkedin Profiles
    """

    logger = logging.getLogger()
    logger.info("Generating links.....................")

    links = []
    query = 'site:linkedin.com/in/ AND ' + category
    for link in search(query, tld="com", num=no_of_results, stop=no_of_results, pause=2):
        if 'linkedin' in link: 
            links.append(link)

    logger.info(links)
    logger.info("..................Links generated!")

    return links

if __name__ == "__main__":
    generate()
