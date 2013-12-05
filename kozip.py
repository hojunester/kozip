#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this script supports shift-jis and euc-kr encodings (basically, Microsoft's Korean and Japanese encoding.)


import sys, os, zipfile, argparse, platform

PARSER = argparse.ArgumentParser(
        description='unzip which supports shift-jis and euc-kr filename encodings')

PARSER.add_argument('file', default=None, type=str)
PARSER.add_argument('exdir', nargs='?', default=None, type=str)
PARSER.add_argument('lang', 
    nargs='?',
    default='euc-kr',
    choices=['euc-kr', 'shiftjis'],
    type=str)

def unzip(file, dir, lang):
    if dir is None:
        dir = os.path.splitext(file)[0]

    if os.path.exists(dir) is not True:
        os.mkdir(dir)

    if platform.python_version().startswith('3'):# workaround: just call on 7zp and fix the files later.
            #info.filename = bytes(info.filename, lang).encode('utf-8')
            os.system('env LANG=C 7z x %s -oc:%s' % (file, dir))
            os.system('convmv --notest -f %s -t utf-8 -r %s' % (lang, dir))
    else:
        for info in zfobj.infolist():
            zfobj = zipfile.ZipFile(file)
            info.filename =  info.filename.decode(lang).encode('utf-8')
            print('extracting %s' % info.filename)
            zfobj.extract(info, dir)

if __name__ == '__main__':
    args = PARSER.parse_args()
    unzip(args.file, args.exdir, args.lang)

# reference:

    #if sys.version_info < (3, 0):
        
        #info.filename = bytes(info.filename,lang).encode('utf-8')
    #else:
        #info.filename = info.filename.decode(lang).encode('utf-8')
# that bit of code was given to me by slaveriq on the jupiter broadcasting irc. I'll make tha the base of the future rewrite.