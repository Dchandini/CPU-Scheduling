from algorithms import fcfs, round_robin, sjf, ljf, priority_scheduling
from process import Process
from prettytable import PrettyTable
import matplotlib.pyplot as plt

processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8),
    Process(4, 3, 6),
    Process(5, 4, 2)
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

