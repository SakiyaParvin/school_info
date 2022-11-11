// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('studentreg', {
	dob: function (frm) {
		frappe.call({
		  doc:frm.doc,
		  method:'get_age', 
		  callback:function(r){
			let doc = frm.doc
			doc.age = r.message
			frm.refresh_field('age')
		  }
		})
			
	},

	class_of_join_link: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"class info",
				name:frm.doc.class_of_join_link,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('class_name_and_division',r.message.namediv)
					frm.set_value('class_mentor',r.message.class_mentor)
				}
			})
		})
	},

	class_range_link: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"fee structure",
				name:frm.doc.class_range_link,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('total_fees',r.message.total)
				}
			})
		})
	},
	
	
});
