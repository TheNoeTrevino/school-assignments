<h1 align='center'>
Assignment 1
</h1>

## Question 1: Supervised vs Unsupervised Learning

### Overall Difference

The main difference between supervised learning and unsupervised learning is
that supervised learning uses labeled data, and unsupervised learning
uses Unlabeled data

_But what does that even mean? What are the implications of this?_

#### Supervised Learning

---

_Labeled are of course labeled._

For example, a real world example of this would be finding the relationship
between independent and dependent variables. The labeled input and output
lets the model learn the relationship overtime. The algorithm will 'learn', in
more understandable terms: adjust, overtime to fit the dataset that it is being
shown.

This approach to machine learning requires human intervention to label the data.
Typically, this style is more accurate, compared to its unsupervised counterpart.

This technique is used to make _predictions_, where as unsupervised is not used
for this, it is used to cluster data and detect anomalies. More this this below

#### Unsupervised Learning

---

_Unsupervised learning does not use labeled data._

This technique looks for pattern in the data and groups it.
An example of this would be the k-means clustering algorithms.
It does not necessarily classify the data,
but it can detect patterns and set boundaries in the data based on patterns and
similarities in the data.

##### Summary and Comparison

You would use supervised learning to classify data, and unsupervised learning
to put data into groups.

Let us pretend we had two almost identical datasets. Both have the exact same
images of apples and oranges.

If the data was classified, we would be able
to have a model determine weather the photo was an apple or an orange over time
with a supervised learning model.

If the data was _not_ classified, we would take a unsupervised learning approach.
This would result in the model being able to group the data into red and small,
based on the color values, and size of the object compared to the frame of the
photo overtime. Cluster 1 would have the data samples that had high red values,
and cluster two would have the data samples with high 'orange' values,
whatever that may be in hex code

## Question 2: Classification vs Regression

---

These two are branches of supervised learning.

Regression models deal with quantitative values,
classification models deal with qualitative values.

Regression models can predict the outcome based on the line they set that
is based on the line of best fit.

Classification models will, of course, classify something.

Notice the difference between classification and regression in terms of
terminology.

Regression puts a numerical value on an input, and classification does not.
Classification puts inputs into categories. For example, an input of a credit
score is given. We see the value to 200. The classification model will
categorize this into the 'bad' category. Well, what can the linear regression
model do instead? It can receive the input of the credit score, and output
a numerical value. In this case, the salary of the subject!

<sub> Sources:

<sub> [supervised vs unsupervised learning article](https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning)

<sub> [youtube video](https://www.youtube.com/watch?v=W01tIRP_Rqs&ab_channel=IBMTechnology)
