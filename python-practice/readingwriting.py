import time
import math
import json


def main1():
    with open("./pyproject.toml", "r", encoding="utf-8") as f:
        print(f.read())
    with open("./pyproject.toml", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
            time.sleep(0.2)
    with open("./pyproject.toml", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(lines)


def is_prime(n):
    if n <= 1:
        return False
    # 求n是不是素数，就是1和n，不能被其他自然数整除，就是就n的因数 a*b = n,但是a，b都小于n的，所以可以求n的二次平方根
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


file_names = ["a.txt", "b.txt", "c.txt"]
file_obj_list = []
try:
    for filename in file_names:
        file_obj_list.append(open(filename, "w", encoding="utf-8"))

    for num in range(1, 10000):
        if is_prime(num):
            if num < 100:
                file_obj_list[0].write(str(num) + "\n")
            elif num < 1000:
                file_obj_list[1].write(str(num) + "\n")
            elif num < 10000:
                file_obj_list[2].write(str(num) + "\n")
except IOError as ex:
    print(ex)
    print("writing error")
finally:
    for file_obj in file_obj_list:
        file_obj.close()
    print("done")

try:
    with open("./code.png", "rb") as f:
        data = f.read()
        print(type(data))
    with open("./code2.png", "wb") as f:
        f.write(data)
except FileNotFoundError as e:
    print("file not found")
except IOError as e:
    print("write and read error")

# if __name__ == "__main__":
# main()


def main():
    mydict = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320},
        ],
    }
    try:
        with open("data.json", "w", encoding="utf-8") as fs:
            json.dump(mydict, fs)
            # 将python对象以json数据格式序列化到文件中
            json_text = json.dumps(mydict)
            print(json_text)
            # 将python对象序列化为json数据格式的字符串
        with open("./data.json", "r", encoding="utf-8") as fs:
            dic_obj = json.load(fs)  # 将文件中的json数据反序列化为pythob对象
            print(dic_obj)
            print(json.loads(json_text))
            # 将json数据格式的字符串反序列化为python对象
    except IOError as e:
        print(e)
    print("保存数据完成!")


main()
