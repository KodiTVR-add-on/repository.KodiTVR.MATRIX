# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.FORMULA.1'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "[COLOR green]●[/COLOR]"
YOUTUBE_CHANNEL_ID2 = "Formula1"
YOUTUBE_CHANNEL_ID3 = "[COLOR green]●[/COLOR]"
def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR red][B]KodiTVR[/B][/COLOR] FORMULA 1",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/aj3d2kw.png",fanart="https://i.imgur.com/qnHiJyJ.jpg",folder=True)
   addDir(title=" [COLOR red]FORMULA[/COLOR] 1",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnglSBGJhobxUNCOjG9KceTuNE-qs-W7P5-iI2FFmw=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/qnHiJyJ.jpg",folder=True )
   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://i.imgur.com/aj3d2kw.png",fanart="https://i.imgur.com/qnHiJyJ.jpg",folder=True)				   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
