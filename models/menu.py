# -*- coding: utf-8 -*-

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = "rece2py"
response.subtitle = "%s: %s" % (request.controller.capitalize(), request.function.capitalize())

response.meta.author = 'Mariano Reingart <reingart@gmail.com>'
response.meta.description = 'Regimen de Emision de Comprobantes Electronicos - Programa Webservice MATRIX'
response.meta.keywords = 'web2py, python, RECE, wsmtxca'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011 - Mariano Reingart - Licence AGPL v3'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('WSMTXCA'), False, URL('wsmtx','index'), [
        (T('Solicitar CAEA'), False, URL('wsmtx','solicitar_caea'), []),
        (T('Consultar CAEA'), False, URL('wsmtx','consultar_caea'), []),
    ]),
    (T('Facturas'), False, URL('facturas','index'), [
        (T('Informar'), False, URL('facturas','informar'), []),
        (T('Recuperar'), False, URL('facturas','recuperar'), []),
    ]),
    ]
