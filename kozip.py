#!/usr/bin/env python2
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
        info.filename =  info.filename.decode(lang).encode('utf-8')
        zfobj.extract(info, dir)

        print 'extracting', info.filename

if __name__ == '__main__':
    args = PARSER.parse_args()
    unzip(args.file, args.exdir, args.lang)
