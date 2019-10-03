# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class Picking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def action_all_as_done(self):

        _logger.info("*" * 80)
        _logger.info("action_all_as_done")

        if not self.move_lines and not self.move_line_ids:
            raise UserError(_('Please add some items to move.'))

        for move_line in self.move_line_ids:
            _logger.info("*"*80)
            _logger.info(move_line.product_uom_qty)
            move_line.qty_done = move_line.product_uom_qty