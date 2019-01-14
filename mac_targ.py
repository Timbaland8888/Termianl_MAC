
#!/user/bin/python
#function:get mac to db
#date:20190114
#Arthor:Timbaland

import  os
import pymysql
import configparser


class HJ_PC(object):
    def __init__(self, host, user, pwd, port, db, charset):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.db = db
        self.charset = charset

    # 教室里面的PC MAC信息
    def input_mac(self, isql):
        try:
            # 连接mysql数据库参数字段
            con = None
            db = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db, port=self.port,
                                 charset=self.charset)
            cursor = db.cursor()
            cursor.execute(isql)
            db.commit()

        except ValueError:
            db.roolback
            print  ('error')
        # 关闭游标和mysql数据库连接
        cursor.close()
        db.close()
        return 'success'
#read configure
cf = configparser.ConfigParser()
cf.read('config.ini', encoding='utf-8')
scode =cf['dhcp']['dhcp_scode']
# print(scode.strip(',').split(','))
 #Collecting pc information
mac_result = []
for dchp_ip in scode.strip(',').split(',') :
    # print(dchp_ip)
    # print('netsh dhcp server {0} scope {1} show clients'.format(cf['dhcp']['dhcp_host'],dchp_ip))
    result = os.popen('netsh dhcp server {0} scope {1} show clients'.format(cf['dhcp']['dhcp_host'],dchp_ip)).readlines()[8:-4]
    # print(len(result))

    for i  in range(len(result)):

        m = list(result[i].split())[3]
        # print(m)
        p  = list(result[i].split())[4]
        if m != '-':
            mac_result.append(m)
        if p != '-':
            mac_result.append(p)
#MAC count
print(len(mac_result))
#list mac
for k in mac_result:
    print(k)



# print type(result.read())
# PC_IP =
# print(result)

# print(cf['hj_db']['db_host'])