from random import random, randint

map_one_sq = []
map_two_sq = []


for i in range(9):
    while True:
        a = randint(1, 9)
        if map_one_sq.count(a) == 0:
            map_one_sq.append(a)
            break


lst1 = [map_one_sq[0], map_one_sq[1], map_one_sq[2]]
lst2 = [map_one_sq[3], map_one_sq[4], map_one_sq[5]]
lst3 = [map_one_sq[6], map_one_sq[7], map_one_sq[8]]












print(str(map_one_sq[0]) + "|" + str(map_one_sq[1])+ "|" + str(map_one_sq[2]))
print("-----")
print(str(map_one_sq[3]) + "|" + str(map_one_sq[4])+ "|" + str(map_one_sq[5]))
print("-----")
print(str(map_one_sq[6]) + "|" + str(map_one_sq[7])+ "|" + str(map_one_sq[8]))


print("\n")


print(str(map_two_sq[0]) + "|" + str(map_two_sq[1])+ "|" + str(map_two_sq[2]))
print("-----")
print(str(map_two_sq[3]) + "|" + str(map_two_sq[4])+ "|" + str(map_two_sq[5]))
print("-----")
print(str(map_two_sq[6]) + "|" + str(map_two_sq[7])+ "|" + str(map_two_sq[8]))

#print(map_one_sq)
