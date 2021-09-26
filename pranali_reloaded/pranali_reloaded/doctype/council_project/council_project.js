// Copyright (c) 2021, Rtr.Neil Trini Lasrado and contributors
// For license information, please see license.txt

cur_frm.cscript.sponsorship = function(doc) {
	doc.total_income = cint(doc.incomes) + cint(doc.sponsorship) - cint(doc.expenditure) 
	refresh_field('total_income');
};

cur_frm.cscript.incomes = cur_frm.cscript.expenditure = cur_frm.cscript.sponsorship


cur_frm.cscript.pis = function(doc) {
doc.total = cint(doc.dcm) + cint(doc.rotarians) + cint(doc.guest) 
		+ cint(doc.alumini) + cint(doc.other_club) + cint(doc.pis)
refresh_field('total');
};

cur_frm.cscript.dcm = cur_frm.cscript.rotarians = cur_frm.cscript.guest = cur_frm.cscript.alumini =
cur_frm.cscript.other_club = cur_frm.cscript.pis;


