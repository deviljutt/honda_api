import requests
import frappe
import base64
from bs4 import BeautifulSoup
import json
from datetime import timedelta, date
from datetime import datetime


@frappe.whitelist(allow_guest=True)
def feachorders():  

        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y-%m-%d")
        uri = 'http://171.103.6.198:8484/LoyaltyHondanont.aspx?rEbUM02=dW5pY29ybg==&rEbUM03=SEBuZGExMjM=&rEbUM01=' + formatted_date
        response = requests.get(uri)  # Send a GET request and get the response
        site_response = str(response.content)
        soup = BeautifulSoup(site_response, 'html.parser')
        specific_element = soup.find('span', id='txtJson')
        if specific_element:
            specific_content = specific_element.get_text();
            decoded_bytes = base64.b64decode(specific_content)
            decoded_string = decoded_bytes.decode('utf-8')
            data  = json.loads(decoded_string)

            end_date = date.today() + timedelta(days=10)


            for item in data:
                invoiceno = item["INVOICE_NO"].replace(" ", "")
                prev_order = frappe.db.exists({"doctype": "Sales Invoice", "invoice_no": invoiceno})
                if not prev_order:
                        if( item["TOTAL_AMT"] == '' ):
                                continue


                        new_order = frappe.new_doc('Sales Invoice')
                        new_order.invoice_no=invoiceno
                        new_order.branchcode=item["BranchCode"]
                        new_order.frame_no=item["FRAME_NO"]
                        new_order.engine_no=item["ENGINE_NO"]
                        new_order.license_no=item["LICENSE_NO"]
                        new_order.customerid=item["CUSTOMERID"]
                        new_order.invoice_date=item["INVOICE_DATE"]
                        new_order.invoice_type=item["INVOICE_TYPE"]
                        new_order.mobile_no=item["MOBILE_NO"]
                        item_code = str(item["INVOICE_TYPE"])
                        price = abs(item["TOTAL_AMT"])

                        new_order.base_grand_total=price
                        new_order.grand_total=price
                        new_order.total=price
                        new_order.net_total=price

                        Itemz = frappe.db.exists("Item", item_code)
                        if( Itemz == None ):
                                _create_product(item_code,item_code)
                                Itemz = frappe.db.exists("Item", item_code)

                        if( item["MOBILE_NO"] == None ):
                                continue

                        if( Itemz == None):
                                continue


                        customer_flag = frappe.db.exists({"doctype": "Customer", "phone": item["MOBILE_NO"]})
                        if( customer_flag == None ):
                               _create_customer(item["MOBILE_NO"])    
                               customer_flag = frappe.db.exists({"doctype": "Customer", "phone": item["MOBILE_NO"]})


                        new_order.customer=customer_flag

                        new_order.append("items",{
                                "item_code": item_code,
                                "item_name": item_code,
                                "qty": 1,
                                "rate": price,
                                "amount":  price,
                                "net_rate": price,
                                "net_amount": price,
                                "billed_amt": price,
                                "valuation_rate": price
                        })

                        new_order.due_date=end_date
                        new_order.order_type="Sales"
                        new_order.flags.ignore_mandatory = True
                        new_order.insert(
				ignore_permissions=True, 
				ignore_links=True, 
				ignore_if_duplicate=True, 
				ignore_mandatory=True 
			)
                        new_order.submit()
                        

def _create_product(item_name,item_code):
        Item = frappe.new_doc('Item')
        Item.item_name=item_name
        Item.item_code=item_code
        Item.item_group='All Item Groups'
        Item.insert(
                        ignore_permissions=True, # ignore write permissions during insert
                        ignore_links=True, # ignore Link validation in the document
                        ignore_mandatory=True # insert even if mandatory fields are not set
                )
        return

def _create_customer(customer_name):
        new_customer = frappe.new_doc('Customer')
        new_customer.customer_name=customer_name
        new_customer.territory="Thailand"
        new_customer.phone=customer_name
        new_customer.insert(
                ignore_permissions=True, # ignore write permissions during insert
                ignore_links=True, # ignore Link validation in the document
                ignore_mandatory=True # insert even if mandatory fields are not set
        )
        return
