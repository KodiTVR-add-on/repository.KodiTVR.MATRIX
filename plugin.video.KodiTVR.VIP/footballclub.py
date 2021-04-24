#py3 fixed Mod by KodiTVR
#!/usr/bin/python
# -*- coding: utf-8 -*-
#######################################[FUCK YOU GRUPETA]############################################################################
##########################################[ACEITA QUE DÓI MENOS]#####################################################################
#####################################################################################################################################
# ===================================================================================================================================
#####################################################################################################################################
#            88888 Yb    dP    8              .d88b                         |8|  .8/""                                              #
#   0000       8    Yb  dP     88b. Yb  dP    8P www 8d8b 8   8 88b. .d8b.  |8| .8/                   w 88888 Yb     dP|888b.       #
#              8     YbdP      8  8  YbdP     8b  d8 8P   8b d8 8  8 8' .8  |8wwKK|    .d8b.  |88b.  |8| |8|    Yb  dP |8  .8   (c) #
#              8      YP       88P'   dP      `Y88P' 8    `Y8P8 88P' `Y8P'  |8|  Yb\  8'| |.8 |8| |8 |8| |8|     YbdP  |8wwk`       #
#                                     8                         8           |8|  'Yb\__`Y8P´  |88P'  |8| |8|      YP   |8  Yb_      #
#####################################################################################################################################
# ===================================================================================================================================
# ############Imports################################################################################################################

import sys
import xbmcaddon, xbmcgui, xbmcplugin

# Plugin Info
ADDON_ID      = 'plugin.video.KodiTVR.VIP'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

def addDir(title, url,icon):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':icon,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

    
def football_club():
    addDir(title="[COLORgold]---●★| ⚽️ KodiTVR *História de Clubes de Futebol* Channels ⚽️|★●---[/COLOR]"            , url="plugin://plugin.video.youtube/channel/UCAqsAQnn2jiIidFaOXS_rfQ/",icon = "https://yt3.ggpht.com/ytc/AAUvwni2dF8ge4KIqnccPoGLQzCEykqIl2H0M2gr4A=s88-c-k-c0x00ffffff-no-rj")
    addDir(title="História do BENFICA DESDE A SUA CRIAÇÃO."                  , url="plugin://plugin.video.youtube/channel/UCn610M9E2nqgKgxEKQ9yB8w/",icon = "https://yt3.ggpht.com/ytc/AAUvwnjzSxx_y2GKfFZSzXNX_8cR4kag8GVmCtg29_J4uVo=s88-c-k-c0x00ffffff-no-rj")
    addDir(title="História do SPORTING DESDE A SUA CRIAÇÃO."                        , url="plugin://plugin.video.youtube/channel/UCTQtZLj8wfAzQwS-d81IMvQ/",icon = "https://yt3.ggpht.com/ytc/AAUvwnhAP__V2lcvfPGzlfzTJMhXfYxIofZCyOppQbnt=s88-c-k-c0x00ffffff-no-rj")
    addDir(title="História do F.C.PORTO"                        , url="plugin://plugin.video.youtube/channel/UCaM8dvOI5ON2A3lIvo1FVUA/",icon = "https://yt3.ggpht.com/ytc/AAUvwnizO5g7y0qESFGuvAhz9t0jLxWrCS8ZjBXoAuJC=s48-c-k-c0x00ffffff-no-rj")
    addDir(title="História do Clube FLAMENGO"                        , url="plugin://plugin.video.youtube/channel/UCNO_kE6srPIGykUY996noUg/",icon = "https://yt3.ggpht.com/ytc/AAUvwniGt3ZJQbbBZH4ouPuw4cdaPPOVuSaC2pslaeuP=s88-c-k-c0x00ffffff-no-rj")
    addDir(title="História do SANTOS FUTEBOL CLUBE"                      , url="plugin://plugin.video.youtube/channel/UCthtt1G3hyOzerDV7Mv7A9A/",icon = "https://yt3.ggpht.com/ytc/AAUvwng81CcEk_rjqOYKl-kxhW1bTJqoAQa8dow6YBRNzA=s48-c-k-c0x00ffffff-no-rj")
    xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
