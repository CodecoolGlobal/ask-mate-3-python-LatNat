import csv
import os

DATA_FILE_PATH_ANSWER = os.getenv('DATA_FILE_PATH_ANSWER') if 'DATA_FILE_PATH_ANSWER' in os.environ else 'answer.csv'
DATA_FILE_PATH_QUESTION = os.getenv('DATA_FILE_PATH_QUESTION') if 'DATA_FILE_PATH_QUESTION' in os.environ else 'question.csv'
DATA_HEADER_ANSWER = ["id","submission_time","vote_number","question_id","message","image"]
DATA_HEADER_QUESTION = ["id","submission_time","view_number","vote_number","title","message","image"]


def data_import(file_name):
    with open(file_name) as file:
        lines = csv.DictReader(file)
        data = [x for x in lines]
    return data


def data_export(filename, dict_data, header):
    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)


if __name__ == "__main__":
    pass