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
import webbrowser


def radio_br():    
    dialog = xbmcgui.Dialog()
    ret2 = dialog.select('[COLOR yellow][B]RADIOS BR[/B][/COLOR]', ['89 FM Radio Rock','97 Rock Web Radio','Difusora FM Riberao Preto','Alfa FM','Band Vale','Nova Brasil FM','Antena 1','Radio 91 Rock','Dumont FM','Radio Farropilha','New Life','Zebu FM','80 FM','Billboard Radio','Back to the 80s','Jazz Groove','Radio Sertaneja Raiz','Mix FM','Kiss FM','Radio FG','Radio Coca-Cola','','Pagina 2'])

    if ret2 == 0:
        link = "https://ice.fabricahost.com.br/89aradiorocksp"
        xbmc.Player().play(""+link+"")

    if ret2 == 1:
        link = "http://euroticast5.euroti.com.br:8094/stream?1591838091356"
        xbmc.Player().play(""+link+"")

    if ret2 == 2:
        link = "https://ice.fabricahost.com.br/difusorathathi"
        xbmc.Player().play(""+link+"")

    if ret2 == 3:
        link = "https://ice.fabricahost.com.br/alphafm1017"
        xbmc.Player().play(""+link+"")

    if ret2 == 4:
        link = "http://162.244.80.106:11011/;?1591838520552"
        xbmc.Player().play(""+link+"")

    if ret2 == 5:
        link = "https://playerservices.streamtheworld.com/api/livestream-redirect/NOVABRASIL_SPAAC.aac"
        xbmc.Player().play(""+link+"")

    if ret2 == 6:
        dialog = xbmcgui.Dialog()
        link2 = dialog.select('Antena 1', ['SP','RJ'])

        if link2 == 0:
            linku = "https://antenaone.crossradio.com.br/stream/1"
            xbmc.Player().play(""+linku+"")

        if link2 == 1:
            linku = "http://a1rj.streams.com.br:7801/stream?1591838836711"
            xbmc.Player().play(""+linku+"")

    if ret2 == 7:
        link = "https://servidor40.brlogic.com:8044/live"
        xbmc.Player().play(""+link+"")

    if ret2 == 8:
        link = "http://rrdns-dumont.webnow.com.br/dumont.aac"
        xbmc.Player().play(""+link+"")

    if ret2 == 9:
        link = "https://1592747t.ha.azioncdn.net/primary/far_poa.sdp/playlist.m3u8"
        xbmc.Player().play(""+link+"")

    if ret2 == 10:
        link = "http://cast4.zadax.com.br:8013/live?1590248253382"
        xbmc.Player().play(""+link+"")

    if ret2 == 11:
        link = "http://r13.ciclano.io:8771/stream"
        xbmc.Player().play(""+link+"")

    if ret2 == 12:
        link = "http://104.247.221.130:9020/stream1"
        xbmc.Player().play(""+link+"")

    if ret2 == 13:
        link = "http://billboardradio.rastream.com/gfm-awesome80s"
        xbmc.Player().play(""+link+"")

    if ret2 == 14:
        link = "http://s1.nexuscast.com:8135/;"
        xbmc.Player().play(""+link+"")

    if ret2 == 15:
        link = "http://mp3-128.streamthejazzgroove.com/;"
        xbmc.Player().play(""+link+"")

    if ret2 == 16:
        link = "http://cast.midiaip.com.br:8330/1;"
        xbmc.Player().play(""+link+"")

    if ret2 == 17:
        link = "https://shout12.crossradio.com.br:18002/1;"
        xbmc.Player().play(""+link+"")

    if ret2 == 18:
        dialog = xbmcgui.Dialog()
        link3 = dialog.select('Kiss FM', ['Sao Paulo','Brasilia','Litoral','Campinas','Rio de Janeiro'])

        if link3 == 0:
            linku2 = "http://stm15.sateg.com.br:23538/stream?1591840998833"
            xbmc.Player().play(""+linku2+"")

        if link3 == 1:
            linku2 = "http://cloud2.cdnseguro.com:23538/stream?1591841243117"
            xbmc.Player().play(""+linku2+"")

        if link3 == 2:
            linku2 = "http://stm18.sateg.com.br:18618/stream?1591841333250"
            xbmc.Player().play(""+linku2+"")

        if link3 == 3:
            linku2 = "http://stm43.sateg.com.br:24462/stream?1591841470628"
            xbmc.Player().play(""+linku2+"")

        if link3 == 4:
            linku2 = "http://cloud2.cdnseguro.com:23538/stream?1591841551315"
            xbmc.Player().play(""+linku2+"")

    if ret2 == 19:
        dialog = xbmcgui.Dialog()
        link4 = dialog.select('Radio FG', ['Radio FG','Radio FG Chic','Radio FG Deep Dance','Radio FG Starter','Radio FG Underground'])

        if link4 == 0:
            linku2 = "http://radiofg.impek.com/fg?1591840109054"
            xbmc.Player().play(""+linku2+"")

        if link4 == 1:
            linku2 = "http://radiofg.impek.com/fgc?1591840253511"
            xbmc.Player().play(""+linku2+"")

        if link4 == 2:
            linku2 = "http://radiofg.impek.com/fgd?1591840367116"
            xbmc.Player().play(""+linku2+"")

        if link4 == 3:
            linku2 = "http://radiofg.impek.com/fgv?1591840461801"
            xbmc.Player().play(""+linku2+"")

        if link4 == 4:
            linku2 = "http://radiofg.impek.com/ufg?1591840514289"
            xbmc.Player().play(""+linku2+"")


    if ret2 == 20:
        link = "http://listen.181fm.com:7080/181-power_128k.mp3"
        xbmc.Player().play(""+link+"")

    if ret2 == 22:
        dialog = xbmcgui.Dialog()
        link5 = dialog.select('[COLOR yellow][B]Melhores Radios Top Pagina 2[/B][/COLOR]', ['Radio Brega','Radio Relax','Radio Anos 80s','Dance Music Anos 2000','Radio as Velhinhas','Flash Disco Dance','Flash Disco Dance Anos 80','Radio Corigao','Radio Rock On','Classic Metal Radio','Power K-pop','Villa Mix','Radio Contact 102.2 FM','Webradio Webnovelas','Jovem Pan SP','Alvorada FM (Belo Horizonte)','Spaco FM (Farropilha)','','','','Pagina 3'])

        if link5 == 0:
            linku3 = "http://azura.sk7.org:8090/radio.mp3"
            xbmc.Player().play(""+linku3+"")

        if link5 == 1:
            linku3 = "http://paineldj6.com.br:8049/stream"
            xbmc.Player().play(""+linku3+"")

        if link5 == 2:
            linku3 = "http://live2.livemus.com.br:27400/;"
            xbmc.Player().play(""+linku3+"")

        if link5 == 3:
            linku3 = "http://209.133.210.170:8190/;"
            xbmc.Player().play(""+linku3+"")

        if link5 == 4:
            linku3 = "http://stm18.xcast.com.br:7916/;"
            xbmc.Player().play(""+linku3+"")

        if link5 == 5:
            linku3 = "http://103.195.100.65:21764/128AAC"
            xbmc.Player().play(""+linku3+"")

        if link5 == 6:
            linku3 = "http://103.195.100.65:6676/;"
            xbmc.Player().play(""+linku3+"")

        if link5 == 7:
            linku3 = "https://s18.hstbr.net:8010/live"
            xbmc.Player().play(""+linku3+"")

        if link5 == 8:
            linku3 = "http://streaming.radiostreamlive.com/radiorockon_devices"
            xbmc.Player().play(""+linku3+"")

        if link5 == 9:
            linku3 = "http://hazel.torontocast.com:2280/stream"
            xbmc.Player().play(""+linku3+"")

        if link5 == 10:
            linku3 = "http://stm11.srvstm.com:12710/;"
            xbmc.Player().play(""+linku3+"")

        if link5 == 11:
            linku3 = "http://198.100.150.244:9627/stream"
            xbmc.Player().play(""+linku3+"")

        if link5 == 12:
            linku3 = "http://radiocontact.ice.infomaniak.ch/radiocontact-mp3-128.mp3?1592923135201"
            xbmc.Player().play(""+linku3+"")

        if link5 == 13:
            linku3 = "http://91.121.155.140:18762/;"
            xbmc.Player().play(""+linku3+"")
            
        if link5 == 14:
            linku3 = "https://19293.live.streamtheworld.com/JP_SP_FM_SC"
            xbmc.Player().play(""+linku3+"")   

        if link5 == 15:
            linku3 = "https://20283.live.streamtheworld.com/RADIO_ALVORADAAAC.aac?dist=triton-widget&tdsdk=js-2.9&pname=tdwidgets&pversion=2.9&banners=none&sbmid=019bd986-bfa2-45e2-91c3-899423afeced"
            xbmc.Player().play(""+linku3+"")   

        if link5 == 16:
            linku3 = "https://stream.spacofm.com.br:8787/spacofm"
            xbmc.Player().play(""+linku3+"")          
            
       
        
