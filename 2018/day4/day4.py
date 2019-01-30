import re
<<<<<<< HEAD
import copy
=======
>>>>>>> sweep up commit

file = open("input", "r")

lines = [x.strip('\n)') for x in file.readlines()]
<<<<<<< HEAD
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
=======

# [1518-11-21 23:58] Guard #3541 begins shift
# m = re.search('#(\d{1,4})\s@\s(\d*,\d*):\s(\d*x\d*)', claim)

guard_sleep_totals = dict()
guard_id = ''
for line in sorted(lines):
  guard_start = re.search('#(\d*)', line)
  if guard_start != None:
    guard_id = guard_start.group(1)
    start_hour = 0
    start_minute = 0
    end_hour = 0
    end_minute = 0
    # print guard_id
  else:
    guard_asleep = re.search('(\d\d):(\d\d)]\sfalls asleep', line)
    if guard_asleep != None:
      start_hour = guard_asleep.group(1)
      start_minute = guard_asleep.group(2)
      end_hour = 0
      end_minute = 0
      # print start_hour + " " + start_minute
    else:
      guard_awake = re.search('(\d\d):(\d\d)]\swakes up', line)
      if guard_awake != None:
        end_hour = guard_awake.group(1)
        end_minute = guard_awake.group(2)
        # print "Guard " + guard_id + " spent " + str(int(end_minute)-int(start_minute)) + " minutes asleep"

        if guard_id not in guard_sleep_totals:
          guard_sleep_totals[guard_id] = 0

        guard_sleep_totals[guard_id] += (int(end_minute)-int(start_minute))

        # print end_hour + " " + end_minute


>>>>>>> sweep up commit

