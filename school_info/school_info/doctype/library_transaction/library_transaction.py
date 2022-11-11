# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
	def validate(self):
		self.before_submit()
		self.msg()


	def before_submit(self):
		exists = frappe.db.exists(
            "Library Transaction",
            {
                "student_name": self.member_name,
			})

	def msg(self):
		if self.type == 'Issue':
			frappe.msgprint("book issued")	
