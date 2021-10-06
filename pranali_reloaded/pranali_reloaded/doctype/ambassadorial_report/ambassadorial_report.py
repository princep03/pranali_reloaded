# -*- coding: utf-8 -*-
# Copyright (c) 2015, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from warnings import filters
import frappe
from frappe.utils import cint, cstr, now, getdate, add_months, add_days
from frappe.model.document import Document

class AmbassadorialReport(Document):
	def validate(self):
		self.set_zone()
		self.document_status='draft'
		self.check_duplicates()
		self.count_total()
		if self.project_of=="Others" and not self.name_of_the_club:
			frappe.throw("Please enter name of the Club")
		self.set_status()
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")

	def on_submit(self):
		self.time_stamp = now()
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Ambassadorial Report', self.name, 'document_status', 'cancelled')

	# def set_status(self):
	# 	self.reporting_month = frappe.get_value("Project", self.project_name, "reporting_month")
		
	# 	if self.reporting_month in ["July", "August", "September"]:
	# 		self.quarter = "One"
	# 	elif self.reporting_month in ["October", "November", "December"]:
	# 		self.quarter = "Two"
	# 	elif self.reporting_month in ["January", "February", "March"]:
	# 		self.quarter = "Three"
	# 	elif self.reporting_month in ["April", "May", "June"]:
	# 		self.quarter = "Four"

	
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def check_duplicates(self):
		members= []
		for d in self.members:
			if not d.member_id in members:
				members.append(d.member_id)
			else:
				frappe.throw("Attendance for {0} appears multiple times.".format(d.member_name))

	def count_total(self):
		self.total_attendance = 0
		for d in self.members:
			self.total_attendance +=1