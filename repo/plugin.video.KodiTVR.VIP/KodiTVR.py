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
import xbmc
import xbmcgui
import xbmcaddon
import os
import xbmcvfs

kodi = float(xbmc.getInfoLabel("System.BuildVersion")[:4])

if kodi > 19:
    import xbmcvfs as xbmc
else:
    import xbmc

addon = xbmcaddon.Addon(id='plugin.video.KodiTVR.VIP')
login1 = addon.getSetting('login')
password1 = addon.getSetting('password')

tv  = os.path.join(xbmc.translatePath("special://home/userdata/addon_data/pvr.iptvsimple/settings.xml"))


    

def main(login,password):
    dialog = xbmcgui.Dialog()
    menu = dialog.select('WELLCOME TO KodiTVR IPTV VIP', ['Pedir um Teste','Configurar o Login','EXTRA 1 [B][COLORred]●[/COLOR][/B] ON [B][COLORlime]●[/COLOR][/B] RADIO PT','EXTRA 2 [B][COLORred]●[/COLOR][/B] ON [B][COLORlime]●[/COLOR][/B] RADIO BR','EXTRA 3 [B][COLORred]●[/COLOR][/B] ON [B][COLORlime]●[/COLOR][/B] FOOTBALL CLUB'])

    if menu == 0:
        dialog = xbmcgui.Dialog()
        ok = dialog.ok('KodiTVR IPTV VIP', 'Para Gerar o Teste entrar em contacto pelo: https://www.facebook.com/KodiTVR/ ou e-mail: koditvr@gmail.com, twitter: @KodiTVR "Have fun with the stream"')

        dialog = xbmcgui.Dialog()
        ok = dialog.ok('KodiTVR IPTV VIP', 'Entre em contacto connosco para obter o teste de streaming by KodiTVR')

    if menu == 1:
        #dialog = xbmcgui.Dialog()
        #login = dialog.input('[COLOR lime]Digite o Username: [/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)

        #dialog = xbmcgui.Dialog()
        #password = dialog.input('[COLOR lime]Digite a Password: [/COLOR]','', type=xbmcgui.INPUT_ALPHANUM)

        file = open(tv,"w") 

        file.write("<settings version=\"2\">\n") 
        file.write("    <setting id=\"m3uPathType\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"m3uPath\" default=\"true\" />\n") 
        file.write("    <setting id=\"m3uUrl\">http://pt.mv2.link:8080/get.php?username="+login+"&amp;password="+password+"&amp;type=m3u_plus&amp;output=ts</setting>\n") 
        file.write("    <setting id=\"m3uCache\">false</setting>\n") 
        file.write("    <setting id=\"startNum\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"numberByOrder\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"m3uRefreshMode\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"m3uRefreshIntervalMins\" default=\"true\">60</setting>\n") 
        file.write("    <setting id=\"m3uRefreshHour\" default=\"true\">4</setting>\n") 
        file.write("    <setting id=\"tvGroupMode\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"numTvGroups\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"oneTvGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"twoTvGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"threeTvGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"fourTvGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"fiveTvGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"customTvGroupsFile\" default=\"true\">special://userdata/addon_data/pvr.iptvsimple/channelGroups/customTVGroups-example.xml</setting>\n") 
        file.write("    <setting id=\"tvChannelGroupsOnly\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"radioGroupMode\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"numRadioGroups\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"oneRadioGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"twoRadioGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"threeRadioGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"fourRadioGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"fiveRadioGroup\" default=\"true\" />\n") 
        file.write("    <setting id=\"customRadioGroupsFile\" default=\"true\">special://userdata/addon_data/pvr.iptvsimple/channelGroups/customRadioGroups-example.xml</setting>\n") 
        file.write("    <setting id=\"radioChannelGroupsOnly\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"epgPathType\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"epgPath\" default=\"true\" />\n") 
        file.write("    <setting id=\"epgUrl\">http://pt.mv2.link:8080/xmltv.php?username="+login+"&amp;password="+password+"&amp;type=m3u_plus&amp;output=ts</setting>\n") 
        file.write("    <setting id=\"epgCache\" default=\"true\">true</setting>\n") 
        file.write("    <setting id=\"epgTimeShift\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"epgTSOverride\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"useEpgGenreText\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"genresPathType\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"genresPath\" default=\"true\">special://userdata/addon_data/pvr.iptvsimple/genres/genreTextMappings/genres.xml</setting>\n") 
        file.write("    <setting id=\"genresUrl\" default=\"true\" />\n") 
        file.write("    <setting id=\"logoPathType\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"logoPath\" default=\"true\" />\n") 
        file.write("    <setting id=\"logoBaseUrl\" default=\"true\" />\n") 
        file.write("    <setting id=\"logoFromEpg\" default=\"true\">1</setting>\n") 
        file.write("    <setting id=\"timeshiftEnabled\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"timeshiftEnabledAll\" default=\"true\">true</setting>\n") 
        file.write("    <setting id=\"timeshiftEnabledHttp\" default=\"true\">true</setting>\n") 
        file.write("    <setting id=\"timeshiftEnabledUdp\" default=\"true\">true</setting>\n") 
        file.write("    <setting id=\"timeshiftEnabledCustom\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"catchupEnabled\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"catchupQueryFormat\" default=\"true\" />\n") 
        file.write("    <setting id=\"catchupDays\" default=\"true\">5</setting>\n") 
        file.write("    <setting id=\"allChannelsCatchupMode\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"catchupOverrideMode\" default=\"true\">0</setting>\n") 
        file.write("    <setting id=\"catchupPlayEpgAsLive\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"catchupWatchEpgBeginBufferMins\" default=\"true\">5</setting>\n") 
        file.write("    <setting id=\"catchupWatchEpgEndBufferMins\" default=\"true\">15</setting>\n") 
        file.write("    <setting id=\"catchupOnlyOnFinishedProgrammes\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"transformMulticastStreamUrls\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"udpxyHost\" default=\"true\">127.0.0.1</setting>\n") 
        file.write("    <setting id=\"udpxyPort\" default=\"true\">4022</setting>\n") 
        file.write("    <setting id=\"useFFmpegReconnect\" default=\"true\">true</setting>\n") 
        file.write("    <setting id=\"useInputstreamAdaptiveforHls\" default=\"true\">false</setting>\n") 
        file.write("    <setting id=\"defaultUserAgent\" default=\"true\" />\n") 
        file.write("    <setting id=\"defaultInputstream\" default=\"true\" />\n") 
        file.write("    <setting id=\"defaultMimeType\" default=\"true\" />\n") 
        file.write("</settings>\n") 
        file.close()

        dialog = xbmcgui.Dialog()
        ok = dialog.ok('KodiTVR IPTV VIP', 'Password Colocada com sucesso precisa reniciar o Kodi. E depois entrar na aba TV para que os canais sejam carregados')


    if menu == 2:
        import radiopt
        radiopt.radio_pt()

    if menu == 3:
        import radiobr
        radiobr.radio_br()

    if menu == 4:
        import footballclub
        footballclub.football_club()        

        
login = login1
password = password1

main(login,password)
