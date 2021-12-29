frappe.listview_settings['OCV Documents'] = {
    add_fields: ["submission_status"],

    get_indicator: function(doc) {
        if (doc.submission_status == "Late") {
            return [__("Late"), "orange", "submission_status,=,Late"];
        } else if (doc.submission_status == "On Time") {
            return [__("On Time"), "green", "submission_status,=,On Time"];
        } 
    }
};