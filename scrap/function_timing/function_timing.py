import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define your functions
def function1():
    time.sleep(1)  # Simulate some work
    pass

def function2():
    time.sleep(2)  # Simulate some work
    pass

# Measure execution time
start_time = time.time()

start_time_function1 = start_time
function1()
end_time_function1 = time.time()
execution_time_function1 = end_time_function1 - start_time_function1

start_time_function2 = end_time_function1
function2()
end_time_function2 = time.time()
execution_time_function2 = end_time_function2 - start_time_function2

# Create a figure and axis
fig, ax = plt.subplots()

# Define timeline parameters
timeline_increment = 0.1  # 0.1 second increment
total_execution_time = max(execution_time_function1, execution_time_function2)
timeline_seconds = [i * timeline_increment for i in range(int(total_execution_time / timeline_increment) + 1)]

# Function 1 timing rectangle
ax.barh(y=1, width=execution_time_function1, left=start_time_function1, color='blue', height=0.4, label="Function 1")

# Function 2 timing rectangle
ax.barh(y=2, width=execution_time_function2, left=start_time_function2, color='green', height=0.4, label="Function 2")

# Create a timeline
ax.set_yticks([])
ax.set_xlim(start_time, start_time + total_execution_time)
ax.xaxis.set_major_locator(mdates.MicrosecondLocator(interval=int(timeline_increment * 1e6)))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%S.%f"))
plt.xlabel("Timeline (seconds)")

# Add legend
plt.legend()

# Show the plot
plt.show()
