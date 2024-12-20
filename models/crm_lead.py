from odoo import models, fields, api

class CrmLeadInh(models.Model):
    _inherit = 'crm.lead'    
    _description = "Lead/Opportunity"
    _order = "priority desc, id desc"
    
    name = fields.Char(
        'Opportunity', index='trigram', required=True,
        compute='_compute_name', readonly=False, store=True) 
    first_name = fields.Char(string='Prénom', help="Prénom de l'utilisateur")
    last_name = fields.Char(string='Nom', help="Nom de l'utilisateur")
    location = fields.Char(string='Localisation', help="Localisation de l'utilisateur")
    

    # @api.model
    # def _get_stages_to_delete(self): 
    #     self.env.cr.execute("""
    #         DELETE FROM crm_stage
    #         WHERE sequence NOT IN (10,11)
    #     """)

    # @api.model
    # def browse(self, ids):
    #     # Exécuter la suppression des étapes non souhaitées quand un lead est ouvert
    #     self._get_stages_to_delete() 
    #     # Appel de la méthode browse pour obtenir les enregistrements
    #     return super(CrmLeadInh, self).browse(ids)
