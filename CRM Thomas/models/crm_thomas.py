from odoo import models,fields,api

class CrmThomas(models.Model):
    _inherit = 'crm.lead'

    #Existente 1

    benefit_center_id=fields.Many2one('benefit.center','Centro de Beneficio', required=True)
    segment_id=fields.Many2one('segment','Segmento', required=True)
    business_units_id=fields.Many2one('business.units','Unidad de Negocio', required=True)

    #Existente 2

    tender_status=fields.Selection([('PRE-PLIEGO', 'PRE-PLIEGO'),('PLIEGO', 'PLIEGO'),('SUBASTA.', 'SUBASTA.')])

    #Existente 3

    #Motivo de perdida

    contact_for_personnel_change=fields.Char()
    competitors_id=fields.Many2one('competitors','Competidor ganador')
    winning_price=fields.Float('Precio ganador', widget='monetary')
    required_time=fields.Char('Tiempo requerido')
    time_offered_by_thomas=fields.Char('Tiempo ofertado por Thomas')
    requirements_not_met=fields.Char('Requisitos no cumplidos')
    #Grupo 1
    opportunity_situation=fields.Char('Situación de la Oportunidad', required=True)
