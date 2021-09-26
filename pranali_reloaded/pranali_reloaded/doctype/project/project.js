cur_frm.cscript.sponsorship = function(doc) {
        doc.total_income = cint(doc.incomes) + cint(doc.sponsorship) - cint(doc.expenditure) 
        refresh_field('total_income');
};

cur_frm.cscript.incomes = cur_frm.cscript.expenditure = cur_frm.cscript.sponsorship


cur_frm.cscript.guest = function(doc) {
	doc.total = cint(doc.home_club) + cint(doc.other_club) + cint(doc.dcm) 
			+ cint(doc.alumini) + cint(doc.rotarians) + cint(doc.pis) + cint(doc.guest)
	refresh_field('total');
};

cur_frm.cscript.home_club = cur_frm.cscript.other_club = cur_frm.cscript.dcm = cur_frm.cscript.alumini =
	cur_frm.cscript.rotarians = cur_frm.cscript.pis = cur_frm.cscript.guest;

cur_frm.add_fetch("member_id", "member_name", "member_name")
