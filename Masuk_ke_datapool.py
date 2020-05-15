import hashlib
import datetime
import pymysql
# import sys

#Connect Dulu
conn = pymysql.connect(host="localhost", user="root", passwd="", db="db_python")
data1 = ['budi','tono','bambang','susanti','dwi']
data2 = ['data1','data2','data3','data4']
data = data2
cur = conn.cursor()
query = "SELECT * FROM data_ins"
cur.execute(query)
check = cur.fetchone()
i = 0
#Check kalau ada data di table sementara atau tidak
if check is None :
    print('Inserting Data')
    while i <= (len(data)-1) :
        id = i + 1
        val = str(data[i])
        time = str(datetime.datetime.now())
        print(id,val,time)
        query = "INSERT INTO data_ins(id,data,timestamp) VALUES(%s,%s,%s)"
        args = (str(id),str(val),str(time))
        cur.execute(query, args)
        conn.commit()
        i += 1
else :
    print('Table not null')

text = input("Data has been inserted to temporary. Press enter!")
# Ambil semua data yang ada di table sementara
query = "SELECT id,data,timestamp FROM data_ins ORDER BY timestamp"
cur.execute(query)
insert = cur.fetchall()
# print(insert)

# Pemeriksaan data pool
query = "SELECT count(*) as tot FROM data_pool"
cur.execute(query)
mr = cur.fetchone()[0]
if mr != 0 :
    query = "Select id from data_pool order by id desc"
    cur.execute(query)
    resId = cur.fetchone()[0]
    newid = int(resId)
else :
    # sql = "Select num from blockchain order by num desc"
    # cur.execute(sql)
    # resId = cur.fetchone()
    newid = 0

for i in range(len(insert)) :
    newid = newid + 1
    query = "SELECT count(*) as tot FROM data_pool"
    cur.execute(query)
    data = cur.fetchall()[0][0]
    prevhash = str(0)
    if data != 0:
        query = "Select hash from data_pool order by id desc"
        cur.execute(query)
        prevhash = str(cur.fetchone()[0])
    else:
        # query = "Select hash from blockchain order by num desc"
        # cur.execute(query)
        prevhash = str(0)
    hash = str(hashlib.sha224((str(newid)+str(insert[i][1])+str(insert[i][2])+prevhash).encode('utf-8')).hexdigest())

    ins_dp = {'id': str(newid),
            'data': str(insert[i][1]),
            'timestamp': str(insert[i][2]),
            'prevhash': str(prevhash),
            'hash': str(hash)}

    query = "Insert INTO data_pool (id, data, timestamp, prevhash, hash) values (%s, %s, %s, %s, %s)"
    value = (ins_dp['id'], ins_dp['data'], ins_dp['timestamp'], ins_dp['prevhash'],
           str(ins_dp['hash']))
    cur.execute(query, value)
    query = "DELETE FROM data_ins WHERE id = %s" % insert[i][0]
    cur.execute(query)
    conn.commit()

print('Data has been inserted to Data Pool')
cur.close()
conn.close()

