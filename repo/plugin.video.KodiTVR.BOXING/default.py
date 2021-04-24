# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.BOXING'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = " ● "
YOUTUBE_CHANNEL_ID2 = "UCAaZm4GcWqDg8358LIx3kmw"
YOUTUBE_CHANNEL_ID3 = "HBOsports"
YOUTUBE_CHANNEL_ID4 = " ● "

def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR chocolate][B]KodiTVR[/B][/COLOR] BOXING",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/sJIh5MS.png",fanart="https://i.imgur.com/7ZcGsc7.jpg",folder=True)
   addDir(title=" [COLOR chocolate]The World of Boxing![/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniE_brt1LokpU3TTlWxDG2NmnjioJn8peeaaSpkWg=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/7ZcGsc7.jpg",folder=True )
   addDir(title=" [COLOR chocolate]BOXING[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://yt3.ggpht.com/-xspd8uYupTc/AAAAAAAAAAI/AAAAAAAAAAA/UTwanzEE9iM/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg",fanart="https://i.imgur.com/7ZcGsc7.jpg",folder=True )
   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail="https://i.imgur.com/sJIh5MS.png",fanart="https://i.imgur.com/7ZcGsc7.jpg",folder=True )
   					   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
