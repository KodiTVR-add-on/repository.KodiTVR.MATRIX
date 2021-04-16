# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.TENNIS'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = " ● "
YOUTUBE_CHANNEL_ID2 = "UCDitdIjOjS9Myza9I21IqzQ"
YOUTUBE_CHANNEL_ID3 = " ● "


def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR blue]KodiTVR[/COLOR] [COLOR red]TENNIS[/COLOR]",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/rZupnbr.png",fanart="https://i.imgur.com/P8uq0XV.jpg",folder=True)
   addDir(title=" [COLOR cyan]Tennis Channel[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngSc7vil3VJ84TufDt21EcHzNiUA0xfhrOgq7Sksg=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/P8uq0XV.jpg",folder=True )
   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://i.imgur.com/rZupnbr.png",fanart="https://i.imgur.com/P8uq0XV.jpg",folder=True )
   					   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
