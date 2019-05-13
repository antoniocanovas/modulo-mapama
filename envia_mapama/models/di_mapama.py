# -*- coding: utf-8 -*-

from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport
from zeep import xsd
from datetime import datetime
import xmlrpc.client

from odoo import models, fields, api


class DiMapama(models.Model):
    _inherit = 'x_dis'
    _name = "DiMapama"

    x_di_mapamaname = fields.Char(string="Estado Modulo Mapama")







