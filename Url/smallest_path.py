from bs4 import BeautifulSoup, SoupStrainer
import requests
from utils.tree import Node
from utils.search.bidirectional_bfs import Bi_Bfs
from utils.search.bfs import bfs
from utils.url import get_urls
import os
import argparse

# doesn't work because web is a
def launch_search_bidirectional(url_start, url_goal):
    url_start = Node(url_start)
    url_goal = Node(url_goal)

    dico = {
        url_start.payload:url_start,
        url_goal.payload:url_goal
    }

    bfs1 = Bi_Bfs(url_start, dico, get_urls)
    bfs2 = Bi_Bfs(url_goal, dico, get_urls)

    bfs1.start()
    bfs2.start()

    bfs1.join()
    bfs2.join()

    sol = bfs1.sol[1:]
    sol.reverse()
    sol.extend(bfs2.sol)
    return sol

def launch_search_bfs(url_start, url_goal, show):
    return bfs([Node(url_start)], Node(url_goal), get_urls, [base_url], show)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action ="store_true", help="See what the program is doing")

    show = False
    args = parser.parse_args()
    if args.verbose:
        show = True
        print("verbose turned on")

    print("Past here the url of the first website")
    base_url = input()
    print("And now the url of the website to be reached")
    url_goal = input()

    sol = launch_search_bfs(base_url, url_goal, show)

    os.system("clear")
    if sol is not None:
        print("\n========= \n Here is the smallest path between {} and {} \n \n".format(base_url, url_goal))
        print(" -> ".join(sol))
