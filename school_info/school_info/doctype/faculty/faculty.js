// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt


frappe.ui.form.on('Faculty', {
	// Faculty_name_link: function(frm) {
	// 	frappe.call({
	// 		method:"frappe.client.get",
	// 		args:{
	// 			doctype:"employee",
	// 			name:frm.doc.Faculty_name_link,
	// 		},
	// 		callback:(r=>{
	// 			if(r.message){
	// 				frm.set_value('Faculty_name',r.message.employee_name)
	// 			}
	// 		})
	// 	})
	// }
});
	// }

	// aculty_name_link: function(frm) {
	// 	frappe.call({
	// 		method:"frappe.client.get",
	// 		args:{
	// 			doctype:"employee",
	// 			name:frm.doc.Faculty_name_link,
	// 		},
	// 		callback:(r=>{
	// 			if(r.message){
	// 				frm.set_value('Faculty_name',r.message.employee_name)
	// 			}
	// 		})
	// 	})
	// }

	// aculty_name_link: function(frm) {
	// 	frappe.call({
	// 		method:"frappe.client.get",
	// 		args:{
	// 			doctype:"employee",
	// 			name:frm.doc.Faculty_name_link,
	// 		},
	// 		callback:(r=>{
	// 			if(r.message){
	// 				frm.set_value('Faculty_name',r.message.employee_name)
	// 			}
	// 		})
	// 	})
	// }



	// salary_is: function (frm) {
	// 	frappe.call({
	// 		salary_is:frm.salary_is,
	// 		method:'get_mapped_doc',
	// 		callback:function(r){
	// 			let salary_is = frm.salary_is
	// 			salary_is.salary_is = r.message
	// 			frm.refresh_field('salary_is')
	// 			}
			
	// 	})
					
	// }


				// let salary_is = get_mapped_doc("Faculty", salary_is, {
					// "salary_is": {
					// 	"doctype": "salary",
					// 	"field_map": {
					// 		"salary_package": "salary_is",
											
					// 	}
					
					// },
				// }
			
			
		  
		  

// "validation": {
					// 	"docstatus": ["=", 1]
					// }
// doc = get_mapped_doc("Faculty", salary_is, {
					// 	"salary package": {
					// 		"doctype": "salary",
					// 		"field_map": {
					// 			"salary_is": "salary_package",
					// 								// map your custom fields here
					// 		},
					// 		"validation": {
					// 			"docstatus": ["=", 1]
					// 		}
					// 	},
					// }
// validate:function(frm){
	// 	frm.set_value('salary_is', frm.doc.salary_is)
		// var d = locals[cdt][cdn];
        // frappe.db.get_value("salary", {"salary is": d.salary_package}, function(value) {
        //     d.salary_package = value.salary_is;
        // });