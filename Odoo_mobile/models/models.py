# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mobile(models.Model):
      _name = 'mobile.mobile'

      name_cel = fields.Char('nome_model',    required=True)
      tipo = fields.Char('id_model',    required=True)
#      value2 = fields.Float(compute="_value_pc", store=True)
#      description = fields.Text()
