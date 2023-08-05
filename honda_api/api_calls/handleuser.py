import frappe
from frappe import _
import json


def handleusersave(doc, event):
    phone = doc.phone
    if phone:
        customer = frappe.get_doc("Customer", phone)
        
        if customer:
                contacts = frappe.get_all("Contact", filters={"email_id": ["like", doc.email]})[0]['name']
                if contacts:
                    contacts = frappe.get_doc("Contact", contacts)
                    contacts.append("links",{
                            "link_doctype": "Customer",
                            "link_name": customer.name,
                            "link_title": customer.name,
                    })
                    contacts.append("links",{
                            "link_doctype": "Customer",
                            "link_name": customer.name,
                            "link_title": customer.name,
                    })
                    contacts.append("links",{
                            "link_doctype": "Customer",
                            "link_name": customer.name,
                            "link_title": customer.name,
                    })
                    contacts.save()
                    converted_string = str(contacts)
                    frappe.throw(converted_string)