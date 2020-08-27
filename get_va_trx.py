import mysql.connector
import requests
import time

def updateData(query_):
    cnx = mysql.connector.connect(user='test', password='1234', host='127.0.0.1',  database='db')
    conn = cnx.cursor()
    conn.execute(query_)
    conn.close()
    cnx.commit()
    cnx.close()
    print(query_)
    
def singlequeryData(query_):
    cnx = mysql.connector.connect(user='test', password='1234', host='127.0.0.1',  database='db')
    conn = cnx.cursor()
    conn.execute(query_)
    data = conn.fetchone()
    conn.close()
    cnx.close()
    print(query_)
    return data

r = requests.get("http://10.2.2.8/_va/get_transaksi.php?t=1")

msg = r.content
nums = msg.decode('utf8').split('##')
no = 0
for num in nums:
    print (num)
    no=no+1
    if(no%500==3):
        print("sleep", no)
        time.sleep(2)
    if(len(num)>70):
        qq = num.split('@')
        print (qq[1])
        sqlq = "SELECT COUNT(id) AS 'qq' FROM keu_tblTransaksiMahasiswa WHERE id_kwitansi='"+qq[0]+"' AND NPK='"+qq[1]+"' "
        print(sqlq)
        mydata = singlequeryData(sqlq)
        print("data0->", mydata[0])
        if(mydata[0]==0):
            #print(qq[1]," ",qq[2]," ",qq[3])
            updateData(qq[3])
            totalbayar_va = singlequeryData("SELECT SUM(jumlah_bayar) FROM keu_tblTransaksiMahasiswa WHERE kode_biaya='VA' AND NPK='"+qq[1]+"' ")
            print(totalbayar_va[0])
            query="UPDATE keu_tblTanggunganMahasiswa SET total_bayar='"+str(totalbayar_va[0])+"' WHERE kode_biaya='VA' AND NPK='"+qq[1]+"' "
            print(query)
            updateData(query)
             


