# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class classinfo(Document):
	def before_save(self):
		self.namediv = f'{self.name1} {self.division or ""}'
