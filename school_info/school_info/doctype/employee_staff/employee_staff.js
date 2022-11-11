// Copyright (c) 2022, demo and contributors
// For licetotal_salarynse information, please see license.txt

frappe.ui.form.on('Employee Staff', {
	before_save:function(frm) {
		frm.set_value('total_salary',frm.doc.salary + frm.doc.increment)

	 }
});
