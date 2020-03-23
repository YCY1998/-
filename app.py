from flask import Flask
from flask  import request
from flask import render_template
import utils
from flask import jsonify
import re
import string
from jieba.analyse import extract_tags
app=Flask(__name__)
@app.route('/')
def helloworld():
    return render_template('main.htm')

@app.route("/login")#函数设置也不能设置相同
def helloworld1():
    good=request.values.get("id")# 必须使用f来传递参数
    return f'''
    <form action="/temp">
    账号:<input name="name" value={good}><br>
    密码:<input name="pwd">
    <input type="submit">
    </form>
    '''
@app.route("/temp")
def helloworld2():
    name=request.values.get("name")
    pwd=request.values.get("pwd")
    return f"name={name},pwd={pwd}"
@app.route("/tem")
def helloword3():
    return render_template("index.html")
@app.route('/ajax',methods=['get','post'])
def helloword4():
    name=request.values.get('name')
    score=request.values.get('score')
    print(f"{name}的分数是{score}")
    return '10000'
@app.route('/time')
def get_time():
    return(utils.get_time())
@app.route("/data")
def get_c1_data():
    data=utils.get_c1_data()
    return jsonify({"confirm":int(data[0]),"suspect":int(data[1]),"heal":int(data[2]),"dead":int(data[3])})
@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})
@app.route("/l1")
def get_l1_data():
    res=utils.get_l1_data()
    ds=[]
    confrim=[]
    suspect=[]
    heal=[]
    dead=[]
    for i in res:
        
        tup="{:0>2d}.{:0>2d}".format(int(i[0].__getattribute__('month')),int(i[0].__getattribute__('day')))
        print(tup)
        # tup = time.strptime(i[0], "%Y-%m-%d %X")
        # time=time.strftime("%m.%d",tup)
        ds.append(tup)
        confrim.append(i[1])
        suspect.append(i[2])
        heal.append(i[3])
        dead.append(i[4])
    return jsonify({"data":[ds,confrim,suspect,heal, dead]})

@app.route("/l2")
def get_l2_data():
    res=utils.get_l2_data()
    ds=[]
    confrim=[]
    suspect=[]
    for i in res:
        
        tup="{:0>2d}.{:0>2d}".format(int(i[0].__getattribute__('month')),int(i[0].__getattribute__('day')))
        # print(tup)
        # tup = time.strptime(i[0], "%Y-%m-%d %X")
        # time=time.strftime("%m.%d",tup)
        ds.append(tup)
        confrim.append(i[1])
        suspect.append(i[2])
    return jsonify({"data":[ds,confrim,suspect]})
@app.route("/r1")
def get_r1_data():
    data=utils.get_r1_data()
    city=[]
    number=[]
    for i in data:
        city.append(i[0])
        number.append(i[1])
    return jsonify({"data":[city,number]})
@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜数字
        v = i[0][len(k):]  # 获取热搜数字
        ks = extract_tags(k)  # 使用jieba 提取关键字
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"data": d})

if __name__=="__main__":
    app.run()

