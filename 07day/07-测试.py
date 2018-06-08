name = input("请输入你的名字")
tender = input("请输入你的性别")
if tender == "男":
    gao = int(input("请输入你的身高"))
    money = int(input("请输入你的财富"))
    yanz = int(input("请输入你的颜值"))
    if gao >= 180 and money > 1000 and yanz > 90:
        print("高富帅")
    else:
        print("稳住,别哭")
if tender == "女":
    color = input("请输入你的肤色")
    caif = int(input("请输入你的财富"))
    yz = int(input("请输入你的颜值"))
    if color == "白" and caif > 1000  and yz > 90:
        print("白富美")
    else:
        print("哈哈哈")
