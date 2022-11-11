// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	library_member_link: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Library Membership",
				name:frm.doc.library_member_link,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('member_name',r.message.student_name)
				}
			})
		})
	}
});
