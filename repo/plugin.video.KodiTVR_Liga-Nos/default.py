# -*- coding: utf-8 -*- 
import sys 
import xbmcaddon, xbmcgui, xbmcplugin 
# Plugin Info

ADDON_ID      = 'plugin.video.KodiTVR_Liga-Nos'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')

YOUTUBE_CHANNEL_ID1 = "Add-on KodiTVR(Fuck_You_Grupeta)"
YOUTUBE_CHANNEL_ID2 = "slbenfica"
YOUTUBE_CHANNEL_ID3 = "SportingCP"
YOUTUBE_CHANNEL_ID4 = "fcporto"
YOUTUBE_CHANNEL_ID5 = "1921scbraga"
YOUTUBE_CHANNEL_ID6 = "VSCoficial"
YOUTUBE_CHANNEL_ID7 = "rafc1939"
YOUTUBE_CHANNEL_ID8 = "MarketingBoavista"
YOUTUBE_CHANNEL_ID9 = "FCFamalicao1931"
YOUTUBE_CHANNEL_ID10 = "UC1fMA-YLirbPBTs3mjuaUBQ"
YOUTUBE_CHANNEL_ID11 = "CDNacionalTV"
YOUTUBE_CHANNEL_ID12 = "UCkeEgKzqUIS_T4V1w-fOmOA"
YOUTUBE_CHANNEL_ID13 = "FCPF1950"
YOUTUBE_CHANNEL_ID14 = "GilVicenteFutebolC"
YOUTUBE_CHANNEL_ID15 = "MoreirenseFC38"
YOUTUBE_CHANNEL_ID16 = "UCj7TKcvf3y82tGW_0QZIiyQ"
YOUTUBE_CHANNEL_ID17 = "UCHtqrolH5tlrj4vB97kF-AA"
YOUTUBE_CHANNEL_ID18 = "cdtondela"
YOUTUBE_CHANNEL_ID19 = "TheCFBelenenses"
YOUTUBE_CHANNEL_ID20 = "*Segunda Liga Portuguesa(e S.C. Vila Real)*"
YOUTUBE_CHANNEL_ID21 = "academicaoaf"
YOUTUBE_CHANNEL_ID22 = "UCJYN6zWIQ5iO9JUoK2vd77w"
YOUTUBE_CHANNEL_ID23 = "webmasterLSC"
YOUTUBE_CHANNEL_ID24 = "GDEPraia"
YOUTUBE_CHANNEL_ID25 = "CDFeirense1918"
YOUTUBE_CHANNEL_ID26 = "FCAroucaOficial"
YOUTUBE_CHANNEL_ID27 = "UC6QUrvNjXlYj6cOtRpL-IbQ"
YOUTUBE_CHANNEL_ID28 = "UC7i9tYzX3DjiIVBoVcqXKtw"
YOUTUBE_CHANNEL_ID29 = "UCkU0iBsXJ6JxH0zE2QDXRhg"
YOUTUBE_CHANNEL_ID30 = "UCRYHkejS-vpVtSPMlxBGkhQ"
YOUTUBE_CHANNEL_ID31 = "UCBJLEXBu0Jw334iBrdOaEcQ"
YOUTUBE_CHANNEL_ID32 = "UCV7WROfx5_aIQNoXKsG4pLg"
YOUTUBE_CHANNEL_ID33 = "UCs2UKNwnvVwy3UtSjVO5yfg"
YOUTUBE_CHANNEL_ID34 = "tvfcpenafiel"
YOUTUBE_CHANNEL_ID35 = "UCO5SilnKmvajcWSh3YBZ79g"
YOUTUBE_CHANNEL_ID36 = "ClubeDesportivoMafra"
YOUTUBE_CHANNEL_ID37 = "mktvfc"
YOUTUBE_CHANNEL_ID38 = "FPFutebolOficial"
YOUTUBE_CHANNEL_ID39 = "UCsIoK3XP-cVcpoCC_SdjZdg"
YOUTUBE_CHANNEL_ID40 = "UCuIlu5oGIj1RzHOYmeSV5Eg"
YOUTUBE_CHANNEL_ID41 = "SCVilaReal"
YOUTUBE_CHANNEL_ID42 = "*Football - International*"
YOUTUBE_CHANNEL_ID43 = "realmadridcf"
YOUTUBE_CHANNEL_ID44 = "fcbarcelona"
YOUTUBE_CHANNEL_ID45 = "LiverpoolFC"
YOUTUBE_CHANNEL_ID46 = "UC6yW44UGJJBvYTlfC7CRg2Q"
YOUTUBE_CHANNEL_ID47 = "chelseafc"
YOUTUBE_CHANNEL_ID48 = "fcbayern"
YOUTUBE_CHANNEL_ID49 = "bvb"
YOUTUBE_CHANNEL_ID50 = "EintrachtMedia"
YOUTUBE_CHANNEL_ID51 = "werderbremen"
YOUTUBE_CHANNEL_ID52 = "milanchannel"
YOUTUBE_CHANNEL_ID53 = "juventus"
YOUTUBE_CHANNEL_ID54 = "INTER"
YOUTUBE_CHANNEL_ID55 = "asroma"
YOUTUBE_CHANNEL_ID56 = "clubatleticodemadrid"
YOUTUBE_CHANNEL_ID57 = "mcfcofficial"
YOUTUBE_CHANNEL_ID58 = "ArsenalTour"
YOUTUBE_CHANNEL_ID59 = "PSGofficiel"
YOUTUBE_CHANNEL_ID60 = "UCzHCZXmqIdjqRnpdp0l_T6g"
YOUTUBE_CHANNEL_ID61 = "ASMONACOFCSA"
YOUTUBE_CHANNEL_ID62 = "2galatasaray"
YOUTUBE_CHANNEL_ID63 = "FBSKTV"
YOUTUBE_CHANNEL_ID64 = "ajax"
YOUTUBE_CHANNEL_ID65 = "bocaentretenimientos"
YOUTUBE_CHANNEL_ID66 = "cariverplatetv"
YOUTUBE_CHANNEL_ID67 = "spursofficial"

def addDir(title, url, thumbnail,fanart,folder):
    liz=xbmcgui.ListItem(title)
    liz.setProperty('IsPlayable', 'false')
    liz.setInfo(type="Video", infoLabels={"label":title,"title":title} )
    liz.setArt({'thumb':thumbnail,'fanart':FANART})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)

if __name__ == '__main__':
   #addDir(title = "[COLORred]KodiTVR[/COLOR]  LIGA NOS",url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail = icon1,)

   addDir(title=" [COLORgold]---●★| ⚽️ KodiTVR *Primeira Liga* Channels ⚽️|★●---[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",thumbnail="https://i.imgur.com/PnCLBbA.png",fanart="",folder=True)
   addDir(title=" [COLOR lightskyblue]Sport Lisboa e Benfica [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjzSxx_y2GKfFZSzXNX_8cR4kag8GVmCtg29_J4uVo=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Sporting Clube de Portugal [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngx42x8UpciT6ReI3-iznMCEvvyVD7511uwXb6bKw=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FC Porto [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID4+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngASODO6HOlp05X8AcjHngDtTNPkp403dNvTRxzy_Q=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]SC Braga [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID5+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhWd5Pl7eqvsmnjrCa5Hlwni2bC2GvbPVVlJVBKtA=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Vitória SC[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID6+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniWilm110vOBMuSlFtIP-cp41EnjsF6KXwTjl4l_w=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Rio Ave Futebol Clube [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID7+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwng4kpQOVj2I5f_zhTLe3fQK480hTsH8xW8ZnBs-ug=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Boavista Futebol Clube[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID8+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjakFGRLbP_LWpnVBRAJxYXWyQQ-WP6851GNGdcFA=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Futebol Clube de Famalicão [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID9+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjZeGkBX9VtAx2cRNyo47RG8W8kQMeQ-9FnjaCbxQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Clube Desportivo Santa Clara, Açores[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwni46aeqNbGPl7ORz5WLnuqyQXSh2SIK2iekMtqMFw=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]CDNacionalTV[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID11+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhCX6cFogxBAqyLaJ0Pi4KA7YmEq9UbS7ZUpE_d=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]CS Maritimo[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID12+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniNIfwJ0Xm_tYWQCdM0Yw56EuBi7VCLz3Zm84gb=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FC Paços de Ferreira[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID13+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh2-WGNv6l_lgKO9p1_vdDMa6NlgNEHolcpm_Wu5A=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Gil Vicente[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID14+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhp0oOea-AEiLMAkD8BD4QfXfMP9HJIXLNQ8iFo=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]MOREIRENSE FUTEBOL CLUBE [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID15+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngfvuXcOHDB7GS2HzNlnYXr-KviOQVAXltehMVUPQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Oficial Portimonense Televisão[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID16+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniitm_kq4hhQ2b5XHFxt0Pas854ogZR_pOKUSo1zQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FARENSE TV[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID17+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngGq-WzFY9JzOL6Viy11z-8dEpv2FtQSLkaX-KE=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]CD Tondela[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID18+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngExzVQcHrYHXYhP5Hrx_NfrwEb3bxdSFRpXoYckQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Belém TV[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID19+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhdlB8-b36JsMZjadSi9zLC_y1-bjQLPB-KshEj=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR gold]---●★| ⚽️ KodiTVR *Segunda Liga* Channels ⚽️|★●---[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID20+"/",thumbnail="https://i.imgur.com/B4OpkDW.jpg",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]academicaoaf[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID21+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngMMnkmMjRphajWtJhZluVgnvT2X5NmBmDW0Yri=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Grupo Desportivo Chaves[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID22+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjJ_rveDVxsCao9Q9b2hj1cqLUVNM_ZWBemB-bp0A=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Leixões Sport Club[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID23+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhbOuerATSqMCKluT4jC8CD3nK2U9xEYVSNwv3x=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Grupo Desportivo Estoril Praia[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID24+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngOVyAnXuW_Bmqi4rNR0WYdNM0PVmytgfbZ_EQUnQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Clube Desportivo Feirense [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID25+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjZxujIJgTWGNnYGmDV4gL6hnpScA0epLpPk6RT4A=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FCAroucaOficial[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID26+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhVrkS5XX3hRhloefZryrcShEKrpnkISbps5Jxp=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Casa Pia AC Comunicação[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID27+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjQAKQURkELV-l61wRJHUL0dVj5cygeMjJ4f1KIJA=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]CD Cova Piedade[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID28+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnidt1mswBaKM-XJ6ayLtWtrpsEyVrHJfIJWnuUV=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]adeptos F.C. VIZELA [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID29+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjuPRWo3GUaQTOzJHWaakjE-QurEgBRVZt8uZA8=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )					   
   addDir(title=" [COLOR lightskyblue]Sporting Clube da Covilhã [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID30+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngjP1VLYBHB8JjQn_yNHN0FFBc2Phk_DXDRPZiH=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]União Desportiva Vilafranquense[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID31+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnglf-wp2JkWkGMAPGCmXY3AsI2Q2qaocL1skwXG=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Académico de Viseu Futebol Clube [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID32+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngHhVPGGeUv8GvkUhtbLGShQnJmjVENXDveaumc=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Varzim Sport Club Multimédia [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID33+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniXrWex4QwtRtcAUhfZ2Pyz0qLc6vCajuTFy0kD=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FC Penafiel [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID34+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjurnjKyCR_eUV46jaOVz0nWE5TshIHIqYxG7VZZg=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]UD Oliveirense [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID35+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhpw0VaQw8b4mVDo-XJvgbrxdC_2AUZgvKuVDIQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]ClubeDesportivoMafra[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID36+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniKfwcF7YrnFkhs93nXDi0Nu3ih8qcfLP8_SVSS=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Vitória Futebol Clube [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID37+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhNhUcIOEV_AJClAx5zRjYWc0OXIgH8mOVaMOMZjQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Canal11[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID38+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjfwCgUV9uLMgFIScqVV_YhGcRYRAYEyEi0dehd=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Federação Portuguesa de Futebol [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID39+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj_Oi9_lsJbI24yZay7u0aVX3yGKHu-w3aVwaln=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]VSPORTS - Liga NOS[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID40+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj7_HJavihTdjwmnNh2-y8J6uaOhk_6853Se2QFWA=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]SCVilaReal[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID41+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjpc-qRTjJ8udnfCeCAEI8cgziditd5d770IvcW=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLORgold]---●★| ⚽️ KodiTVR *Football - International* Channels ⚽️|★●---[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID42+"/",thumbnail="https://i.imgur.com/U2h6k0E.jpg",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Real Madrid[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID43+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjLWwm1cDoFo65P-dqKbmG45ozzrFgv87XdfdLnYa0=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FC Barcelona[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID44+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnilINlipkvw1ijwWsp_0I3YGmb_9bHk6TshlpYGzVM=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Liverpool FC [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID45+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhFDKPrdtata8maXMqPwhhC5sq_lJpEpZP76hUHk0o=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Manchester United[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID46+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwng1lhnPSqypAfQhEuoUeOyT6e3Yu9QoPh6QddCz0w=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Chelsea Football Club[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID47+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngV_tkwdihGaN2NulJrALp6itU0FtIbDyc49i3F2FY=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]FC Bayern München[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID48+"/",thumbnail="https://yt3.ggpht.com/-2Y_1_ERp2EE/AAAAAAAAAAI/AAAAAAAAAAA/WjpNzvZ-s_g/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Borussia Dortmund[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID49+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwni73kTBQcUzx6j4guzVE-71DW9hoU3Y1KfjKU9ukjc=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Eintracht Frankfurt[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID50+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwni0F0d8Vier5y1wEV07z2LnKcji93FTQsU0xEPiPpU=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Werder Bremen[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID51+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniTio3VIodty4s6_GmovPwz77brqJqEus3W5UiOb7I=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]AC Milan[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID52+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjueHi1ZtRb3hGwDSEC_NjCbB16PJARVF8lwm6PFXQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Juventus[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID53+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnj6QbT689dmT3xCfSPUGN8oBmMHQ3hXH9EzEnj4Imo=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Inter[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID54+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniN-SITdzcufUyT8AYwW8IHtT0prvgFfPibokpz5w=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]AS Roma [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID55+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngwX_cvj9lft0OlfYaUXc-8hWqjzr9XtCxHbdwuig=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Atlético de Madrid[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID56+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnh3gU9MAYRT-Y8NjBFsP7WypmfxC-h4tIQwR2gZjvU=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Man City[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID57+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhhZ0utnNy_q2zvrt_1uwfy-MAue6exlFO4ye-xo28=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Arsenal[/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID58+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnhtlTU4PV85s58rqOnGLRQP4p498PhQw_YxUCF6Y2Q=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]PSG - Paris Saint-Germain [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID59+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjgIjnDfoh_yW0iky4Tck-bHeLJ6fo0N18R1UfWUxs=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )					   
   addDir(title=" [COLOR lightskyblue]Olympique Lyonnais [/COLOR]",url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID60+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngKPWCsORbipbOfitDA8bLvEMSadWWOCuuGNAulgUg=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]AS MONACO[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID61+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniSrSnFhliYDmji0Z3EP_wJRjkZBj6G5yXtBOU6lQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Galatasaray [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID62+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnieXeDBee5gMzA9aiHfudpWQMEyOhvFhim3Un8oGYQ=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Fenerbahçe SK [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID63+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwngB8gx6HENrn4UZkcrkGqrUAW-wvNNTK8CDzM54hGA=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]AFC Ajax [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID64+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnig6NZKZRPR6C0DyIp1DGfj4cUk3uoBfMz4l89pew=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Club Atlético Boca Juniors [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID65+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwni5Hf_vRhFiUpxsX7w5y1UhjYSE1QvBV381c8rePw=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Club Atlético River Plate[/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID66+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwnjVH6m97wVSBG7KVzx17EV1_WwbQ4m0fFGZGyA97Q=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   addDir(title=" [COLOR lightskyblue]Tottenham Hotspur [/COLOR]",url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID67+"/",thumbnail="https://yt3.ggpht.com/ytc/AAUvwniWmCvWqErL14F1kNa7bgF_xoLOoeISQJ_4IXzfMsU=s88-c-k-c0x00ffffff-no-rj",fanart="",folder=True )
   xbmcplugin.endOfDirectory(int(sys.argv[1]),cacheToDisc=True)  