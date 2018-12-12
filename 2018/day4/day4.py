import re
import copy

file = open("input", "r")

lines = [x.strip('\n)') for x in file.readlines()]
# lines = ["[1518-11-01 00:00] Guard #10 begins shift",
#         "[1518-11-01 00:05] falls asleep",
#         "[1518-11-01 00:25] wakes up",
#         "[1518-11-01 00:30] falls asleep",
#         "[1518-11-01 00:55] wakes up",
#         "[1518-11-01 23:58] Guard #99 begins shift",
#         "[1518-11-02 00:40] falls asleep",
#         "[1518-11-02 00:50] wakes up",
#         "[1518-11-03 00:05] Guard #10 begins shift",
#         "[1518-11-03 00:24] falls asleep",
#         "[1518-11-03 00:29] wakes up",
#         "[1518-11-04 00:02] Guard #99 begins shift",
#         "[1518-11-04 00:36] falls asleep",
#         "[1518-11-04 00:46] wakes up",
#         "[1518-11-05 00:03] Guard #99 begins shift",
#         "[1518-11-05 00:45] falls asleep",
#         "[1518-11-05 00:55] wakes up"]

guard_asleep = dict()
times = dict()
guard_id = 0
wake_time = 0
sleep_time = 0
for x in range(60):
  times[x] = 0

for line in sorted(lines):
  words = line.split()
  if words[2] == 'Guard':
    guard_id = int(words[3][1:])
  elif words[2] == 'falls':
    sleep_time = int(words[1][3:5])
  else:
    wake_time = int(words[1][3:5])

    if guard_id not in guard_asleep:
      guard_asleep[guard_id] = copy.deepcopy(times)

    for time in range(sleep_time, wake_time):
      guard_asleep[guard_id][time] += 1

highest_guard_id = 0
highest_guard_value = 0
for guard_id in guard_asleep:
  if sum(guard_asleep[guard_id].values()) > highest_guard_value:
    highest_guard_value = sum(guard_asleep[guard_id].values())
    highest_guard_id = guard_id

print "Day 4 Part 1 = " + str(highest_guard_id * max(zip(guard_asleep[highest_guard_id].values(), guard_asleep[highest_guard_id].keys()))[1])

print "Day 4 Part 2 = " + str(max([(k, max(d.iteritems(), key=lambda a:a[1])) for k, d in guard_asleep.iteritems()], key=lambda a:a[1][1]))
# 65854

