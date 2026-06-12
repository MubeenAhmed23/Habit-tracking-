from datetime import timedelta



def longest_streak(habit):

    logs=sorted(
        [x.completed_at for x in habit.logs]
    )


    if not logs:
        return 0


    longest=1
    current=1


    for i in range(1,len(logs)):

        if logs[i]==logs[i-1]+timedelta(days=1):

            current+=1

            longest=max(
                longest,
                current
            )

        else:

            current=1



    return longest




def current_streak(habit):

    return longest_streak(habit)