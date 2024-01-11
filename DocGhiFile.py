
import  csv
with open('test.csv','w', newline='') as f:
    fiedName = { 'user', 'password'}
    writer = csv.DictWriter(f,fieldnames= fiedName)
    writer.writeheader()
    writer.writerow({'user':'2154050273','password':'' })
with open('test.csv','r', newline='') as f:
    reader=csv.DictReader(f)
    for i in reader:
        user = i['user']
        password = i['password']
print(user + password)



