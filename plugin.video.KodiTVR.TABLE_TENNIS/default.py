# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR.TABLE_TENNIS'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = " ● "
YOUTUBE_CHANNEL_ID2 = "UCSUHcNZ91UkK89XxZ26j74Q"
YOUTUBE_CHANNEL_ID3 = "ittfchannel"
YOUTUBE_CHANNEL_ID4 = "UCSdlsyWvr-EriabK13fZWSQ"
YOUTUBE_CHANNEL_ID5 = "usatabletennis"
YOUTUBE_CHANNEL_ID6 = " ● "
def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLOR blue]KodiTVR[/COLOR] TABLE [COLOR chocolate]TENNIS[/COLOR]",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/b6RLwsj.png",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True)
   addDir(title=" [COLOR gold]Official Table Tennis Channel[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngcIAHzz7O4vEDDMdRlJsaf8Fwvpys0kjVDlRmx_g=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True )
   addDir(title=" [COLOR gold]World Table Tennis[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj7URmLPXNeOgibVTjTtAWp2l0sTFiaxmCneUwY3A=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True )
   addDir(title=" [COLOR gold]Table Tennis Central[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngYz8aU4kIZMLmK0YWfX9_8ITraZHIsDAlaMuba=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True )
   addDir(title=" [COLOR gold]USA Table Tennis[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjtvMbue-7oy2uOkptc_s0okeIobzpHTCeu2-_7Nw=s88-c-k-c0x00ffffff-no-rj",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True )					   
   addDir(title=" [COLOR green]●[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",thumbnail="https://i.imgur.com/b6RLwsj.png",fanart="https://i.imgur.com/oKVjcgi.jpg",folder=True )
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)
