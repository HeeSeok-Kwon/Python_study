import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8", newline="")
    # print(file)
    writer = csv.writer(file)
    writer.writerow(["title","company","location","link"])
    # print(jobs)
    for job in jobs:
        # print(job.values())
        writer.writerow(list(job.values()))
    return