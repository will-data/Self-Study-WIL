# My First Solution without using heapq
def solution(jobs):
    done = 0;
    nJobs = len(jobs);
    nInjobs = 0
    jobStack = sorted(jobs, key=lambda k: k[0], reverse=True)
    inStack = [];
    working = False
    wtime = 0;
    now = 0;
    job = jobStack.pop();

    while done < nJobs:
        if jobStack:
            jobTemp = []
            while jobStack and job[0] <= now:
                jobTemp.append(job);
                nInjobs += 1
                job = jobStack.pop()
            if job[0] <= now:
                jobTemp.append(job);
                nInjobs += 1
            if jobTemp:
                inStack += jobTemp
                inStack.sort(key=lambda k: (k[1], k[0]), reverse=True)
        elif nInjobs != nJobs and job[0] <= now:
            inStack.append(job);
            nInjobs += 1
            inStack.sort(key=lambda k: (k[1], k[0]), reverse=True)

        if inStack:
            working = inStack.pop()
            now += working[1];
            done += 1;
            wtime += (now - working[0])
        else:
            now = job[0]

    return wtime // nJobs


# Another solution using heapq
import heapq

def solution(jobs):
    done = 0;
    nJobs = len(jobs);
    nInjobs = 0
    jobStack = sorted(jobs, key=lambda k: k[0], reverse=True)
    inStack = [];
    working = False
    wtime = 0;
    now = 0;
    job = jobStack.pop();

    while done < nJobs:
        if jobStack:
            while jobStack and job[0] <= now:
                wtime += now - job[0];
                nInjobs += 1
                heapq.heappush(inStack, (job[1]));
                job = jobStack.pop()
            if job[0] <= now:
                wtime += now - job[0];
                nInjobs += 1
                heapq.heappush(inStack, (job[1]));
        elif nInjobs != nJobs and job[0] <= now:
            wtime += now - job[0];
            nInjobs += 1
            heapq.heappush(inStack, (job[1]));

        if inStack:
            working = heapq.heappop(inStack)
            now += working;
            done += 1;
            wtime += working * (len(inStack) + 1)
        else:
            now = job[0]

    return wtime // nJobs