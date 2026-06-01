from odoo import models, fields

class InventoryImportWizard(models.TransientModel):
    _name = "inventory.import.wizard"
    _description = "Import Inventory"

    api_token = fields.Char(
        string="API Token",
        required=True
    )