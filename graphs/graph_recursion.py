class Internet(object):
    """
    this class has knowledge of all the web pages that exist.
    given the url of a web page its contents can be fetched
    """

    # the dictionary below represents the graph
    pages = {
        'http://A.com': ['http://C.com', 'http://D.com', 'http://F.com'],  # [ac,ad,af]
        'http://B.com': ['http://A.com', 'http://F.com'],  # [ba, bf]
        'http://C.com': ['http://B.com', 'http://D.com'],  # [cb,cd]
        'http://D.com': [],  # D doesn't link anywhere
        'http://E.com': ['http://F.com'],  # ef
        'http://F.com': []  # F doesn't link anywhere
    }

    @classmethod
    def fetch_page_links(cls, url):
        """
        given a page url, return a list of all the urls that the page links to
        """
        if url not in cls.pages:
            # the url does not exist on the Internet
            raise Exception(404)
        return cls.pages[url]

    @staticmethod
    def traverse_graph(url, visited_pages=None):
        """
        this will do the actual work of traversing the graph.
        if the url has already been visited then return
        otherwise fetch all the links and visit each linked to page
        increment the known incoming link count as needed
        """

        visited_pages = visited_pages or {}
        # the visited_pages dictionary will be used to keep track of
        # what we have visited and how many incoming links we know about for each page

        # visited_pages will look like this:
        #  { url_1 : known_incomming_link_count_for_url_1, url_2 ... }

        if url in visited_pages:
            return visited_pages # been there done that. return

        # add the page to visited pages so that we don't exceed our maximum recursion
        visited_pages[url] = 0
        for link in Internet.fetch_page_links(url):
            # recurse
            Internet.traverse_graph(link, visited_pages)
            # and increment the incomming link count
            visited_pages[link] += 1
            pass
        return visited_pages


print(Internet.traverse_graph('http://A.com'))
