from odoo import models,fields,api

value_billing_potential=[
    ('1M - 10M','1M - 10M'),
    ('10M - 20M','10M - 20M'),
    ('20M - 50M','20M - 50M'),
    ('50M - 100M','50M - 100M'),
    ('100M - 500M','100M - 500M'),
    ('MÁS DE 500M','MÁS DE 500M')
]

type_tender=[
    ('PÚBLICA','PÚBLICA'),
    ('MÍNIMA CUANTÍA','MÍNIMA CUANTÍA'),
    ('DIRECTA','DIRECTA'),
    ('PRIVADA','PRIVADA'),
    ('SUBASTA','SUBASTA')
]
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

    #Grupo 2
    commercial_management_viability_approval=fields.Selection([('SI','SI'),('NO','NO')])

    #Grupo 3
    board_of_directors_approval=fields.Selection([('SI','SI'),('NO','NO')])

    #Grupo 4
    planned_closure=fields.Date(string='Cierre previsto', required=True)

    #Grupo 5
    billing_potential=fields.Selection(value_billing_potential, string='Potencial de facturación', required=True)

    #Licitación (etiqueta o pestaña nueva)
    #Grupo 6
    type_of_tender=fields.Selection(type_tenderm, string='Tipo de Licitación', required=True)

    #Grupo 7
    process_number=fields.Char('Número de proceso', required=True)
    object_=fields.Char('Objeto', required=True)
    budget=fields.Float('Presuouesto', widget='monetary', required=True)
    opening_date=fields.Date('Fecha de apertura', required=True)
    deadline=fields.Date('Fecha de cierre', required=True)

    #Union temporal (etiqueta o pestaña nueva)
    #Competidores
    competitors_id==fields.Many2one('competitors','Competidor', required=True)
