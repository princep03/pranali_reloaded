# Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, getdate, today, to_timedelta
from frappe.model.document import Document

class CouncilMeeting(Document):
	def validate(self):
		self.validate_date()
		self.calculate_totals()
		self.document_status='draft'
		self.reporting_month = getdate(self.date).strftime("%B")
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")
		self.set_attendance_percentage()

	def on_submit(self):
		frappe.db.set_value('Meeting', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('Meeting', self.name, 'document_status', 'cancelled')

	def calculate_totals(self):
		self.total_attendance = cint(self.district_council_members) + cint(self.rotarians) + cint(self.alumini) + cint(self.pis) + cint(self.guest)

	def validate_date(self):
		if self.date > today():
			frappe.throw("Did you fix the Flux Capacitor ? \n Meeting Date is Greater than today.")

		if to_timedelta(self.start_time) > to_timedelta(self.end_time):
			frappe.throw("Start Time cannot be greater than End Time.")
