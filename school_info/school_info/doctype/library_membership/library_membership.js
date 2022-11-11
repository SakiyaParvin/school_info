// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	refresh: function(frm) {
		frm.add_custom_button('Make Transaction', () => {
            frappe.new_doc('Library Transaction', {
                student: frm.doc.name
            })
        })
	},
    student_link: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"student",
				name:frm.doc.student_link,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('student_name',r.message.s_name)
				}
			})
		})
	}
});
