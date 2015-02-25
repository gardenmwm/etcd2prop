import json
import requests
import sys
import argparse
import pickle



parser = argparse.ArgumentParser(description='EtcD to Java properties file')
parser.add_argument('--server',action="store",dest='server',default="http://localhost:4001")
parser.add_argument('--base',action="store",dest='BASEDIR',default="/test/dev")
parser.add_argument('--confdir',action="store",dest='CONFDIR',default="/tmp/mydir")
parser.add_argument('--compare-only',action="store_true",dest='COMPAREONLY',default=False)
args=parser.parse_args()

ETCDSERVER=args.server
BASEDIR=args.BASEDIR
CONFDIR=args.CONFDIR
COMPAREONLY=args.COMPAREONLY
CACHEDIR='/var/cache/etcd2prop'



def getConfig():
    '''
    Loads all the configs from ETCD Server
    '''
    path=ETCDSERVER + '/v2/keys'+BASEDIR +'?recursive=true'
    r=requests.get(path)
    if r.status_code == 200:
        return r.json()
    else:
        exit()

def writepropfile(file,properties):
    '''
    Writes out the file
    '''
    with open(file, 'w+') as f:
        f.seek(0)
        for prop in properties['nodes']:
            propname=prop['key'][len(key['key'])+1:]
            propval=prop['value']
            f.write("%s=%s\n" % (propname , propval))
            f.truncate()
            f.close

def compare(conf):
    '''
    compares the key with the stored key
    '''
    with open("%s/props" %(CACHEDIR),'r') as handle:
        oldconf = pickle.load(handle)
    if cmp(oldconf,conf) != 0:
        print "NOT THE SAME, NOT THE SAME"
        exit(44)



conf=getConfig()
if COMPAREONLY:
    compare(conf)
else:
    for key in conf['node']['nodes']:
        filename=CONFDIR + '/' + key['key'][len(BASEDIR):]+'.properties'
        writepropfile(filename,key)
    pickle.dump(conf,open("%s/props" % (CACHEDIR),'w+'))
