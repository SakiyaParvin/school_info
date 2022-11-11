# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def validate(self):
		self.before_submit()


	def before_submit(self):
		exists = frappe.db.exists(
            "Library Membership",
            {
				"student_name": self.student_name,
				"to_date": (">", self.from_date),
			})
		if exists:
			frappe.throw("There is an active membership for this member")
