# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeeStaff(Document):
	def validate(self):
		self.create_teacher()
		self.create_nonteach()

	def create_teacher(self):
		if self.status == 'Teaching' and not self.employee_id: 
			doc = frappe.get_doc({
				"doctype": "Faculty",
				"faculty_name": self.employee_name,
				"subject": self.subject,
				"employment_type": self.status,
				"date_of_birth": self.date_of_birth,
				"salary": self.total_salary,
				})
			doc.insert(ignore_permissions=True, ignore_mandatory=True)
			self.employee_id = doc.name

	def create_nonteach(self):
		if self.status == 'Non Teaching' and not self.employee_id: 
			doc = frappe.get_doc({
				"doctype": "Non Teaching Staff",
				"staff_name": self.employee_name,
				"employment_type": self.status,
				"work": self.work,
				"date_of_birth": self.date_of_birth,
				"salary": self.total_salary,
				})
			doc.insert(ignore_permissions=True, ignore_mandatory=True)
			self.employee_id = doc.name

