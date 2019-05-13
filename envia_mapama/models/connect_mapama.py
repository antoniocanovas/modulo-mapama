# -*- coding: utf-8 -*-

from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from datetime import datetime
import xmlrpc.client

from odoo import models, fields, api


class Connect_Mapama(models.Model):
    _name = 'ConnectMapama'


    x_di_mapama_estado = fields.Char(string="Estado Modulo Mapama")







