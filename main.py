# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    # print(n,m,data)

    threads = []
    thlens = []

    for i in range(n) :
        threads.append([])
        thlens.append(0)

    for i in range(m) :
        choice = thlens.index(min(thlens))
        thlens[choice] += data[i]
        output.append([choice, len(threads[choice])])
        for j in range(data[i]) :
            threads[choice].append(data[i])
            

    # print(threads)
    for i in output :
        print(i[0], i[1])
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    ###
    line1 = list(map(int, input().split()))
    n = line1[0]
    m = line1[1]
    data = list(map(int, input().split()))
    ###

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
