"""Importing csv module"""
import csv


def check_user(user_name):
    """Check if user is already existing or not
    user_name = Username, type -- String
    """
    with open("rating.csv", 'r', encoding="UTF-8") as file:
        reader = csv.reader(file)
        for line in reader:
            if line.__contains__(user_name):
                scores = int(line[1])
                return scores

    with open("rating.csv", "a", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow([user_name, 0])
        # self.scores = 0
        return 0


def add_score(score, user_name):
    """Adds score to user
    score = Score that we need to add into rating.csv, type -- Integer
    user_name = Username, type -- String
    """
    with open('rating.csv', mode='r', newline='', encoding="UTF-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('rating.csv', mode='w+', newline='\n', encoding="UTF-8") as file:
        writer = csv.writer(file)
        for i, row in enumerate(rows):
            if len(row) > 0 and row[0].__contains__(user_name):
                rows[i][1] = int(rows[i][1]) + score

        writer.writerows(rows)
