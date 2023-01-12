# author: tobebetter9527
# since: 2023/01/11 21:40
print("hello world")

fp = open('E:/hello.txt', 'a+')
print("Hello world!", file=fp)
fp.close()

print("hello", "world", "你好，世界")
