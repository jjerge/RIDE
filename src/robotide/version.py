# Automatically generated by 'package.py' script.

VERSION = '0.35'
RELEASE = 'final'
TIMESTAMP = '20110413-153258'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE
