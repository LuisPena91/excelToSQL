def menu():
    print('----Tables----')
    print('1. Users.\n2. Tasks.\n3. CheckInCheckOut.\n4. Projects.\n5. Boxes.\n6. Productivity.\n0. EXIT')
    pos = int(input('Select a table to update:'))
    return pos-1