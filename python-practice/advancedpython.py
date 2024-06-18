import heapq
import itertools
import collections


def generate():
    prices = {"AAPL": 122, "GOOG": 1185, "IBM": 149, "ACN": 49, "SYMC": 21, "FB": 208}

    # 使用生成式创建新的dict,list, set
    prices1 = {key: value for key, value in prices.items() if value > 100}
    print(prices1)

    names = ["jack", "rose"]
    courses = ["english", "math", "physic"]

    scores = [[None] * len(courses) for _ in range(len(names))]

    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input("input score"))

    # print(scores)


def heapq_fn():
    # 从列表中找出最大的或最小的N个元素
    # 堆结构(大根堆/小根堆)
    list1 = [44, 22, 13, 45, 12, 35, 2, 67, 8]
    list2 = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35},
        {"name": "ACME", "shares": 75, "price": 115.65},
    ]
    print(heapq.nsmallest(2, list1))
    print(heapq.nlargest(2, list1))
    print(heapq.nsmallest(2, list2, key=lambda x: x["shares"]))
    print(heapq.nlargest(2, list2, key=lambda x: x["price"]))


def itertoolsfn():
    # ABCD的组合排列
    permutations = itertools.permutations("ABCD", 2)
    # print(list(permutations))
    for item in permutations:
        print(item, end=" ")
    # ABCD的不重复的组合排列
    combinations = itertools.combinations("ABCD", 2)
    # print(combinations)
    for item in combinations:
        print(item, end=" ")
    # ABCD和123的笛卡尔积
    products = itertools.product("ABCD", "123")
    for item in products:
        print(item, end="\n")
    counter = 0
    cycles = itertools.cycle(("A", "B", "C"))
    for item in cycles:
        print(item)
        if counter > 10:
            break
        counter += 1


def collectionsfn():
    # colletions 提供了许多具备高效功能的容器数据类型
    # namedtuple
    # 定义一个 Person的namedtuple， 包含 name age 两个字短
    Person = collections.namedtuple("Person", ["name", "age"])
    print(Person)
    person = Person(name="Alice", age=25)
    print(person)
    print(person.name)
    print(person.age)
    # <class '__main__.Person'>
    # Person(name='Alice', age=25)
    # Alice
    #  25
    # deque
    d = collections.deque()
    print(d)  # deque([])
    # 在队列两端添加元素
    d.append("B")
    d.appendleft("A")
    d.append("C")
    print(d)  # deque(['A', 'B', 'C'])
    # 从队列的两端溢出元素
    d.pop()
    d.popleft()

    # counter
    # Counter是一个计数器工具，提供了快速计数的功能，用于计数可哈希对象。
    c = collections.Counter("jkdsjfkjkbjahhfabdgda")
    print(c)  # 放回每个字母的个数
    # Counter({'j': 4, 'k': 3, 'd': 3, 'a': 3, 'f': 2, 'b': 2, 'h': 2, 's': 1, 'g': 1})
    print(c.most_common(2))  # [('j', 4), ('k', 3)] 获取最常出现的2个元素
    # OrderedDict
    # OrderedDict是字典的一种子类，记住了添加键值对的顺序。
    ordereddict = collections.OrderedDict()
    # 创建一个OrderedDict
    ordereddict["first"] = 1
    ordereddict["second"] = 2
    ordereddict["third"] = 3

    # 迭代键值对时会按插入顺序返回
    for key, value in ordereddict.items():
        print(key, value)
    # 输出：
    # first 1
    # second 2
    # third 3


if __name__ == "__main__":
    # heapq_fn()
    # itertoolsfn()
    collectionsfn()
