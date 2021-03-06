# -*- coding: utf-8 -*-
# Copyright (c) 2020, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OCV(Document):
	def validate(self):
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.validate_club()
		self.set_points()

	def validate_club(self):
		rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.existing_ocv = frappe.get_all("OCV", filters={"club": self.club, 'docstatus':1, 'rotaract_year': rotaract_year})
		if self.existing_ocv:
			frappe.throw("OCV Record is already created for Club {0}. <a href='/desk#Form/OCV/{1}'>Please cancel {1} to proceed.</a>".format(self.club, self.existing_ocv[0].get('name')))

	def set_points(self):
		rules = ['gavel', 'charter', 'collar', 'saa', 'minutes', 'attendance', 'avenue_files', 'saa_files',
			'banner', 'roster', 'membership', 'website', 'bye_laws', 'bye_laws_minutes', 'finance', 'additional_points']
		
		rule_points = frappe.get_single("OCV Points Configuration")
		self.max_points = rule_points.max_points
		self.points = 0

		if self.ocv_date < rule_points.cut_off_date:
			self.points += rule_points.additional_points
		
		for rule in rules:
			if self.get(rule):
				self.points += rule_points.get(rule)

		self.percentage_points_earned = (self.points/self.max_points) * 100