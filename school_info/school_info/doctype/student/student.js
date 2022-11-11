// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('student', {
	refresh: function(frm) {
		frm.add_custom_button('Create Library Membership', () => {
            frappe.new_doc('Library Membership', {
                student: frm.doc.name
            })
        })
        frm.add_custom_button('Create Club Membership', () => {
            frappe.new_doc('Club Membership', {
                student: frm.doc.name
            })
        })
	}
});
