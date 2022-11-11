# Copyright (c) 2022, demo and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Faculty(Document):
    pass

    # def validate(self):
    #     self.create_Faculty()
    # def create_Faculty(self):
    #    # for i in self.get("initial_intake_form"):
    # #    if self.status == 'Enrollment Completion' and not self.student_id:
    #        doc = frappe.get_doc({
    #            "doctype": "employee",
    #            "Faculty_name": self.employee_name,
    #            "last_name": self.last_name,
    #            "date_of_birth": self.dob,
    #            "gender": self.gender,
    #            })
    #        doc.insert(ignore_permissions=True, ignore_mandatory=True)
    #        self.student_id = doc.name
 

  
    # def validate(self):
    #     self.create_Faculty()

    # def create_Faculty(self):
    #     for i in self.get("employee"):
    #         doc = frappe.get_doc({
    #             "doctype":"Faculty",
    #             "employee_name":i.Faculty_name, 
    #             "employment_type":i.type, 
    #             # "salary_is":i.salary_package
    #         })
    #         doc.insert(ignore_permissions=True)
    #         i.Faculty_id
            

            
    # def validate(self):
        # self.get_document()
        # self.get_mapped_doc()
    

    # def get_document(self):
    #     doc = frappe.get_doc('salary', self.employee_status)
    #     frappe.msgprint(("salary is {0}").format(doc.salary_package))
    #     doc.insert()
        
    # def get_mapped_doc(source_name, target_doc= None):
    #     def set_value(source, target):
    #         target.salary_package = frappe.db.set_value('salary', 'employee_status', ['salary_package'])
        
    #     doc = get_mapped_doc("Faculty", source_name, {
	# 		"Faculty": {
	# 			"doctype": "salary",
	# 			"field_map": {
    #                 "salary_is": "salary_package",
    #             }
	# 		}
	# 	}, target_doc, set_value)
    #     # target_doc.insert()
    #     return doc

        # doc = frappe.get_doc('salary', self.employee_status)
        # frappe.msgprint(("salary is {0}").format(doc.salary_package))
        # doc.insert()
        
    #     source_doc = frappe.get_doc("salary",salary_package)
    #     if source_doc.get("salary_package"):
    #         tabsalary = {
	# 			"doctype": "Faculty",
	# 			"postprocess": salary_is
	# 		}
    #     return target_doc
			# map_child_doc(source_doc, target_doc, table_map, source_doc)

		

        # doc = get_mapped_doc(“Task”, source_name, {“Task”: {“doctype”: “”,},)



    # def get_mapped_doc(self):
    #     salary_is = get_mapped_doc("", self.salary_is)
    #     # "salary_is": {
    #     #     "doctype": "salary",
    #     #     "field_map": {
    #     #         "salary_package": "salary_is",
	# 	# 	}
					
	# 	# }
    #     frappe.msgprint(("salary fetched is {0}").format(salary_is.salary_package))
		
        # frappe.msgprint(("salary fetched is {0}").format(salary_is.salary_package))
       # salary_is = get_mapped_doc("Faculty", salary_is, {
        #     "salary package": {
        #         "doctype": "salary",
        #         "field_map": {
        #             "salary_is": "salary_package",
                                        
        #         },
        #         "validation": {
        #             "docstatus": ["=", 1]
        #         }
        #     },
        # }
        

    # def before_save(self):
    #     self.salary_is = {self.salary_package or ""} 
    
    
        # self.set_value()

    # @frappe.whitelist()
    # def get_value(self):
    #     salary_package = frappe.db.get_value('salary', 'employee_status', ['salary_package'])

    # frappe.db.set_value('Task', 'TASK00002', 'subject', 'New Subject')

    # def set_value(self):
    #     salary_is = frappe.db.set_value('Faculty', 'salary_is')
    #     frappe.msgprint(("salary is {0}").format(salary_is.salary_package))        

    # def get_document(self):
    #     doc = frappe.get_doc('salary', 'salary_package')
    #     # doc.title = 'salary_package'
    #     doc.save()

