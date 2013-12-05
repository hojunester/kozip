kozip
=====

Unzip zip files that contain file names that are encoded in non-utf-8 encodings. Supports japanese(shift-jis) and Korean(euc-kr).<br />


Added initial support for python 3. However, it isn't implemented in 
pure python. The python3 code currently just calls on system commands to 
unzip the files first and then fix the file names. Rewrite needed,  

Usage: kozip.py [file] [target_directory] [lang]<br />
lang can be euc-kr, or shiftjis, depending on the language that you want 
to 
use.

Here is [an example](https://www.dropbox.com/s/t8wk3i4a386ia3t/test_files.zip "test_files.zip") file, containing files that have names encoded with EUC-KR. Try unzipping the file with the standard unzip command, and then try with the script. 
