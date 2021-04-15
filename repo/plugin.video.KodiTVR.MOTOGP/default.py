# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.MOTOGP'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "[COLORgreen]●[/COLOR]"
YOUTUBE_CHANNEL_ID2 = "MotoGP"
YOUTUBE_CHANNEL_ID3 = "[COLORgreen]●[/COLOR]"

def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "KodiTVR [COLOR red]MOTO[/COLOR]GP",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLORgreen]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/0e6ksDZ.png",fanart="https://i.imgur.com/vTmHiWP.jpg",folder=True)
   addDir(title=" [COLOR red]MotoGP[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngkqCZTqgdixXOxygR26-9XS_3QFLDeIyaHXrD_sgY=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/vTmHiWP.jpg",folder=True )
   addDir(title=" [COLORgreen]●[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://i.imgur.com/0e6ksDZ.png",fanart="https://i.imgur.com/vTmHiWP.jpg",folder=True )
   				   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
