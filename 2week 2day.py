memu = ("돈까스", "치즈돈까스")
print(memu[0])
print(memu[1])

name ="피그랫"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피그", 21, "코코")
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
print(departure,">", arrival)
(departure, arrival) = (arrival,departure )
print(departure,">", arrival)

my_set = {1,2,3,3,3}
print(my_set)

java = {"푸", "피그렛", "티거"}
python = set(["푸", "이요르"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("피그렛")
print(python)

java.remove("피그렛")
print(java)



