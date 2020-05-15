import hashlib
# import datetime
import threading
import pymysql
from threading import Lock

semLock = Lock()
onNonce = False

def Mining(id) :

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="db_python")
    cur = conn.cursor()
    query = 'select * from data_pool where id = %s'
    args = (id)
    cur.execute(query,args)
    test = cur.fetchone()

    nonce = 0
    found = False

    while not found :
        hash_nonce = str(hashlib.sha224((str(test)+str(nonce)).encode('utf-8')).hexdigest())
        if hash_nonce[:6] == '117036' :
            found = True
        nonce += 1
        global onNonce
        if onNonce == True :
            found = True

    semLock.acquire()

    onNonce = True
    query = "DELETE from data_pool WHERE id = %s"
    cur.execute(query,(id))

    conn.commit()

    query = "SELECT count(*) as tot FROM blockchain where id = %s "
    cur.execute(query,(id))
    res = cur.fetchone()[0]

    if res == 0 :
        query = "Insert INTO blockchain (id, data, timestamp, prevhash, hash, nonce) values (%s, %s, %s, %s, %s, %s)"
        test = list(test)
        test.append(str(nonce))
        values = tuple(test)
        cur.execute(query, values)
        conn.commit()

    conn.close()
    semLock.release()

def main() :
    iter = 0
    stop = True
    iterv2 = 0
    while stop :
        conn = pymysql.connect(host="localhost", user="root", passwd="", db="db_python")
        cur = conn.cursor()
        if iter >= 10 :
            stop = False
        global onNonce
        onNonce = False
        query = "SELECT count(*) as tot FROM data_pool"
        cur.execute(query)
        data = cur.fetchall()[0][0]
        print("data : %s" % str(data))
        if data != 0 :
            query2 = "SELECT id FROM data_pool order by id"
            cur.execute(query2)
            result = cur.fetchone()[0]
            list_thread = []
            print('On id = %s' %result)
            print(iterv2)
            iterv2 += 1
            for i in range(4):
                list_thread.append(threading.Thread(target=Mining,args=(result)))
            for n in list_thread:
                n.start()
            for k in list_thread:
                k.join()
        else :
            iter += 1
        conn.close()


if __name__ == "__main__":
    main()

