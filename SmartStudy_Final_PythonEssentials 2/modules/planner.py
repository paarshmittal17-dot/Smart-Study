DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def allocate_hours(analysis, available_hours):
    weights = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    if not analysis:
        return []
    total_weight = sum(weights[x["priority"]] for x in analysis)
    return [
        {
            "subject": x["name"],
            "priority": x["priority"],
            "hours": round(weights[x["priority"]] / total_weight * available_hours, 1)
        }
        for x in analysis
    ]

def generate_daily_plan(analysis, available_hours):
    allocations = allocate_hours(analysis, available_hours)
    schedule = {day: [] for day in DAYS}

    # Spread each subject's weekly allocation across different days.
    day_index = 0
    for item in allocations:
        remaining = item["hours"]
        chunks = []
        while remaining > 0:
            chunk = min(1.0, remaining)
            chunks.append(round(chunk, 1))
            remaining = round(remaining - chunk, 1)

        for chunk in chunks:
            day = DAYS[day_index % len(DAYS)]
            schedule[day].append({
                "subject": item["subject"],
                "hours": chunk
            })
            day_index += 1

    return schedule
