#!/usr/bin/env python
# coding: utf8

import sys

# WRAPPER

# configurar ruta a la librería:

PYAFIPWS_PATH = "/home/reingart/pyafipws"
CERT = PYAFIPWS_PATH + "/reingart.crt"
PKEY = PYAFIPWS_PATH + "/reingart.key"

if PYAFIPWS_PATH not in sys.path:
    sys.path.append(PYAFIPWS_PATH)

from wsaa import WSAA
from wsmtx import WSMTXCA

def autenticar(service="wsfe", cert=CERT, pkey=PKEY, url=""):
    wsaa = WSAA()
    tra = wsaa.CreateTRA(service)
    cms = wsaa.SignTRA(tra, cert, pkey)
    wsaa.Conectar("", url)
    ta = wsaa.LoginCMS(cms)        
    return wsaa
