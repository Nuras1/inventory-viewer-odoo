from odoo import models, fields


class InventoryViewer(models.Model):
    _name = "inventory.viewer"
    _description = "Imported Inventory"

    name = fields.Char(required=True)

    category = fields.Char()

    items_count = fields.Integer()