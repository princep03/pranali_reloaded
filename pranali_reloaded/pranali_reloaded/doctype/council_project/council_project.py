# Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, now, getdate, add_months, add_days
from frappe.model.document import Document

class CouncilProject(Document):
	def validate(self):
		self.validate_date()
		self.set_status()
		self.calculate_totals()
		self.calculate_total_income()
		self.document_status='draft'
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")

	def on_submit(self):
		frappe.db.set_value('Council Project', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Council Project', self.name, 'document_status', 'cancelled')

	def set_status(self):
		self.time_stamp = now()
		self.reporting_month = getdate(self.end_time).strftime("%B")
		d = add_months(getdate(self.end_time), 1)
		early = frappe.db.get_single_value("Pranali Settings", "early_reporting_days")
		reporting_deadline = frappe.db.get_single_value("Pranali Settings", "reporting_deadline") + 5
		deadline = cstr(getdate(d).strftime("%Y")) + "-" + cstr(getdate(d).strftime("%m")) + "-" + cstr(reporting_deadline)
		if getdate(self.time_stamp) > getdate(deadline):
			self.project_status = "Late"
		elif early > 0 and getdate(self.time_stamp) <= getdate(add_days(getdate(self.end_time), early)):
			self.project_status = "Early"
		else:
			self.project_status = "On Time"

		if self.reporting_month in ["July", "August", "September"]:
			self.quarter = "One"
		elif self.reporting_month in ["October", "November", "December"]:
			self.quarter = "Two"
		elif self.reporting_month in ["January", "February", "March"]:
			self.quarter = "Three"
		elif self.reporting_month in ["April", "May", "June"]:
			self.quarter = "Four"

	def calculate_totals(self):
		self.total = cint(self.dcm) + cint(self.rotarians) + cint(self.guest) + cint(self.alumini) + cint(self.other_club) + cint(self.pis)

	def calculate_total_income(self):
                self.total_income = cint(self.incomes) - cint(self.expenditure) + cint(self.sponsorship)

	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_date(self):
		if self.end_time > now():
			frappe.throw("Did you fix the Flux Capacitor ? \n Project End Time is Greater than today.")

		if self.start_time > self.end_time:
			frappe.throw("Start Time cannot be greater than End Time.")

