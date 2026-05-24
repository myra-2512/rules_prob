set_1={'A','B','C','D','E'}
set_2={'B','D','V','X','Y','Z'}

union=set_1.intersection(set_2)

total_guests=list(union)

print('Total guests invited to the party are:',len(total_guests))
print('Guest list :',total_guests)