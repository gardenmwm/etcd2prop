#!/usr/bin/python
import requests as r
import argparse

parser=argparse.ArgumentParser(description='Send to ETCD')
parser.add_argument('--server',action="store",dest='server',default="http://localhost:4001")
parser.add_argument('--base',action="store",dest='BASEDIR',default="/test/dev")
parser.add_argument('--file',action="store",dest='filetoparse')
args=parser.parse_args()

def sendline(filename,key,value):
    url="%sv2/keys%s/%s/%s" %(args.server, args.BASEDIR, filename, key)
    print url
    req = r.post(url,data={'value':value})
    print req.text


propfile=args.filetoparse.split('.')[0]
with open(args.filetoparse,'r') as f:
    for line in f:
        prop=line.strip().split('=')
        sendline(propfile,prop[0].strip(),prop[1].strip())

