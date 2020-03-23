import requests
import json
import time
import pymysql
import sql_synatx
from selenium.webdriver import Chrome,ChromeOptions
def sprider_tencent():
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    url_h5 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    url_other='https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    res_h5=requests.get(url_h5,headers=header)
    content_h5=json.loads(res_h5.text)
    res_other=requests.get(url_other,headers=header)
    content_other=json.loads(res_other.text)
    data=json.loads(content_other['data'])
    data_all=json.loads(content_h5['data'])
    return data, data_all

def history(data):
    history = {}  # 历史数据
    history_list=[]
    for i in data["chinaDayList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式,不然插入数据库会报错，数据库是datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data["chinaDayAddList"]:
        ds_add = "2020." + i["date"]
        tup_add = time.strptime(ds_add, "%Y.%m.%d")
        ds_add = time.strftime("%Y-%m-%d", tup_add)
        confirm_add = i["confirm"]
        suspect_add = i["suspect"]
        heal_add = i["heal"]
        dead_add = i["dead"]
        history[ds_add].setdefault(("confirm_add", "suspect_add", "heal_add", "dead_add"),(0,0,0,0))# 设置默认的字典格式， 然后两边都是元组的格式
        history[ds_add].update({"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})
        
        # 设置字典使用get 返回默认值即可
    for key ,value in history.items():
        temp=dict(value)
        history_list.append((key,temp.get("confirm"),temp.get("suspect"),temp.get("heal"),temp.get("dead"),\
                            temp.get("confirm_add",0),temp.get("suspect_add",0),temp.get("heal_add",0),temp.get("dead_add",0)))
    return history_list
def details(data_all):        
        details = []  # 当日详细数据
        update_time = data_all["lastUpdateTime"]
        data_country = data_all["areaTree"]  # list 25个国家
        data_province = data_country[0]["children"]  # 中国各省
        for pro_infos in data_province:
            province = pro_infos["name"]  # 省名
            for city_infos in pro_infos["children"]:
                city = city_infos["name"]
                confirm = city_infos["total"]["confirm"]
                confirm_add = city_infos["today"]["confirm"]
                heal = city_infos["total"]["heal"]
                dead = city_infos["total"]["dead"]
                details.append((update_time, province, city, confirm, confirm_add, heal, dead))
        return details
def baidu():
    url_baidu=r"https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    # from selenium.webdriver.chrome.options import Options 从不同的地方读取的包都是可以使用
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # # 创建浏览器对象
    option=ChromeOptions()
    option.add_argument('--headless')# 隐藏浏览器
    option.add_argument('--no-sandbox')# 禁用沙盘模式
    np=time.strptime(time.asctime())
    k=time.strftime('%m-%d-%H:%M:%S',np)
    print(f"开始时间{k}")
    browser =Chrome(chrome_options=option)#可以直接调用本地的浏览器， 然后对数据进行爬取
    browser.get(url_baidu)
    # print(browser.page_source)
    content=browser.find_elements_by_xpath(r'//*[@id="ptab-0"]/div/div[2]/section/a/div/span[2]')
    # for i in content:
    #     print(i.text)
    # np=time.strptime(time.asctime())
    # k=time.strftime('%m-%d-%H:%M:%S',np)
    # print(f"结束时间{k}")
    value=[]
    for i in content:
        print(i.text)
        np=time.strptime(time.asctime())
        k=time.strftime('%Y-%m-%d %X',np)
        value.append((i.text,k))
    return value
#数据装入数据库
# 使用cov 的数据库
def create_table():
    db=pymysql.connect(host='localhost',user='root',password='ycy1234')
    cursor=db.cursor()
    # 写一个try 语句
    #创建数据库
    sql_database='create database if not exists `cov`'
    drop_table1='DROP TABLE IF EXISTS `history`'
    drop_table2='DROP TABLE IF EXISTS `details`'
    drop_table3='DROP TABLE IF EXISTS `hotsearch`'
    cursor.execute(sql_database)
    cursor.execute('use`cov`')
    cursor.execute(drop_table1)
    cursor.execute(drop_table2)
    cursor.execute(drop_table3)
    #创建数据表
    cursor.execute(sql_synatx.sql_table)
    print("创建表1 history ...")
    cursor.execute(sql_synatx.sql_table1)
    print("创建表2 details ...")
    cursor.execute(sql_synatx.sql_table2)
    print("创建表3 hotsearch ...")
    close_conn(db,cursor)


    
def get_conn():
    conn=pymysql.connect("localhost","root","ycy1234","cov")
    cursor=conn.cursor()
    return conn,cursor# 返回的形式是元组
def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def insert_table(details,history_list,value):
    #插入数据,才用直接全部插入的形式
    sql_history="replace into history(ds,confirm,suspect,heal,dead,confirm_add,suspect_add,heal_add,dead_add) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #insert into history((ds,confirm,suspect,heal,dead,confirm_add,suspect_add,heal_add,dead_add) values('2020-01-13', 41, 0, 0, 1, 0, 0, 0, 0);
    sql_details="replace into details(update_time,province,city,confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"# 更新部分数据需要设置更新的键值
    sql_insert='replace into `hotsearch`(content,dt)values(%s,%s)'
    db,cursor=get_conn()
    print(f"{time.asctime()}开始更新--details--最新数据")
    cursor.executemany(sql_details,details)
    db.commit()
    print(f"{time.asctime()}开始更新--details--数据完毕")
    print(f"{time.asctime()}开始更新--history--最新数据")
    cursor.executemany(sql_history,history_list)
    db.commit()
    print(f"{time.asctime()}开始更新-- history--数据完毕")
    print(f"{time.asctime()}开始更新--hotsearch--最新数据")
    cursor.executemany(sql_insert,value)
    db.commit()
    print(f"{time.asctime()}开始更新--hotsearch--数据完毕")
    close_conn(db,cursor)
    

    # try:

    #     cursor.executemany(sql_details,details)
    #     db.commit()
    #     print(f"{time.asctime()}更新最新--details--数据完毕")
    # except Exception as e:
    #     db.rollback()
    #     print(f"{time.asctime()}数据回滚，更新失败！")
    # # 更新history 数据
    # finally:

    #     print(f"{time.asctime()}开始更新-- history--最新数据")
    #     try:
    #         cursor.executemany(sql_history,history_list)
    #         db.commit()
    #         print(f"{time.asctime()}更新最新-- history--数据完毕")
    #     except Exception as e:
    #         db.rollback()
    #         print(f"{time.asctime()}数据回滚，更新失败！")
    #     finally:
    #         try:
                
    #             cursor.executemany(sql_insert,value)
    #             db.commit()
    #             print(f"{time.asctime()}更新最新--hotsearch--数据完毕")
    #         except Exception as e:
    #             db.rollback()
    #             print(f"{time.asctime()}数据回滚，更新失败！")
    #         finally:
    #             close_conn(db,cursor)

if __name__=="__main__":

    data,data_all=sprider_tencent()
    
    history_list=history(data)
    # # print(data["chinaDayAddList"])
    # for i in data["chinaDayAddList"]:
    #     ds_add = "2020." + i["date"]
    #     tup_add = time.strptime(ds_add, "%Y.%m.%d")
    #     ds_add = time.strftime("%Y-%m-%d", tup_add)
    #     confirm_add = i["confirm"]
    #     suspect_add = i["suspect"]
    #     print(confirm_add,suspect_add)
    # print(history_list)
    details=details(data_all)
    value=baidu()
    create_table()
    insert_table(details,history_list,value)



