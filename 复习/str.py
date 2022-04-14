name = "alen pink"
print(name)
print(name.title())  # 单词首字母大写
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写

msg = "hello, " + name + "!"  # 拼接字符串
print(msg)

msg = " python "
print(msg)
print(msg.lstrip())  # 删除左边空白
print(msg.rstrip())  # 删除右边空白
print(msg.strip())   # 删除左右空白
msg = msg.strip()    # 永久删除空白
print(msg)

age = 23
msg = "you are " + str(age) + " old."
print(msg)
