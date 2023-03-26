# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0" ,file= score_file)
# print("영어 : 0" ,file= score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 80\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.read())
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # print(score_file.readline(), end="")
# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

import pickle 
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "스누피", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)

# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)

# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file) )

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

for weekend in range(1,51):
    filename = (str(weekend) +"주차.txt")
    # print(filename)
    with open(filename, "w", encoding="utf8") as filename_file:
        filename_file.write("- " + str(weekend) + "주차 주간보고 -\n")
        filename_file.write("부서 :\n")
        filename_file.write("이름 :\n")
        filename_file.write("업무 요약 :\n")