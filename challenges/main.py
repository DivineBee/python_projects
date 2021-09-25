import csv
import pandas
import random

# with open("myfile.txt", mode="a") as file:
#     file.write("ggggggggg")

# with open("weather_data.csv") as file:
#     weather_list = csv.reader(file)
#     temperatures = []
#     for row in weather_list:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data.to_dict())
#
#
# max = data["temp"].max()
# print(data[data.temp == max])
#
# monday = data[data.day == "Monday"]
# monday_fahr = int(monday.temp * 9/5 + 32)
# data[monday] = monday_fahr
# print(data[monday])

# LIST COMPREHENSION
# file1 = open("file1.txt")
# list1 = file1.readlines()
#
# file2 = open("file2.txt")
# list2 = file2.readlines()
#
# result = [int(f) for f in list1 if f in list2]
# print(result)


# names = ["sam", "pam", "liam", "court"]
#
# score = {name: random.randint(1, 100) for name in names}
#
# passed = {student: score for (student, score) in score.items() if score > 50}
# print(score)
# print(passed)
#


# student_dict = {
#     "student": ["san", "tur", "ger"],
#     "score": [23, 56, 45]
# }
# student_frame = pandas.DataFrame(student_dict)
#
# for (index, row) in student_frame.iterrows():
#     if row.student == "san":
#         print(row.score)
#

# NATO ALPHABET
df = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Enter name").upper()
    try:
        result = [dict[letter] for letter in user_input]
    except KeyError:
        print("only letters allowed")
        generate_phonetic()
    else:
        print(result)
        is_word = True


generate_phonetic()
