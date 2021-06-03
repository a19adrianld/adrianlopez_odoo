# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adriodoo(models.Model):
    _name = 'adrianlopez_odoo.adriodoo'
    _description = 'Prueba examen odoo'

    #name = fields.Char(string="Hola mundo")
    name = fields.Char(required=True, size=20, string="Suceso")
    descripcion = fields.Text(string="A Descripción do Suceso")  # string é a etiqueta do campo
    nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')
    data_hora = fields.Datetime(string="Data e Hora", default=lambda self: fields.Datetime.now())

    #autorizado = fields.Boolean(string="¿Autorizado?")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
