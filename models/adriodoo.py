# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adrianlopez_odoo(models.Model):
    _name = 'adrianlopez_odoo.adrianlopez'
    _description = 'Prueba examen odoo'

    name = fields.Char(string="Hola mundo")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
