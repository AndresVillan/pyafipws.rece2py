# coding: utf8

import pyafipws

if not session.token:
    wsaa = pyafipws.autenticar(service="wsmtxca")
    session.token = wsaa.Token
    session.sign = wsaa.Sign

wsmtxca = pyafipws.WSMTXCA()
wsmtxca.Cuit = 20267565393
wsmtxca.Token = session.token
wsmtxca.Sign = session.sign

def consultar_caea(): 
    form = SQLFORM.factory(
        Field("periodo", "string", 
            label="Período", 
            default=201112, 
            comment="Año + Mes (AAAAMMM)"),
        Field("orden", "string", 
            label="Orden", 
            default=1, 
            comment="Quincena (1 o 2)"),
        )
    caea = None
    if form.accepts(request.vars, session, keepvalues=True):
        wsmtxca.Conectar()
        caea = wsmtxca.ConsultarCAEA(form.vars.periodo, form.vars.orden)
        
    return dict(form=form, caea=caea)

def solicitar_caea(): 
    form = SQLFORM.factory(
        Field("periodo", "string", 
            label="Período", 
            default=201201, 
            comment="Año + Mes (AAAAMMM)"),
        Field("orden", "string", 
            label="Orden", 
            default=1, 
            comment="Quincena (1 o 2)"),
        )
    caea = None
    errores = None
    if form.accepts(request.vars, session, keepvalues=True):
        wsmtxca.Conectar()
        caea = wsmtxca.SolicitarCAEA(form.vars.periodo, form.vars.orden)
        errores = wsmtxca.Errores

        
    return dict(form=form, caea=caea, errores=errores)
