# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class OutsourceWork(models.Model):
    _inherit = "outsource_work"

    @api.onchange(
        "allowed_pricelist_ids",
        "currency_id",
        "work_object_id",
        "model_id",
    )
    def onchange_pricelist_id(self):
        super().onchange_pricelist_id()
        if self.model_name == "project_outsource_work_acceptance" and self.work_object_id:
            pwa_id = self.env["project_outsource_work_acceptance"].browse(self.work_object_id)
            self.pricelist_id = pwa_id.pricelist_id.id
