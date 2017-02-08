import csv
import numpy
#create test and training data

with open('spam.csv') as f:
    dataset=[tuple(line) for line in csv.reader(f)]
dataset = numpy.array(dataset)    

tokens = dataset
train_data = []
for item in tokens:
    train_data.append(item[1])
#print len(train_data)

tokens = dataset
train_label = []#spam or ham
for item in tokens:
    train_label.append(item[0])
#print len(train_label)

#print dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train_data, train_label, test_size=0.005, random_state=42)
#print len(x_train)
#print len(x_test)
#print len(y_train)
#print len(y_test)
#print x_test
#print y_test

new_x_train = [] 
for line in x_train:
    line = line.decode('utf-8','ignore').encode("utf-8")
    new_x_train.append(line)
#print new_x_train

new_x_test = [] 
for line in x_test:
    line = line.decode('utf-8','ignore').encode("utf-8")
    new_x_test.append(line)
#print new_x_test

#tokenizing
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(stop_words = 'english')
x_train_count = count_vectorizer.fit_transform(new_x_train)
#print x_train_count
#print x_train_count.shape
x_test_count = count_vectorizer.transform(new_x_test)

#Predict class of Test data set
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(x_train_count, y_train)
predicted = clf.predict(x_test_count)
#print predicted
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,predicted)
#print accuracy