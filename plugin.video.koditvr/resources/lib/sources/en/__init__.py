# -*- coding: utf-8 -*-

'''
	KodiTVR Add-on
    Copyright (C) 2021 Mod by KodiTVR

    THE BEERWARE LICENSE (Revision 42)
    KodiTVR (Mod) wrote this file. wrote this file. As long as you retain this notice you
	can do whatever you want with this stuff. If we meet some day, and you think
	this stuff is worth it, you can buy me a beer in return.
'''

import os

files = os.listdir(os.path.dirname(__file__))
__all__ = [filename[:-3] for filename in files if not filename.startswith('__') and filename.endswith('.py')]
