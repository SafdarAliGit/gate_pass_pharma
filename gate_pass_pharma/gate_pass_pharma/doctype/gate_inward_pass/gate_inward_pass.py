import frappe
from frappe.model.document import Document


class GateInwardPass(Document):
    def on_submit(self):
        # Check if 'po_no' exists
        supplier = frappe.get_doc("Supplier", self.party)
        if self.po_no and self.gate_inward_pass_items:
            for item in self.gate_inward_pass_items:
            
                # Create a new Purchase Receipt document
                pr = frappe.new_doc("Purchase Receipt")
                pr.supplier = self.party
                pr.supplier_address = supplier.supplier_primary_address
                pr.supplier_name = supplier.supplier_name
                pr.posting_date = frappe.utils.nowdate()
                pr.posting_time = frappe.utils.now()
                pr.ref_no = self.name
                pr.ref_doctype = "Gate Inward Pass"

                # Add items to the Purchase Receipt
                
                pr.append("items", {
                    "item_code": item.item_code,
                    "stock_uom": item.uom,
                    "qty": item.qty,
                    "rate": item.rate,
                    "amount": item.qty * item.rate,
                    "purchase_order": self.po_no
                })

                try:
                    # Save and submit the Purchase Receipt
                    pr.insert()
                    
                    # Update the Gate Inward Pass with the Purchase Receipt reference
                    self.db_set("ref_no", pr.name)
                    self.db_set("ref_doctype", "Purchase Receipt")

                except Exception as e:
                    # Handle any errors during the creation of the Purchase Receipt
                    frappe.throw(frappe._("Error creating Purchase Receipt: {0}".format(str(e))))

            # No Purchase Order reference; only submit the Gate Inward Pass
            # Further logic for only submitting the Gate Inward Pass (if any) can be added here
