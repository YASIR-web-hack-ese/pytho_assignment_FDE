total_items = 23
box_capacity = 6
shipping_cost_per_box = 120

full_boxes = total_items // box_capacity
leftover_items = total_items % box_capacity
total_boxes_needed = (total_items + box_capacity - 1) // box_capacity
shipping_cost = total_boxes_needed * shipping_cost_per_box

print(f"Full boxes: {full_boxes}")
print(f"Leftover items: {leftover_items}")
print(f"Total boxes needed: {total_boxes_needed}")
print(f"Shipping cost: Rs. {shipping_cost}")