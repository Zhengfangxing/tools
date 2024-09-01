# 打开文件并读取内容
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(content)

# 打开文件并逐行读取
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # 使用 strip() 去除行末的换行符

# 读取文件的前 5 行
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = [next(file) for _ in range(5)]

print(''.join(lines))

# 读取文件的所有行到一个列表中
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(lines)

# 逐块读取文件内容
chunk_size = 1024  # 每次读取 1024 字节
with open('example.txt', 'r', encoding='utf-8') as file:
    while chunk := file.read(chunk_size):
        print(chunk)
