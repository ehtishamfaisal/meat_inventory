# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import models, fields, api

class meat_inventory(models.Model):
	_name = 'meat_inventory'

	name = fields.Char(string="Order No")
	branch_user = fields.Many2one('res.users', string="Branch")
	stages = fields.Selection([
		('requested', 'Order'),
		('process', 'Processing'),
		('delivered', 'Ordered'),
		('recieved', 'Recieved'),
		],string = "Stages", default = 'requested')
	order_date = fields.Datetime(default=datetime.now())
	order_line_ids = fields.One2many('meat_inventory_tree', 'order_id', string="Order Line")

	_defaults = {
	'order_date' : datetime.now(),
	}

	@api.model
	def create(self, vals):
		new_record = super(meat_inventory, self).create(vals)
		if new_record.branch_user.name == 'Maandag':
			new_record.name = self.env['ir.sequence'].next_by_code('maandog.seq')
		elif new_record.branch_user.name == 'Dinsdag':
			new_record.name = self.env['ir.sequence'].next_by_code('dinsdag.seq')
		elif new_record.branch_user.name == 'Woensdag':
			new_record.name = self.env['ir.sequence'].next_by_code('woensdag.seq')
		elif new_record.branch_user.name == 'Donderdag':
			new_record.name = self.env['ir.sequence'].next_by_code('donderdag.seq')
		elif new_record.branch_user.name == 'Vrijdag':
			new_record.name = self.env['ir.sequence'].next_by_code('vrijdag.seq')
		elif new_record.branch_user.name == 'Zaterdag':
			new_record.name = self.env['ir.sequence'].next_by_code('zaterdag.seq')
		else:
			new_record.name = self.env['ir.sequence'].next_by_code('zondag.seq')
		return new_record

	@api.multi
	def btn_update(self):
		if self.stages=='requested':
			Products = self.env['meat_inventory_tree_config'].search([])
			for line in Products:
				self.order_line_ids.create({
					'product': line.product.id,
					'uom': line.uom,
					'order_id' : self.id
					})


	@api.multi
	def btn_requested(self):
		self.write({'stages':'requested'})

	@api.multi
	def btn_process(self):
		self.write({'stages':'process'})

	@api.multi
	def btn_delivered(self):
		self.write({'stages':'delivered'})

	@api.multi
	def btn_recieved(self):
		self.write({'stages':'recieved'})

	@api.multi
	def btn_draft(self):
		self.write({'stages':'draft'})

	@api.multi
	def btn_cancel(self):
		self.write({'stages':'cancel'})





class meat_inventory_tree(models.Model):
	_name = 'meat_inventory_tree'

	product = fields.Many2one('product.template',string="Product")
	uom = fields.Selection([
		('box', 'BOX'),
		('kg', 'KG'),
		('bottle', 'BOTTLE'),
		('bag', 'BAG'),
		],string = "UOM")
	remaining_qty = fields.Float(string="Remaining Qty")
	request_qty = fields.Float(string="Alloted Qty")
	capacity = fields.Float(string="Capacity")

	order_id = fields.Many2one('meat_inventory',string="Order ID")


class meat_inventory_tree_config(models.Model):
	_name = 'meat_inventory_tree_config'

	product = fields.Many2one('product.template',string="Product")
	uom = fields.Selection([
		('box', 'BOX'),
		('kg', 'KG'),
		('bottle', 'BOTTLE'),
		('bag', 'BAG'),
		],string = "UOM")

