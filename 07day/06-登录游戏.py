print("请选择游戏")
name = input("1王者荣耀，2 植物大战僵尸")
account = "123123"
paw = "456456"
if name == "1":
    acc = input("输入账号") 
    p = input("输入密码")  
    if acc == account and p == paw:
        print("欢迎来到王者峡谷")
    else:
        print("登录失败")
elif name == "2":
    print("一大波僵尸来袭")
