from algorithms import fcfs, round_robin, sjf, ljf, priority_scheduling
from process import Process
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import random

processes = [
    Process(1, 0, 10, 7),
    Process(2, 1, 15, 6),
    Process(3, 2, 7, 8),
    Process(4, 3, 6, 3),
    Process(5, 4, 4, 5),
    Process(6, 5, 9, 8),
    Process(7, 6, 7, 6),
    Process(8, 7, 14, 4),
    Process(9, 8, 7, 9),
    Process(10, 9, 4, 5),
    Process(11, 10, 2, 9),
    Process(12, 11, 9, 9),
    Process(13, 12, 6, 4),
    Process(14, 13, 7, 1),
    Process(15, 14, 8, 1),
    Process(16, 15, 25, 9),
    Process(17, 16, 4, 5),
    Process(18, 17, 6, 3),
    Process(19, 18, 7, 2),
    Process(20, 19, 5, 7),
    Process(21, 20, 5, 16),
    Process(22, 21, 43, 10),
    Process(23, 22, 5, 1),
    Process(24, 23, 7, 8),
    Process(25, 24, 8, 8),
    Process(26, 25, 5, 5),
    Process(27, 26, 4, 7),
    Process(28, 27, 7, 3),
    Process(29, 28, 9, 2),
    Process(30, 29, 6, 7),

]

time_slice = 2

# FCFS
avg_waiting_time_fcfs, avg_turnaround_time_fcfs = fcfs(processes.copy())

# Round Robin
avg_waiting_time_rr, avg_turnaround_time_rr = round_robin(processes.copy(), time_slice)

# SJF
avg_waiting_time_sjf, avg_turnaround_time_sjf = sjf(processes.copy())

# LJF
avg_waiting_time_ljf, avg_turnaround_time_ljf = ljf(processes.copy())

# Priority Scheduling
avg_waiting_time_priority, avg_turnaround_time_priority = priority_scheduling(processes.copy())

# Create a new PrettyTable instance
table = PrettyTable()

# Define table headers
table.field_names = ["Algorithm", "Avg Waiting Time", "Avg Turnaround Time"]

# Add rows of data
table.add_row(["FCFS", avg_waiting_time_fcfs, avg_turnaround_time_fcfs])
table.add_row(["Round Robin", avg_waiting_time_rr, avg_turnaround_time_rr])
table.add_row(["SJF", avg_waiting_time_sjf, avg_turnaround_time_sjf])
table.add_row(["LJF", avg_waiting_time_ljf, avg_turnaround_time_ljf])
table.add_row(["Priority Scheduling", avg_waiting_time_priority, avg_turnaround_time_priority])

# Print the table
print(table)


# Algorithm names
algorithms = ["FCFS", "Round Robin", "SJF", "LJF", "Priority Scheduling"]

# Average waiting times
avg_waiting_times = [avg_waiting_time_fcfs, avg_waiting_time_rr, avg_waiting_time_sjf, avg_waiting_time_ljf, avg_waiting_time_priority]

# Average turnaround times
avg_turnaround_times = [avg_turnaround_time_fcfs, avg_turnaround_time_rr, avg_turnaround_time_sjf, avg_turnaround_time_ljf, avg_turnaround_time_priority]

# Create a bar plot for average waiting times
plt.figure(figsize=(10, 6))
plt.bar(algorithms, avg_waiting_times, color='skyblue')
plt.xlabel('Algorithm')
plt.ylabel('Average Waiting Time')
plt.title('Comparison of Average Waiting Time')
plt.ylim(0, max(avg_waiting_times) * 1.2)  # Set y-axis limit to add some padding
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

# Create a bar plot for average turnaround times
plt.figure(figsize=(10, 6))
plt.bar(algorithms, avg_turnaround_times, color='lightgreen')
plt.xlabel('Algorithm')
plt.ylabel('Average Turnaround Time')
plt.title('Comparison of Average Turnaround Time')
plt.ylim(0, max(avg_turnaround_times) * 1.2)  # Set y-axis limit to add some padding
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# Function to simulate transient events by randomly adding new processes
def simulate_transient_events(processes, num_events, max_burst_time, max_priority):
    max_arrival_time = max(process.arrival_time for process in processes)
    for _ in range(num_events):
        pid = len(processes) + 1
        arrival_time = random.randint(0, max_arrival_time + 5)
        burst_time = random.randint(1, max_burst_time)
        priority = random.randint(1, max_priority)
        new_process = Process(pid, arrival_time, burst_time, priority)
        processes.append(new_process)
    processes.sort(key=lambda x: x.arrival_time)

# Call simulate_transient_events function before running scheduling algorithms
num_transient_events = 5
max_transient_burst_time = 10
max_transient_priority = 15
simulate_transient_events(processes, num_transient_events, max_transient_burst_time, max_transient_priority)

# Run scheduling algorithms
avg_waiting_time_fcfs, avg_turnaround_time_fcfs = fcfs(processes.copy())
avg_waiting_time_rr, avg_turnaround_time_rr = round_robin(processes.copy(), time_slice)
avg_waiting_time_sjf, avg_turnaround_time_sjf = sjf(processes.copy())
avg_waiting_time_ljf, avg_turnaround_time_ljf = ljf(processes.copy())
avg_waiting_time_priority, avg_turnaround_time_priority = priority_scheduling(processes.copy())

# Create a new PrettyTable instance
table = PrettyTable()

table.title = "Comparison of Scheduling Algorithms with Transient Events"
# Define table headers
table.field_names = ["Algorithm", "Avg Waiting Time", "Avg Turnaround Time"]

# Add rows of data
table.add_row(["FCFS", avg_waiting_time_fcfs, avg_turnaround_time_fcfs])
table.add_row(["Round Robin", avg_waiting_time_rr, avg_turnaround_time_rr])
table.add_row(["SJF", avg_waiting_time_sjf, avg_turnaround_time_sjf])
table.add_row(["LJF", avg_waiting_time_ljf, avg_turnaround_time_ljf])
table.add_row(["Priority Scheduling", avg_waiting_time_priority, avg_turnaround_time_priority])

# Print the table
print(table)