# Automatically generated by 'package.py' script.

VERSION = 'trunk'
RELEASE = '20110808'
TIMESTAMP = '20110808-163036'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE
