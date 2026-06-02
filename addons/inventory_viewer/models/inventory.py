from odoo import models, fields

class InventoryViewer(models.Model):
    _name = "inventory.viewer"

    name = fields.Char(required=True)
    category = fields.Char()
    items_count = fields.Integer()
    api_token = fields.Char()

    field_ids = fields.One2many(
        "inventory.viewer.field",
        "inventory_id"
    )

    aggregate_ids = fields.One2many(
        "inventory.viewer.aggregate",
        "inventory_id"
    )


class InventoryViewerField(models.Model):
    _name = "inventory.viewer.field"

    inventory_id = fields.Many2one(
        "inventory.viewer"
    )

    name = fields.Char()
    field_type = fields.Char()


class InventoryViewerAggregate(models.Model):
    _name = "inventory.viewer.aggregate"

    inventory_id = fields.Many2one(
        "inventory.viewer"
    )

    field_name = fields.Char()
    value = fields.Text()