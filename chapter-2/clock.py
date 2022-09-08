time_now_str = input("what is the time right now (in hrs)?")
waiting_time_str = input("what is the waiting time (in hrs)?")

hours = int(time_now_str) + int(waiting_time_str)

alarmtime = hours % 24
print(alarmtime)