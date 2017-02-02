import csv, sys, time, operator
from operator import itemgetter

def RoundRobin(processes, quantum):
	Scheduler = []
	calculation = [] #to calculate turnaround time and waiting time
	total_time = 0
	
	for process in processes:
		processID = process.pid
		ArrivTime = int(process.arrival_time)
		BurstTime = int(process.burst_time)
		total_time = total_time + BurstTime
		Scheduler.append([processID, ArrivTime, BurstTime, 0])
		calculation.append([ArrivTime, BurstTime])
			
	sys.stdout.write("Round Robin Process Gantt Chart")
	
	ptime = [] #processing time
	new_arrival_time = 0

	while total_time != 0:
		Scheduler = sorted(Scheduler, key = itemgetter(1,3))
		
		for x in Scheduler:
			if x[2] == 0: Scheduler.pop(Scheduler.index(x))
		
		process = Scheduler[0]
	
		if new_arrival_time != 0 and process[1] > new_arrival_time:
			ptime.append(["IDLE", (process[1] - new_arrival_time)])
			new_arrival_time = (process[1] - new_arrival_time) + new_arrival_time
		else:
			if process[2] > quantum:
				new_arrival_time = new_arrival_time + quantum #record the current process time
				ptime.append([process[0], quantum]) #process, processing time
				process[1] = new_arrival_time #update the current process's new arrival time
				process[2] -= quantum #update current process's burst time
				process[3] = 1 #mark current process as executed at least one time
				total_time -= quantum 		
			elif process[2] > 0 and process[2] <= quantum:	
				new_arrival_time = new_arrival_time + process[2]
				ptime.append([process[0], process[2], new_arrival_time]) #process, processing time, finish time
				total_time -= process[2] 
				process[2] = 0 #process finished executed	
			
	cumulative_ptime = [i[1] for i in ptime]
	
	for i in range(len(cumulative_ptime)):
		if i != 0: cumulative_ptime[i] = cumulative_ptime[i] + cumulative_ptime[i - 1]

	print "\n+" + "-----+" * len(cumulative_ptime) + "\n|",			
	for element in ptime: print str(element[0]).center(4, " ") + "|",	
	print "\n+" + "-----+" * len(cumulative_ptime) + "\n0",
	for element in cumulative_ptime: print "%5d" % element,
	
	finish_time = [x[2] for x in (sorted(x for x in ptime if len(x) == 3))]
	arrival_time = [x[0] for x in calculation]
	burst_time = [x[1] for x in calculation]
	turnaround_time = map(operator.sub, finish_time, arrival_time)
	waiting_time = map(operator.sub, turnaround_time, burst_time)
	
	print "\nTotal turnaround time: %d ms" % sum(turnaround_time)
	print "Total waiting time: %d ms" % sum(waiting_time)
	print "Average turnaround time: %.2f ms" % (float(sum(turnaround_time)) / float(len(turnaround_time)))
	print "Average waiting time: %.2f ms\n" % (float(sum(waiting_time)) / float(len(waiting_time)))
	
	
		