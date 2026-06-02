from odoo import models, fields
import requests


class InventoryImportWizard(models.TransientModel):
    _name = "inventory.import.wizard"

    api_url = fields.Char(required=True)

    def action_import(self):

        response = requests.get(self.api_url)

        data = response.json()

        inventory = self.env["inventory.viewer"].create({
            "name": data.get("title"),
            "category": data.get("category"),
            "items_count": data.get("itemsCount"),
        })

        for field in data.get("fields", []):

            self.env["inventory.viewer.field"].create({
                "inventory_id": inventory.id,
                "name": field.get("name"),
                "field_type": field.get("type")
            })

        for aggregate in data.get("aggregates", []):

            self.env["inventory.viewer.aggregate"].create({
                "inventory_id": inventory.id,
                "field_name": aggregate.get("field"),
                "value": str(aggregate)
            })

        return True