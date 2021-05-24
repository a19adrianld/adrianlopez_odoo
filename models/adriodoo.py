# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adriodoo(models.Model):
    _name = 'adrianlopez_odoo.adriodoo'
    _description = 'Prueba examen odoo'

    name = fields.Char(string="Hola mundo")

    autorizado = fields.Boolean(string="¿Autorizado?")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
