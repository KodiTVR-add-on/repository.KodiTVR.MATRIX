# -*- coding: UTF-8 -*-
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re
import urllib
import urlparse

from koditvrscrapers.modules import cleantitle, client, debrid, source_utils, utils
#from koditvrscrapers.sources_oathscrapers import cfScraper


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['yts.am']
        self.base_link = 'https://yts.mx/'
        self.search_link = 'browse-movies/%s/all/all/0/latest/0/all'

    def movie(self, imdb, title, localtitle, aliases, year):
        if debrid.status() is False:
            return

        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None:
                return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            query = '%s %s' % (data['title'], data['year'])

            #_headers = {'User-Agent': client.agent()}

            url = self.search_link % urllib.quote(query)
            url = urlparse.urljoin(self.base_link, url)
            html = client.request(url)#, headers=_headers)
            try:
                results = client.parseDOM(html, 'div', attrs={'class': 'row'})[2]
            except Exception:
                return sources

            items = re.findall('class="browse-movie-bottom">(.+?)</div>\s</div>', results, re.DOTALL)
            if items is None:
                return sources

            for entry in items:
                try:
                    try:
                        link, name = re.findall('<a href="(.+?)" class="browse-movie-title">(.+?)</a>', entry, re.DOTALL)[0]
                        name = client.replaceHTMLCodes(name)
                        if not cleantitle.get(data['title']) in cleantitle.get(name):
                            continue
                    except Exception:
                        continue
                    y = entry[-4:]
                    if not y == data['year']:
                        continue

                    response = client.request(link)#, headers=_headers)
                    try:
                        entries = client.parseDOM(response, 'div', attrs={'class': 'modal-torrent'})
                        for torrent in entries:
                            link, name = re.findall('href="magnet:(.+?)" class="magnet-download download-torrent magnet" title="(.+?)"', torrent, re.DOTALL)[0]
                            link = 'magnet:%s' % link
                            link = str(client.replaceHTMLCodes(link).split('&tr')[0])
                            quality, info = source_utils.get_release_quality(name, link)
                            try:
                                size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+)\s*(?:GB|GiB|MB|MiB))', torrent)[-1]
                                dsize, isize = utils._size(size)
                            except Exception:
                                dsize, isize = 0, ''
                            info.insert(0, isize)
                            info = ' | '.join(info)

                            sources.append({'source': 'Torrent', 'quality': quality, 'language': 'en',
                                            'url': link, 'info': info, 'direct': False, 'debridonly': True, 'size': dsize})
                    except Exception:
                        continue
                except Exception:
                    continue

            return sources
        except Exception:
            import traceback
            from resources.lib.modules import log_utils
            failure = traceback.format_exc()
            log_utils.log('---Ytsam Testing - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        return url