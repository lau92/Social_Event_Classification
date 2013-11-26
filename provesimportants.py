import csv
with open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\sed2013_task2_dataset_train.csv', 'rb') as f:
    reader = csv.reader(f)
        for row in reader:
            print row