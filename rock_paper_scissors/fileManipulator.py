import csv


def checkUser(userName):
    """Check if user is already existing or not"""
    with open("rating.csv", 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line.__contains__(userName):
                scores = int(line[1])
                return int(line[1])

    with open("rating.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([userName, 0])
        # self.scores = 0
        return 0

def addScore(score, userName):
    """Adds score to user"""
    with open('rating.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('rating.csv', mode='w+', newline='\n') as file:
        writer = csv.writer(file)
        for i, row in enumerate(rows):
            if len(row) > 0 and row[0].__contains__(userName):
                rows[i][1] = int(rows[i][1]) + score

        writer.writerows(rows)