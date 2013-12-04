kozip
=====

Unzip zip files that contain file names that are encoded in non-utf-8 encodings. Supports japanese(shift-jis) and Korean(euc-kr).


Currently, only works in python 2. I'm trying to rewrite the script to 
work in python 3, but it will take a while to do so. 

Usage: kozip.py [file] [target_directory] [lang]
lang can be kor, or jap, depending on the language that you want to use.
