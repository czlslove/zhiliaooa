(本项目是基于Python+flask+mysql的一个问答论坛)做完本项目可以让你对flask框架有一个基础的理解  
=======
部署项目
-------

### 1.本机安装python解释器环境，最好在3.10.0版本及以上 
    
### 2.使用pip安装以下python包 
  
pip install  flask flask_migrate flask_mail flask-wtf email-validator -i https://pypi.tuna.tsinghua.edu.cn/simple  
  
### 3.安装mysql，将用户名和密码都设置为root，创建名为zhiliaooa的数据库（字符集为utf8）  
  
CREATE DATABASE zhiliaooa CHARACTER SET utf8;  
  
### 4.配置数据库表  
  
删除migrations这个目录  
执行flask db init  
在执行flask db migrate    
最后执行flask db upgrade    
  
### 5.运行app.py启动项目  
  
python app.pyp  
  
### 6.访问本机5000端口  

http://127.0.0.1:5000/  
