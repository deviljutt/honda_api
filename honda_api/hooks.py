import frappe
from . import __version__ as app_version
from frappe.utils import now


app_name = "honda_api"
app_title = "Honda Api"
app_publisher = "daviljutt"
app_description = "Honda API"
app_email = "itsgoraya@gmail.com"
app_license = "MIT"



doc_events = {
    "User": {
        "on_update": "honda_api.api_calls.handleuser.handleusersave"
    }
}


    
# include js, css files in header of desk.html
# app_include_css = "/assets/honda_api/css/honda_api.css"
# app_include_js = "/assets/honda_api/js/honda_api.js"

# include js, css files in header of web template
# web_include_css = "/assets/honda_api/css/honda_api.css"
# web_include_js = "/assets/honda_api/js/honda_api.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "honda_api/public/scss/website"

# include js, css files in header of web form

# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
#page_js = {"page" : "/honda_api/honda_api/public/js/custom.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "honda_api.utils.jinja_methods",
#	"filters": "honda_api.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "honda_api.install.before_install"
# after_install = "honda_api.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "honda_api.uninstall.before_uninstall"
# after_uninstall = "honda_api.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "honda_api.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"honda_api.tasks.all"
#	],
#	"daily": [
#		"honda_api.tasks.daily"
#	],
#	"hourly": [
#		"honda_api.tasks.hourly"
#	],
#	"weekly": [
#		"honda_api.tasks.weekly"
#	],
#	"monthly": [
#		"honda_api.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "honda_api.install.before_tests"

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
	"frappe.www.login.login_via_line": "honda_api.api_calls.linehandle.login_via_line",
}




#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "honda_api.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "honda_api.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["honda_api.utils.before_request"]
# after_request = ["honda_api.utils.after_request"]

# Job Events
# ----------
# before_job = ["honda_api.utils.before_job"]
# after_job = ["honda_api.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"honda_api.auth.validate"
# ]

fixtures = ["Custom Field"]

