'''
1st kaj --> sort korbo,then oi sort er 1st index k output nibo...then 2nd theke last porjonto loop krbo, 
most recent tupple er last index er value nibo ..then oita k compare krbo jeta te achi oitar 1st er sathe ,jodi choto hoi tahole interval hoise,nahole output e push kore dibo tupple ta k...then return output.
'''
def mergeIntervals(intervals):
    intervals.sort(key=lambda i:i[0])
    output = [intervals[0]]
    
    for start,end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd,end)
        else:
            output.append([start,end])
    return output
    
   

print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
# output = [[1, 6], [8, 10], [15, 18]]
        
    
