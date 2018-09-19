import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Ares Sergio Gracas Tools Install'
EXCLUDES       = [ADDON_ID, 'Kodish.repo.store']
# Text File with build info in it.
BUILDFILE      = 'https://pastebin.com/raw/EfZJzyrV'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://kodi.tv/'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Videos Tutoriais (Aprenda a Instalar Kodi e Build)'
YOUTUBEFILE    = 'http://sergiogracas.com/emular/kodi/conf/Youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONMAINT      = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONAPK        = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONADDONS     = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONYOUTUBE    = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONSAVE       = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONTRAKT      = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONREAL       = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONLOGIN      = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONCONTACT    = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
ICONSETTINGS   = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '//'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'red'
COLOR2         = 'blue'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']SGracas[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Build Atual:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Thema Atual:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Obrigado por escolher o Vikings Build.Inscreva-se em nosso canal no Youtbe:  http://www.youtube.com/c/VikingsArcades'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://sergiogracas.com/emular/kodi/imagens/icone.png'
CONTACTFANART  = 'http://sergiogracas.com/emular/kodi/imagens/fanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://pastebin.com/raw/EfZJzyrV'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://pastebin.com/raw/3QDVzEgz'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Painel de Noticias e Avisos Importantes da equipe Sergio Gracas'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################