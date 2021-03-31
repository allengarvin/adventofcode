#!/usr/bin/python3

import datetime as dt

def read_log(fn):
    guard_times = dict()

    lines = sorted([x.replace("1518", "2018") for x in open(fn)])

    for l in lines:
        tm = dt.datetime.strptime(l[:18].replace("1518", "2018"), "[%Y-%m-%d %H:%M]")
        l = l[19:].strip()
        if l.startswith("Guard #"):
            guard_num = int(l[7:].split()[0])
            arr = guard_times.get(guard_num, [])
            guard_times[guard_num] = arr
        else:
            arr += [tm]
    return guard_times

def intervals(time_arr):
    return [(a.minute, b.minute) for a, b in zip(time_arr[::2], time_arr[1::2])]

def total_minutes(time_arr):
    return sum([(b-a) for a, b in intervals(time_arr)])

def sleepiest_minute(ints):
    minutes = dict()
    for a, b in intervals(ints):
        for i in range(a, b):
            minutes[i] = minutes.get(i, 0) + 1

    return sorted(minutes.keys(), key=lambda x: minutes[x])[-1]

def main(fn):
    times = read_log(fn)

    totals = { g : total_minutes(tms) for g, tms in times.items() }
    sleepiest = sorted(totals.keys(), key=lambda g: totals[g])[-1]

    print(sleepiest * sleepiest_minute(times[sleepiest]))
    
    guards_by_minute = { g : sleepiest_minute(tms) for g, tms in times.items() if tms }
    minutest_guard = sorted(guards_by_minute.keys(), key=lambda g: guards_by_minute[g])[-1]
    print(minutest_guard * guards_by_minute[minutest_guard])
