import numpy as np
import pandas as pd

headers = ["\mprotect","_llseek","clock_gettime","clone","close","dup","epoll_ctl","epoll_pwait","faccessat","fchmodat","fcntl64","fdatasync","fstat64","fstatat64","fsync","ftruncate64","futex",
"geteuid32","getpid","getrandom","getsockopt","gettimeofday","getuid32","ioctl","lseek","madvise","mmap2","mprotect","munmap","openat","prctl","pread64","process_vm_readv","pwrite64","read",
"readlinkat","recvfrom","renameat","rt_sigprocmask","rt_sigreturn","rt_sigsuspend",
"sched_yield","sendmsg","sendto","sigreturn","unlinkat","write","writev"]

def obtainLogInfo(textFile):
    AppLogs=[]

    with open(textFile) as f:
        f.seek(0)
        AppLogs=f.read()

    return AppLogs

def frequencyAnalysis(logs):

    frequency=np.ones((1,len(headers)))

    logLine = logs.split("\n")
    totalCount=0
    callCount = np.zeros(len(headers))
    for l in logLine:
        if "(" in l:
            totalCount+=1
            callCount[headers.index(l.split("(")[0])] += 1

    for i in range(len(headers)):
        frequency[0][i] = callCount[i] / totalCount

    return frequency[0]

if __name__ == "__main__":
    testLogs= obtainLogInfo("u")
    testFrequency = frequencyAnalysis(testLogs)
    print(testFrequency)
    '''
    outputCSV = pd.DataFrame(testFrequency)
    outputCSV.to_csv("output.csv", header=headers, index=True)
    '''
