"""
Chapter 4.1 Performance

    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) == 0:
                count += 1

        the above is logorithmic or n^2 in speed at 8 seconds it 10000 and 80000 at 1000000
            or a doubly nested loop
Constants are irrelevant and can become n times faster

        N is the only value we care about the constant
        Counting the steps in the above is 1+n*n+1+1=n^2

ANYTHING THAT IS QUADRATIC n^2 is not scalable
"""

"""
Big O Notation Time Complexity
    O(n) is constant scalability or middle diagonal in graph like constant function
        same with other mathmatical functions O(log n) is below constant
            constant is constant
        O(n^2) is above O(n) and so on
Anything slower that O(n) is not scalable
"""
"""
can have multiple for i in range(n) 
    in different funtion
"""
"""
can trade time for space or space for time
    increasing or decreasing memory to increase or decrease time for completion
            (RAM Memory for cached money memory)
                trade time to reduce RAM space
"""