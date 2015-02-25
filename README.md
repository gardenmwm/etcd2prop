# etcd2prop
Converts ETCD stores into java property files

Created this so I could move a bunch of java property files into etcd to allow devs to make config changes without access to the systems.


Usage:
```
etcd2prop --server <your etcd server> --base <ETCD Base path> --confdir <Where all configs will get dumped>
```
There is also compare only flag that returns 0 if everythin is the same, 44 otherwise
```
etcd2prop --compare-only --server <your etcd server> --base <ETCD Base path> --confdir <Where all configs will get dumped>
```

Todo:
* Add Config file
* Package scripts
* Better Error handling
