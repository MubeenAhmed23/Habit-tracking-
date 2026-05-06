from datetime import timedelta


def is_next_period(d1, d2, periodicity):
    if periodicity == "daily":
        return d2 == d1 + timedelta(days=1)
    elif periodicity == "weekly":
        return d2 == d1 + timedelta(days=7)
    return False


def get_longest_streak(habit):
    logs = sorted([l.completed_at for l in habit.logs])
    if not logs:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(logs)):
        if is_next_period(logs[i - 1], logs[i], habit.periodicity):
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest


def get_current_streak(habit):
    logs = sorted([l.completed_at for l in habit.logs])
    if not logs:
        return 0

    current = 1

    for i in range(len(logs) - 1, 0, -1):
        if is_next_period(logs[i - 1], logs[i], habit.periodicity):
            current += 1
        else:
            break

    return current