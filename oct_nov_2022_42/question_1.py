
#Question 1a: declare 2D array
job_array = [[]]
number_of_jobs = None

#Question 1b: create initialise()
def initialise():
    global job_array, number_of_jobs
    job_array = [[-1 for i in range(0,2)] for j in range(0, 100)]
    number_of_jobs = 0
    print(job_array)


#Question 1c: create add_job()
def add_job(job_number, priority):
    global job_array, number_of_jobs
    if number_of_jobs != len(job_array):
        job_array[number_of_jobs][0] = job_number
        job_array[number_of_jobs][1] = priority
        number_of_jobs += 1
        print("Added")
    else:
        print("Not Added")

#Question 1d: call the functions
initialise()
add_job(12, 10)
add_job(526, 9)
add_job(33, 8)
add_job(12, 9)
add_job(78, 1)

#Question 1e: insertion sort
def insertion_sort(job_array):
    for i in range(len(job_array)):
        while job_array[i-1][1] > job_array[i][1] and i > 0:
            job_array[i-1], job_array[i] = job_array[i], job_array[i-1]
            i -= 1
        
    print(job_array)

insertion_sort(job_array)

#Question 1f: print_array()
def print_array():
    for i in range(len(job_array)):
        if job_array[i][0] != -1:
            print(str(job_array[i][0]) + " priority " + str(job_array[i][1]))

print_array()
