from odoo import models,fields,api

class Competitors(models.Model):
    _name='competitors'
    _description='This module will modify CRM'

    name=fields.Char('Competidor')
    code=fields.Char('Code')
    weaknesses_id=fields.Many2one('weaknesses','Debilidades')
    strengths_id=fields.Many2one('strengths','Fortaleza')
