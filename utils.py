import re
import time

import pymysql
from jieba.analyse import extract_tags


def get_time():
    str_time=time.strftime("%Y{}%m{}%d{} %X")
    return str_time.format("年","月","日")

# 封装方法
def get_conn():
    conn=pymysql.connect("localhost","root","ycy1234","cov")
    cursor=conn.cursor()
    return conn,cursor# 返回的形式是元组
def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    conn,cursor=get_conn()
    cursor.execute(sql,args)# 设定arg为占位符
    res=cursor.fetchall()
    close_conn(conn,cursor)
    return res
def get_c1_data():
    sql='''
    select confirm, suspect, heal,dead\
    from history \
    where ds=(select ds from history  order by ds desc limit 1)
    '''
    res=query(sql)
    return res[0]
def get_c2_data(): #desc limit 1 表示获取最新的数据
    sql='''
    select province,cast(sum(confirm) as signed) from details \
    where update_time=(select update_time from details\
    order by update_time desc limit 1)\
    group by province
    '''
    res=query(sql)
    return res
def get_l1_data(): #desc limit 1 表示获取最新的数据
    sql='''
    select  ds,cast(confirm as signed), cast(suspect as signed),cast(heal as signed), cast(dead as signed) \
    from history

    '''
    res=query(sql)
    return res
def get_l2_data(): #desc limit 1 表示获取最新的数据
    sql='''
    select  ds,cast(confirm_add as signed), cast(suspect_add as signed) \
    from history
    '''
    res=query(sql)
    return res
def get_r1_data(): #desc limit 1 表示获取最新的数据
    sql='''
    select city ,confirm from details\
    where (province !="湖北")and(update_time=(select update_time from details\
    order by update_time desc limit 1))\
    order by confirm desc limit 5
    '''
    res=query(sql)
    return res
def get_r2_data(): #desc limit 1 表示获取最新的数据
    sql='''
    select content from hotsearch\
    where dt=(select dt from hotsearch order by dt limit 1);
    '''
    res=query(sql)
    return res

if __name__=="__main__":
    # print({"confirm":int(data[0]),"suspect":int(data[1]),"heal":data[2],"dead":data[3]})
    # data=get_c2_data()
    # res = []
    # for tup in get_c2_data():
    #     # print(tup)
    #     res.append({"name":tup[0],"value":int(tup[1])})
    # time=time.strftime("%m.%d",i)
    # res=get_l2_data()
    # ds=[]
    # confrim=[]
    # suspect=[]
    # for i in res:
        
    #     tup="{}.{}".format(str(i[0].__getattribute__('month')),str(i[0].__getattribute__('day')))
    #     print(tup)
    #     # tup = time.strptime(i[0], "%Y-%m-%d %X")
    #     # time=time.strftime("%m.%d",tup)
    #     ds.append(tup)
    #     confrim.append(i[1])
    #     suspect.append(i[2])
    # print({"data":[ds,confrim,suspect]})
    # data=get_r2_data()
    # print(data)
    # content=[]
    
    # for i in data:
    #     n=re.search("[\u4e00-\u9fa5]([\d]+)$",i[0])
    #     m=re.search("^(.*[\u4e00-\u9fa5])",i[0])
    #     temp=extract_tags(m.group(1))
    #     values=n.group(1)
    #     for tags in temp:
    #         content.append({"name":tags,"value":values})
    #     # n.group(1) ,m.group(1)
    #     print(content)

        # city.append(i[0])
        # number.append(i[1])
    # print({"data":[city,number]})
    # res=get_l2_data()
    # ds=[]
    # confrim=[]
    # suspect=[]
    # for i in res:
        
    #     tup="{:0>2d}.{:0>2d}".format(int(i[0].__getattribute__('month')),int(i[0].__getattribute__('day')))
    #     print(tup)
    data=get_c1_data()
    print(data)
    # content=[]
    # for i in data:
    #     n=re.search("[\u4e00-\u9fa5]([\d]+)$",i[0])
    #     m=re.search("^(.*[\u4e00-\u9fa5])",i[0])
    #     temp=extract_tags(m.group(1))
    #     values=n.group(1)
    #     for tags in temp:
    #         content.append({"name":tags,"value":values})
    # print(content)
