// Copyright (c) 2022, demo and contributors
// For license information, please see license.txt

frappe.ui.form.on('fee structure', {
	before_save:function(frm) {
		frm.set_value('total',frm.doc.admission_fee + frm.doc.special_fee + frm.doc.tution_fee + frm.doc.coution_deposit)

	}
});
