# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import logging


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def action_all_as_done(self):

        if not self.move_lines and not self.move_line_ids:
            raise UserError(_('Please add some items to move.'))

        for move_line in self.move_line_ids:
            move_line.qty_done = move_line.product_uom_qty