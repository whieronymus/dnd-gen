from rollstats import roll_stats

int1 = 0
int2 = 0
int3 = 0
int4 = 0
int5 = 0
int6 = 0

times_through_loop = input("How many times should I roll?: ")

for i in range(int(times_through_loop)):
    stat_list = roll_stats()
    int1 += stat_list[0]
    int2 += stat_list[1]
    int3 += stat_list[2]
    int4 += stat_list[3]
    int5 += stat_list[4]
    int6 += stat_list[5]

new_average = []
new_average.append(int1 / int(times_through_loop))
new_average.append(int2 / int(times_through_loop))
new_average.append(int3 / int(times_through_loop))
new_average.append(int4 / int(times_through_loop))
new_average.append(int5 / int(times_through_loop))
new_average.append(int6 / int(times_through_loop))

print(new_average)

    