#!/usr/bin/python3

import os
import sys
import threading

runing = True

uvpath = '\"C:/Keil_v5/UV4/UV4.exe\" '

def readfile(logfile):
    with open(logfile, 'w') as f:
        pass
    with open(logfile, 'r') as f:
        while runing:
            line = f.readline(1000)
            if line != '':
                line = line.replace('\\', '/')
                print(line, end = '')

if __name__ == '__main__':
    modulePath = os.path.abspath(os.curdir)
    logfile = modulePath + '/build.log'
    cmd = uvpath
    for i in range(1, len(sys.argv)):
        cmd += sys.argv[i] + ' '
    cmd += '-j0 -o ' + logfile
    thread = threading.Thread(target=readfile, args=(logfile,))
    thread.start()
    code = os.system(cmd)
    runing = False
    thread.join()
    sys.exit(code)