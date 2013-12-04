kozip
=====

Unzip zip files that contain file names that are encoded in non-utf-8 encodings. Supports japanese(shift-jis) and Korean(euc-kr).<br />


Currently, only works in python 2. I'm trying to rewrite the script to 
work in python 3, but it will take a while to do so.  

Usage: kozip.py [file] [target_directory] [lang]<br />
lang can be euc-kr, or shift-jis, depending on the language that you 
want to 
use.

Here is [an example](https://www.dropbox.com/s/t8wk3i4a386ia3t/test_files.zip "test_files.zip") file, containing files that have names encoded with EUC-KR. Try unzipping the file with the standard unzip command, and then try with the script. 
