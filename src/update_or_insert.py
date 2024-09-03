def users(cursor, df_excel):
    for index, row in df_excel.iterrows():
        #If exist select the row and give a result
        cursor.execute("SELECT * FROM users WHERE caNumber = %s",
        (row['caNumber'],))
        result = cursor.fetchone()
        
        if result:
            #if existe update the actual row
            cursor.execute(
                "UPDATE users SET name = %s,status = %s,profile = %s WHERE caNumber = %s",
                (row['UserId'],row['Status'],row['Profile'],row['caNumber'])
            )
            print(f"Updated row: {row['caNumber']} - {row['UserId']}")
        else:
            #if no insert new row
            cursor.execute(
                "INSERT INTO users (caNumber,name,status,profile) VALUES (%s,%s,%s,%s)",
                (row['caNumber'],row['UserId'],row['Status'],row['Profile'])
            )
            print(f"New row: {row['caNumber']} - {row['UserId']}")

def tasks(cursor, df_excel):
    for index, row in df_excel.iterrows():
        cursor.execute("SELECT * FROM tasks WHERE idtasks = %s",
        (row['idT'],))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE tasks SET tasksName = %s WHERE idtasks = %s",
                (row['Task'],row['idT'])
            )
            print(f"Updated row: {row['idT']} - {row['Task']}")
        else:
            cursor.execute(
                "INSERT INTO tasks (idtasks,tasksName) VALUES (%s,%s)",
                (row['idT'],row['Task'])
            )
            print(f"New row: {row['idT']} - {row['Task']}")

def checkinout(cursor, df_excel):
    for index, row in df_excel.iterrows():
        cursor.execute("SELECT * FROM checkinout WHERE idCheckInOut = %s",
        (row['CID'],))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE checkinout SET dateIn=%s, timeIn=%s, timeOut=%s,status=%s,caNumber=%s,totalTime=%s WHERE idCheckInOut = %s",
                (row['CheckIn'],row['CheckInTime'],row['CheckOutTime'],row['InOut'],row['caNumber'],row['Time'],row['CID'])
            )
            print(f"Updated row: {row['CID']}")
        else:
            cursor.execute(
                "INSERT INTO checkinout (idCheckInOut,dateIn,timeIn,timeOut,status,caNumber,totalTime) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (row['CID'],row['CheckIn'],row['CheckInTime'],row['CheckOutTime'],row['InOut'],row['caNumber'],row['Time'])
            )
            print(f"New row: {row['CID']}")

def projects(cursor, df_excel):
    for index, row in df_excel.iterrows():
        cursor.execute("SELECT * FROM projects WHERE idprojects = %s",
        (row['idP'],))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE projects SET projects=%s WHERE idprojects = %s",
                (row['PROJECT'], row['idP'])
            )
            print(f"Updated row: {row['idP']} - {row['PROJECT']}")
        else:
            cursor.execute(
                "INSERT INTO projects (idprojects,projects) VALUES (%s,%s)",
                (row['idP'],row['PROJECT'])
            )
            print(f"New row: {row['idP']} - {row['PROJECT']}")

def boxes(cursor, df_excel):
    for index, row in df_excel.iterrows():
        cursor.execute("SELECT * FROM boxes WHERE idboxes = %s",
        (row['Boxes_Id'],))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "UPDATE boxes SET boxName=%s, idprojects=%s WHERE idboxes = %s",
                (row['Box'], row['idP'],row['Boxes_Id'])
            )
            print(f"Updated row: {row['Boxes_Id']}")
        else:
            cursor.execute(
                "INSERT INTO boxes (idboxes,boxName,idprojects) VALUES (%s,%s,%s)",
                (row['Boxes_Id'],row['Box'], row['idP'])
            )
            print(f"New row: {row['Boxes_Id']}")

def productivity(cursor, df_excel):
    for index, row in df_excel.iterrows():
        cursor.execute("SELECT * FROM productivity WHERE idproductivity = %s",
        (row['OT'],))
        result = cursor.fetchone()
        if result:
            cursor.execute(
                "UPDATE productivity SET dateStart=%s, startTime=%s, endTime=%s, idtasks=%s, idprojects=%s, documents=%s, images=%s, status=%s, caNumber=%s, idboxes=%s, totalTime=%s, WHERE idproductivity = %s",
                (row['Date'], row['StartTime'], row['EndTime'], row['idT'], row['idP'], row['Folders'], row['Images'], row['Status'], row['caNumber'], row['Boxes_Id'], row['Time'], row['OT'])
            )
            print(f"Updated row: {row['OT']}")
        else:
            cursor.execute(
                "INSERT INTO productivity (idproductivity, dateStart, startTime, endTime, idtasks, idprojects, documents, images, status, caNumber, idboxes, totalTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (row['OT'],row['Date'], row['StartTime'], row['EndTime'], row['idT'], row['idP'], row['Folders'], row['Images'], row['Status'], row['caNumber'], row['Boxes_Id'], row['Time'])
            )
            print(f"New row: {row['OT']}")
