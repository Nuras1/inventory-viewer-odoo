from odoo import models, fields


class InventoryImportWizard(models.TransientModel):
    _name = "inventory.import.wizard"
    _description = "Import Inventory"

    api_url = fields.Char(
        required=True
    )

    def action_import(self):
        return True