# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
    # standard loop with range
    # for i in range(0, len(list)):
    #     print list[i]

    # for each loop
    for item in list:
        print item

def print_scores(names, scores):
    for i in range(0, len(names)):
        print names[i] , " scored " , scores[i]

def average(scores):
        total = n
        for n in scores:
            total += n
        
        return total / len(scores)
        for n in scores:
            print "Average test score is" , scores[n]

def improved_average(scores):
    for n in scores:
        if n <= current_min:
            current_min = n

    for n in scores:
        if n <= current_min2:
            current_min2 = n
            
    sum_of_improved_average = 0
    for n in scores:
        sum_of_improved_average += n

    return sum_of_improved_scores / len(scores)
    for n in scores:
        print "Improved test score is" , improved_average
