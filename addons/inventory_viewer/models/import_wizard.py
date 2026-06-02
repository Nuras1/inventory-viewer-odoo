from odoo import models, fields
import requests


class InventoryImportWizard(models.TransientModel):
    _name = "inventory.import.wizard"
    _description = "Import Inventory"

    api_url = fields.Char(required=True)

    def action_import(self):

        response = requests.get(self.api_url)

        data = response.json()

        print(data)

        return True