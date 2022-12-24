#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ListVERSION = "1"

list = [ 'GE-Proton7-35', 'GE-Proton7-34','GE-Proton7-33', 'GE-Proton7-31', 'GE-Proton7-30', 'GE-Proton7-29', 'GE-Proton7-28','GE-Proton7-27', 'GE-Proton7-26', 'GE-Proton7-25', 'GE-Proton7-24', 'GE-Proton7-23', 'GE-Proton7-22', 'GE-Proton7-21' ]

ProtonDescription = { 
    'GE-Proton7-35': """
    * The Phantasy Star Online 2 update wasn't working properly. I've updated it and it's now working as expected (double checked on steam deck) -- Thanks Goldreaver"""
    ,
    'GE-Proton7-34': """
    * Phantasy Star Online 2 fixed (again)
    * Persona 4 Golden fixed (again) -- Thanks tgurr
    * GTA IV custom radio protonfix added -- Thanks xperia64
    * upstream WINE_HEAP_DELAY_FREE fix for CoD BO3 Multiplayer + zombies added
    * upstream LAA disable for Sword and Fairy 4 added
    * wine updated to latest bleeding edge
    * DXVK updated to latest git
    * vkd3d updated to latest git"""
    ,
    'GE-Proton7-33': """
    So I uh.. kind of sort of forgot to apply the GE patches + dxvk async patches to the 7-32 build. Whoops. Guess I should get coffee before pushing releases next time.
    Anyway, here's the correct build with all of the usual patches applied (don't use the 7-32 build, the Lutris Wine-GE 7-28 build is also fine).

    * wine updated to latest bleeding edge, pulls in more fixes for gta v, rdr2, verified bioshock remastered 1/2 + infinite work with 2k launcher
    * dxvk updated to latest git
    * vkd3d updated to latest git
    * pulled in latest proton script changes from upstream
    * fixed issue with fall guys protonfix trying to replace incorrect command name (Thanks Corben78)
    * removed Divinity Original Sin 2 launcher protonfix as it's no longer needed
    NOTE: for Divinity Original Sin 2 you will need to do the following to return the game files back to normal:

        Open the game folder
        delete the 'bin' symlink
        rename 'bin-bak' as 'bin'
        delete the 'Data' symlink
        rename 'Data-bak' as 'Data'
        Then in steam verify the integrity of the game files."""
    ,
    'GE-Proton7-32': "-edit- don't use this build"
    ,
    'GE-Proton7-31': """
    * FFXIV Launcher fixed (thanks Valve) 
    * GTA V fixes added (thanks Valve) 
    * NOSTEAM=1 envvar option available for Guild Wars 2. Use it the same way you do for ffxiv non-steam accounts: 
    * NOSTEAM=1 %command% 
    * dxvk updated to git 
    * vkd3d-proton updated to git  
    * wine updated to latest bleeding edge  
    * patches added for Visual Novel Doukyuusei"""
    , 
    'GE-Proton7-30': """
    Nothing major this release, just keeping things up to date

    * protonfix for Flatout Ultimate Carnage (single player only) added -- thanks Ranplayer
    * amazon games patch added (this is mainly for possible future compatibility, please use wine-ge for non-steam games)
    * wine-staging ddraw-Device_Caps and ddraw-version-check patchsets disabled in favor of new proton ddraw changes.
    * dxvk updated to latest git
    * vkd3d-proton updated to latest git
    * wine updated to latest bleeding-edge
    * upstream openxr patches applied"""
    ,
    'GE-Proton7-29': """ Changelog:
    """
    ,
    }
