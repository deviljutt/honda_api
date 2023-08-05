frappe.pages['user_update'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'User Update',
		single_column: true
	});
}