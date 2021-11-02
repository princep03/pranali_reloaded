# -*- coding: utf-8 -*-
# Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class OCVPointsConfiguration(Document):
	def validate(self):
		rules = ['gavel', 'charter', 'collar', 'saa', 'minutes', 'attendance', 'avenue_files',
			'banner', 'roster', 'website', 'bye_laws', 'bye_laws_minutes', 'finance', 'saa_files', 'additional_points']
		
		self.max_points = 0

		for rule in rules:
			self.max_points += self.get(rule)
