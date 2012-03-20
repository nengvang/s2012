from urllib import urlopen, urlretrieve
import re

feeds = {'^Sherlock\.': 'http://ezrss.it/search/index.php?simple&show_name=Sherlock&mode=rss_feed',
         '^Awake\.': 'http://ezrss.it/search/index.php?simple&show_name=Awake&mode=rss_feed',
         }

black_list_patterns = ['(.*)720(.*)',]
white_list_patterns = ['(.*)REPACK(.*)',]
black_list = None
white_list = None

def scrape_ezrss(feed):
    # Open RSS feed, and download page
    page  = urlopen(feed).read()
    
    # Compile regular expression and search for .tc2 table elements
    # These contain torrent urls on ezrss.it
    torr = re.compile('\"http:(.*)\.torrent\"')
    find_torrs = re.findall(torr, page)
    find_torrs = ['http:'+ft+'.torrent' for ft in find_torrs]
    find_urls = []
    for ft in find_torrs:
        if ft not in find_urls:
            find_urls.append(ft)

    # Look through all found torrents, and get episode details and file names
    downloads = []
    for fu in find_urls:
        dl = {'url': fu,
              'name': fu.split('/')[-1]}
        dl['ep'] = get_episode(dl['name'])
        downloads.append(dl)

    return filter_downloads(downloads)


def filter_downloads(downloads):
    global black_list, white_list
    # Initialize global filters
    if black_list is None:
        black_list = [re.compile(bl) for bl in black_list_patterns]
        white_list = [re.compile(wl) for wl in white_list_patterns]

    approved = []
    # First check global filters
    # Black List
    for dl in downloads:
        for bl in black_list:
            if re.findall(bl, dl['name']):
                break
        else:
            approved.append(dl)

    return approved


def get_episode(filename):
##    print 'get_episode', filename
    re_x = '(.*)\.([0-9]+)[xX]([0-9]+)\.(.*)'
    re_se = '(.*)\.[sS]([0-9]+)[eE]([0-9]+)\.(.*)'

    x = re.compile(re_x)
    se = re.compile(re_se)

    # x-type episode info (eg. 1x01)
    ep = re.findall(x, filename)
    if ep:
        return {'season': int(ep[0][1]), 'episode': int(ep[0][2])}

    # se-type episode info (eg. S01E01)
    ep = re.findall(se, filename)
    if ep:
        return {'season': int(ep[0][1]), 'episode': int(ep[0][2])}

    # No episode info
    return None


def retrieve_downloads(downloads):
    for dl in downloads:
        urlretrieve(dl['url'], dl['name'])
        print 'File: {name}\n\tURL: {url}\n\tEpInfo: {ep}'.format(**dl)


if __name__ == '__main__':
    downloads = []
    for fname, frss in feeds.iteritems():
        downloads += scrape_ezrss(frss)

    retrieve_downloads(downloads)
