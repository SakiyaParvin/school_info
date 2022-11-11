# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil import relativedelta

class studentreg(Document):
	def validate(self):
		self.get_age()
		self.before_save()
		self.create_student()

	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	@frappe.whitelist()
	def get_age(self):
		if(self.dob):
			today = datetime.now()
			dob = datetime.strptime(self.dob, '%Y-%m-%d')
			t = relativedelta.relativedelta(today, dob)
			return t.years

	

	def create_student(self):
		if self.fees_paid == 'Paid' and not self.student_id: 
			doc = frappe.get_doc({
				"doctype": "student",
				"s_name": self.full_name,
				"age": self.age,
				"sex": self.sex,
				"date_of_birth": self.dob,
				"class_name_div": self.class_name_and_division,
				"class_mentor": self.class_mentor,
				"fees": self.total_fees,
				"address": self.address,
				"phone_number": self.phone_number,
				})
			doc.insert(ignore_permissions=True, ignore_mandatory=True)
			self.student_id = doc.name