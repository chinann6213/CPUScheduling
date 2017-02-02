import sys,csv
import copy

from Process import Process
from SRTN import SRTN
from FCFS import FCFS
from RRscheduling import RoundRobin

def getInput(input, processes):
	print "Enter number of processes (Range from 3-10):",
	num_of_processes = int(raw_input())
	while num_of_processes < 3 or num_of_processes > 10:
		print "Number of processes is out of range. Please enter again:",
		num_of_processes = int(raw_input())
	input.append(num_of_processes)
	for i in xrange(num_of_processes):
		pid = raw_input("Enter process name: ")
		arrival_time = int(raw_input("Enter arrival time: "))
		burst_time = int(raw_input("Enter burst time: "))	
		priority = int(raw_input("Enter priority (Range from 1-6): "))
		while priority < 1 or priority > 6:
			priority = int(raw_input("Priority is out of range. Please enter again: "))
		processes.append(Process(pid, arrival_time, burst_time, priority))
	quantum = int(raw_input("Enter quantum: "))
	input.append(quantum)
	print
	
def readFile(filename, input, processes):
	with open(filename, "r") as input_file: 
		next(input_file)	
		input_file = csv.reader(input_file, delimiter = ",", quotechar = "|")
		for i, l in enumerate(input_file): 
			processes.append(Process(l[0], int(l[1]), int(l[2]), int(l[3])))
			pass
		input.append(i + 1)

	
def main():
	input = [] 
	processes = []
	
	# Use given text file
	if len(sys.argv) == 2:
		quantum = int(raw_input("Enter quantum: "))
		readFile(sys.argv[1], input, processes)
	# Manual input
	else:
		getInput(input, processes)
	
	num_of_processes = input[0]
	for i in processes:
		print i.pid
		
	FCFS(num_of_processes, copy.deepcopy(processes))
	SRTN(num_of_processes, copy.deepcopy(processes))
	RoundRobin(copy.deepcopy(processes), quantum)
	
main()