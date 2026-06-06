my_str = "Η Οδηγίαγιαμισθολογική διαφάνειαστηνΕΕορίζειότιοιεργοδότεςθαπρέπεινααναφέρουν τονμισθόστιςαγγελίες,ενώθα απαγορεύεται να ρωτούν τους υποψηφίους για το ιστορικό των αμοιβών τους"
print (my_str)
my_list = list(my_str)
print (my_list)
my_dict = {}

for i in my_list:
    my_dict[i] = my_list.count(i)
print (my_dict)

max_value = 0
max_key = []

for key, value in my_dict.items():
    if value > max_value:
       max_value = value
       max_key = [key]
    elif value == max_value:
        max_key.append(key)
print ("Ο χαρακτήρας με το μέγιστο πλήθος εμφανίσεων είναι: " + str(max_key) + " και βρέθηκε " + str(max_value) + " φορές.")
