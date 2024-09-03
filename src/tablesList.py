excel = ['Users','CheckInCheckOut','Task','Projects','Boxes','Productivity']
sql = {
    'users':'caNumber',
    'checkinout':'idCheckInOut',
    'task':'idtasks',
    'projects':'idprojects',
    'boxes':'idboxes',
    'productivity':'idproductivity'
}

listSql = list(sql.items())
pos=0

for pos in range(len(excel)):
    table, pk = listSql[pos]
    print(excel[pos]," = ",table," | ",pk)


