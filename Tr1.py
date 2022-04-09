mis = ['tu', 'esk', 'col']
mis.append('ss')
mis.insert(2, 'kin')
mis.insert(0, 'C300')
mis.append('ss24')
mis.remove('ss24')
message1 ="Today we have a " + mis[0].title() + "."
message2 ="Today we have a " + mis[1].title() + "."
message3 ="Today we have a " + mis[3].title() + "."
message4 ="Today we have a " + mis[4].title() + "."
message5 ="Today we have a " + mis[5].title() + "."
#message6 ="Today we have a " + mis[6].title() + "."
popped_mis = mis.pop(1)

print("The visit of " + popped_mis + " have been canceled")
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(mis)

