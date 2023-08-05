frappe.call({
    method: 'frappe.client.get_value',
    args: {
        doctype: 'User',
        fieldname: ['location','phone'],
        filters: { 'name': frappe.session.user }
    },
    callback: function(response) {
        if (response && response.message) {
            var location = response.message.location;
            var phone = response.message.phone;
            if(location == 'line_user'){
                if(!phone){
                    //window.location = "/app/user_update";

                }
            }
        }
    }
});