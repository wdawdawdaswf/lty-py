from flask import Flask,render_template,request,session,redirect

#创建一个Flask类的对象
app = Flask(__name__)
# 给session 加盐，加密
app.secret_key='123'
@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
    # 打印客户端发来得是什么请求信息
    print(request.method)
    #
    request.args #获取get请求信息
    if request.method == 'GET':
        print(request.args)
        return render_template('login.html')
    else:
        user=request.form.get('user')
        pwd=request.form.get('pwd')
        print(user,pwd)
        if user == 'admin' and pwd =='admin':
            # 用户信息放入session
            session['user_info'] = user
            print(user,pwd,'恭喜登录成功！！！')
            return render_template('admin_index.html',msg = user)
        else:
            # return render_template('login.html',msg = '用户名或者密码错误')
            return "账户密码或者错误！！"
    #request.form #获取post请求信息
    #return render_template('login.html')

@app.route('/login')
def admin_index():
    user_info = session.get('user_info')
    print(user_info)
    if user_info !="":
        print('登录成功！')
        return render_template('login.html')
    else:
        print('登录失败！')



@app.route('/')
def index():
    print("t")
    #return render_template('index.html')
    user_info = session.get('user_info')
    if user_info !="":
        print('登录成功！')
        return render_template('index.html',msg = '用户名或者密码错误')
    else:
        print('登录失败！')

if __name__ == '__main__':
    app.run(port=8000)