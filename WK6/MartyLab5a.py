def search_Email():
    for in range(len(email)):
        if dept[i] == "MIS":
            email[i] = email[i].replace(".com", ".net")
            count +=1
    return count

def get_data():
    rows = 0

    with open("C:/Lab5A.txt") as f:
        data = csv.reader(f)
        for row in data:
            fname.append(row[0])
            lname.append(row[1])
            phone.append(row[2])
            email.append(row[3])
            dept.append(row[4])
            employeePosition.append(row[5])
        rows += 1
    return rows

#============ Main Program ===============

