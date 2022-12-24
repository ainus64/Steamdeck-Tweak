#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################################################
## Imports 
#################################################################################

#################################################################################

#################################################################################
## Variables and system folder 
#################################################################################
#download_dir = "/mnt/Juegos/tmp/proton"
#install_dir = "/mnt/Juegos/tmp/installation"
#################################################################################

#################################################################################
## Download, install, uninstall Class
#################################################################################
class protonClass:
    def __init__(self):
        print("Module_lib loaded")
    def download(self, ProtonGE_Release, download_dir):
        # Esto funciona pero podría estar mejor.
        url = 'https://github.com/GloriousEggroll/proton-ge-custom/releases/download/' + ProtonGE_Release + '/' + ProtonGE_Release + '.tar.gz'
        ####
        start_download = wget.download(url, out=download_dir)
        start_download

    def install(self, ProtonGE_Release, download_dir):
        print("Install...")
    def unInstall(self, ProtonGE_Release):
        print("Uninstall..")


#################################################################################

