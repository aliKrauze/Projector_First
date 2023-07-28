import pandas as pd
import csv


def copy_file():
    with open('user_score_file.csv', mode='r') as old_file:
        reader_file = csv.reader(old_file)

        with open('new_user_score_file.csv', mode='w', newline='') as new_file:
            writer_file = csv.writer(new_file)

            for data in reader_file:
                writer_file.writerow(data)

    csvData = pd.read_csv("new_user_score_file.csv")
    csvData.sort_values(csvData.columns[1], axis=0, inplace=True)

    csvData.to_csv("new_user_score_file.csv", index=False)


if __name__ == "__main__":
    copy_file()
