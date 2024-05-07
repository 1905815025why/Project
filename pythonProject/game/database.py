import sqlite3                                      #连接SQLite数据库
link = sqlite3.connect('user.db')                   #连接SQLite3数据库，数据库文件是user.db
cursor = link.cursor()                              #创建游标
#像数据库中插入数据
# cursor.execute('''
#     create table user (
#     id int(10) primary key,
#     username varchar(3) not null,
#     password varchar(6) not null
#     )
# ''')
user1=('''
    insert into user(id,username,password)
    values (0000000002,'saz','123456abc')
    
''')
sql=cursor.execute(user1)
for row in sql:
    print("id=",row[0])
    print("name=",row[1])
    print("password=",row[2],"\n")
cursor.close()                                      #关闭游标
link.commit()                                       #提交事务
link.close()