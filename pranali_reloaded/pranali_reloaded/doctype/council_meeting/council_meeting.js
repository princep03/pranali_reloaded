// Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

frappe.ui.form.on('Council Meeting', {
	// refresh: function(frm) {

	// }
});

cur_frm.cscript.guest = function(doc) {
	doc.total_attendance = cint(doc.district_council_members) + cint(doc.club_rotaractors) + cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest)
	refresh_field('total_attendance');
};

cur_frm.cscript.dcm = cur_frm.cscript.alumini = cur_frm.cscript.club_rotaractors =
	cur_frm.cscript.rotarians = cur_frm.cscript.pis = cur_frm.cscript.guest;