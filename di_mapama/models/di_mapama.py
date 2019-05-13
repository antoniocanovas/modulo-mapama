# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Nombre")
    active = fields.Boolean("Activo")
    image = fields.Binary()
    description = fields.Html(string="Descripción")

    def buscalibros(self):
        fields = ['name','active']
        libros=self.search_read(domain,fields,*kwars)




