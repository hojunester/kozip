#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# this script supports shift-jis and euc-kr encodings (basically, Microsoft's Korean and Japanese encoding.)


import sys, os, zipfile, argparse

PARSER = argparse.ArgumentParser(
        description='unzip which supports shift-jis and euc-kr filename encodings')

PARSER.add_argument('file', default=None, type=str)
PARSER.add_argument('exdir', nargs='?', default=None, type=str)
PARSER.add_argument('lang', 
    nargs='?',
    default='euc-kr',
    choices=['euc-kr', 'shift-jis'],
    type=str)

def unzip(file, dir, lang):
    if dir is None:
        dir = os.path.splitext(file)[0]
        os.mkdir(dir)
    else:
        os.mkdir(dir)

    zfobj = zipfile.ZipFile(file)
    for info in zfobj.infolist():
        if sys.version_info < (3.0):
            info.filename =  info.filename.decode(lang).encode('utf-8')
        else:
            info.filename = bytes(info.filename, lang).encode('utf-8')

        print('extracting %s' % info.filename)

if __name__ == '__main__':
    args = PARSER.parse_args()
    unzip(args.file, args.exdir, args.lang)

# reference:

    #if sys.version_info < (3, 0):
        
        #info.filename = bytes(info.filename,lang).encode('utf-8')
    #else:
        #info.filename = info.filename.decode(lang).encode('utf-8')
# that bit of code was given to me by slaveriq on the jupiter broadcasting irc. I'll make tha the base of the future rewrite.