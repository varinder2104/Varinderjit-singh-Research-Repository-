"""
In this program, we will apply the conditions for the approval of the request that under what conditions it should be approved 
or still be pending.

Author: Varinderjit singh
"""


def requisition_approval(total_cost, requisition_id, staff_id):
    status = "Approved"if total_cost > 0 and total_cost < 500 else "Pending"

    ref_number = staff_id.upper() + str(requisition_id)[-3:]
    # here, we use slicing for concatination.
    return status, ref_number