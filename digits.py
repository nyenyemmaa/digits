# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause 

# import datasets, claussifiers and performance metriecs 
# form sklearn import datasets, svm, metrics

# To apply a calssifier on this data, we need to flatten the image, to 
# turn the data in a (samples, feature) matrix:
n_samples = len(digits, images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits 
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Now predict the value of the digit on the second hald:
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples 2:]
print("Classification report for classifier 
%s:\n"
    % (classifier metrics.
classification_report(expected. predicted)))
print("confusion matrix:\n%s" % metrics. confusion_metrix(expected, predicted))

