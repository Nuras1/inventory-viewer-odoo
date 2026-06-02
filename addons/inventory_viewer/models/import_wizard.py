from odoo import models, fields
import requests


class InventoryImportWizard(models.TransientModel):
    _name = "inventory.import.wizard"
    _description = "Import Inventory"

    api_url = fields.Char(
        required=True
    )

    def action_import(self):

        response = requests.get(
            self.api_url,
            timeout=30
        )

        data = response.json()

        self.env["inventory.viewer"].create({
            "name": data["title"],
            "category": data["category"],
            "items_count": data["itemsCount"]
        })

        return {
            "type": "ir.actions.act_window_close"
        }