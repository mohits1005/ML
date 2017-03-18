import csv
import numpy

with open('chalk_test4.csv') as f:
    csdataset=[tuple(line) for line in csv.reader(f)]
csdataset = numpy.array(csdataset)

tokens = csdataset
test_data = []
for item in tokens:
    test_data.append(item[3]) 
#print test_data

tokens = csdataset
test_label = []#spam or ham
for item in tokens:
    if item[6] > '2' :
    	test_label.append('good')
    else :
    	test_label.append('bad')	
#print test_label    

with open('spam.csv') as f:
    dataset=[tuple(line) for line in csv.reader(f)]
dataset = numpy.array(dataset)    
#print(dataset)

tokens = dataset
train_data = []
for item in tokens:
    train_data.append(item[1])
#print len(train_data)

tokens = dataset
train_label = []#spam or ham
for item in tokens:
    train_label.append(item[0])

x_train = train_data
x_test = test_data
y_train = train_label
y_test = test_label    

print len(x_train)
print len(x_test)
print len(y_train)
print len(y_test)

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
import sys
from time import time
t0 = time()
#Training classifier
clf = MultinomialNB().fit(x_train_count, y_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
predicted = clf.predict(x_test_count)
print "predicting time:", round(time()-t1, 3), "s"
#print predicted
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,predicted)
print accuracy