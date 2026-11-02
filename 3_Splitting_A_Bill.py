total_bill = 4750
number_of_friends = 4

share_per_friend = total_bill / number_of_friends
whole_rupees_per_friend = total_bill // number_of_friends
remaining_rupees = total_bill % number_of_friends

print("Share per friend", share_per_friend)
print(f"Whole rupees per friend: Rs. {whole_rupees_per_friend}")
print(f"Rupees left over: Rs. {remaining_rupees}")