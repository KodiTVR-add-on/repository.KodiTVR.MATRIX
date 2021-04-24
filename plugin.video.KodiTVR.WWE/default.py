# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.WWE'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "[COLORgreen]●[/COLOR]"
YOUTUBE_CHANNEL_ID2 = "UCJ5v_MCY6GNUBTO8-D3XoAg"
YOUTUBE_CHANNEL_ID3 = "TNAwrestling"
YOUTUBE_CHANNEL_ID4 = "WWEFanNation"
YOUTUBE_CHANNEL_ID5 = "[COLORgreen]●[/COLOR]"

def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR red]KodiTVR[/COLOR] [COLOR skylightblue]WRESTLING[/COLOR]",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLORgreen]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/SoHE1oA.png",fanart="https://i.imgur.com/AFcDQp6.jpg",folder=True)
   addDir(title=" [COLOR yellow]WWE[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhQZApiFpRRw4X6IWEDw3Vutq7qG6prfB0MApsbus4=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/AFcDQp6.jpg",folder=True )
   addDir(title=" [COLOR yellow]TNA WRESTLING[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://yt3.ggpht.com/a/AATXAJyx6Ru-5W3RBJHWe-TC9fFspjNKGlZ5PuYttg=s288-c-k-c0xffffffff-no-rj-mo",fanart="https://i.imgur.com/AFcDQp6.jpg",folder=True )
   addDir(title=" [COLOR yellow]WWE[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail="https://yt3.ggpht.com/a-/AN66SAx_23YzwxBkenlfs35ly3_BWP_5F8Trmmx0zA=s288-mo-c-c0xffffffff-rj-k-no",fanart="https://i.imgur.com/AFcDQp6.jpg",folder=True )
   addDir(title=" [COLORgreen]●[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",thumbnail="https://i.imgur.com/SoHE1oA.png",fanart="https://i.imgur.com/AFcDQp6.jpg",folder=True )
   				   
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
