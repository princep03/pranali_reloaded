# Copyright (c) 2021, Rtr. Prince Pandey and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, now, getdate, add_months, add_days
import datetime
from frappe.model.document import Document
from frappe.utils.data import today

class OCVDocuments(Document):
	def validate(self):
		self.set_zone()
		self.set_status()
		self.document_status='draft'
		self.rotaract_year = frappe.db.get_single_value("Pranali Settings", "current_rotaract_year")

	def on_submit(self):
		self.validate_account()
		self.validate_reporting_access()
		frappe.db.set_value('OCV Documents', self.name, 'document_status', 'submitted')

	def on_cancel(self):
		frappe.db.set_value('OCV Documents', self.name, 'document_status', 'cancelled')

	def set_status(self):
		self.time_stamp = datetime.datetime.today()
		self.today = datetime.date.today()
		self.date = datetime.datetime.strptime(self.ocv_date,'%Y-%m-%d').date()
		if (self.date - self.today).days >= 15:
			self.submission_status = "On Time"	
		else:
			self.submission_status = "Late"
	
	def set_zone(self):
		self.zone = frappe.db.get_value("Club", self.club, "zone")

	def validate_account(self):
		balance_amount = frappe.db.get_value("Club", self.club, "balance_amount")
		if balance_amount < 0:
			frappe.throw("Your account has been locked due to Negative funds in your wallet. Please pay INR {0} to Unlock !".format(abs(balance_amount)))

	def validate_reporting_access(self):
		if frappe.db.get_value("Club", self.club, "disable_reporting_access"):
			frappe.throw("Reporting Access has been disabled for your club. Please contact the District Secretary.")



