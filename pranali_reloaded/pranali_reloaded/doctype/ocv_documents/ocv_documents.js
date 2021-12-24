cur_frm.add_fetch("member_id", "member_name", "member_name")

frappe.ui.form.on("ocv_documents", {
    refresh:function(frm) {
            $('.form-attachments').hide(); 
        }
    });