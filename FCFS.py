from Process import Process

def FCFS(num_of_processes, processes):
	print "~~~ First Come First Serve-based Preemptive Priority scheduling ~~~"

	# For gantt chart
	pnames = [] 
	ptimes = []
	
	# Burst time
	temp_burst_time = [process.burst_time for process in processes]
	total_burst_time = sum(temp_burst_time)
	
	# Statistics
	total_turnaround_time = 0
	total_waiting_time = 0
	
	# Initialise timer
	current_time = 0 
	
	# IDLE
	IDLE = False
	
	# Loop if process haven't finish executing
	while total_burst_time != 0:
		# Store processes that have arrived and haven't finish executing
		arrived_processes = []
		for i in xrange(num_of_processes):
			if processes[i].arrival_time <= current_time and temp_burst_time[i] != 0:
				arrived_processes.append(i)
		
		# No process arrive, thus no process executes
		if len(arrived_processes) == 0:
			if not IDLE:
				IDLE = True
				pnames.append("IDLE")
				ptimes.append(current_time)
		else:
			if IDLE:
				IDLE = False
				
			# Find index of arrived process with the least priority
			index_min_priority = arrived_processes[0]
			for arrived in arrived_processes:
				if processes[arrived].priority < processes[index_min_priority].priority:
					index_min_priority = arrived
				# If both have the same priority, choose the one arrive earlier
				elif processes[arrived].priority == processes[index_min_priority].priority:
					if processes[arrived].arrival_time < processes[index_min_priority].arrival_time:
						index_min_priority = arrived
		
			# Update burst time
			temp_burst_time[index_min_priority] -= 1
			
			# Process finish executing
			# Update total burst time, total turnaround time and total waiting time
			if temp_burst_time[index_min_priority] == 0:
				total_burst_time -= processes[index_min_priority].burst_time
				finish_time = current_time + 1
				turnaround_time = finish_time - processes[index_min_priority].arrival_time
				waiting_time = turnaround_time - processes[index_min_priority].burst_time
				total_turnaround_time += turnaround_time
				total_waiting_time += waiting_time
			
			# For gantt chart, store process id and start time 
			# if current time is 0 or previous process id is different from current process id
			if current_time == 0 or pnames[-1] != processes[index_min_priority].pid:
				pnames.append(processes[index_min_priority].pid)
				ptimes.append(current_time)
		
		# Update timer
		current_time += 1
	
	# For gantt chart, store end time
	ptimes.append(current_time)
	
	# Print gantt chart
	print "Gantt chart:"
	print "+------" * len(pnames) + "+"
	for pname in pnames:
		print "|" + pname.center(5, " "),
	print "|"
	print "+------" * len(pnames) + "+"
	print ptimes[0],
	for index in xrange(len(ptimes)-1):
		print "%6d" % ptimes[index+1],
	print
	
	# Print statistics about algorithm
	print "Total turnaround time: %d ms" % total_turnaround_time
	print "Total waiting time: %d ms" % total_waiting_time
	print "Average turnaround time: %.2f ms" % (float(total_turnaround_time) / float(num_of_processes))
	print "Average waiting time: %.2f ms\n" % (float(total_waiting_time) / float(num_of_processes))