subway=[10, 20, 30]
print(subway)

subway = ["푸", "피글렛", "티거"]
print(subway)

print(subway.index('피글렛'))

subway.append("이요르")
print(subway)

subway.insert(1, "루")
print(subway)

print(subway.pop())      
print(subway)

subway.clear()
print(subway)

subway = ["푸", "피글렛", "티거"]
subway.append("푸")
print(subway)
print(subway.count('푸'))

num_list =[5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)

mix_list = ["푸", 20, True, [5,2,4,3,1]]
print(mix_list)

mix_list = ["푸", 20, True]
num_list =[5,2,4,3,1]
num_list.extend(mix_list)
print(mix_list)
print(num_list)

cabinet = {3:"푸", 100:"피그렛"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5))
print("hi")
# print(cabinet[5])
# print("hi")
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3" : "푸", "B-100" : "피그랫"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["A-3"] = "티거"
cabinet["C-20"] = "이요르"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)