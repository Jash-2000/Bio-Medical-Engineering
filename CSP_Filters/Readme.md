# Comman Spatial Pattern Filters

A dataset (35 secs data with sampling freq. 10Hz ) consisting of 5 electrode channels was extracted and subjected to data augmentations. Let there be two thought patterns - Thought 1 & Thought 2 which can be observed in the images mentioned below. The region of brain activation along with the affected electrodes has been depicted.

![Capture](https://user-images.githubusercontent.com/47540320/125205992-6f035200-e2a2-11eb-8315-8fc56b4ed4cb.PNG)

A CSP filter was developed to be applied above the covariance matrix (pre-processing) and subjected to a simple SVM. Even with very less data, we were able to get about 89% accuracy. As per defination, Common spatial pattern (CSP) is a mathematical procedure used in signal processing for separating a multivariate signal into additive subcomponents
which have maximum differences in variance between two windows. Simply speaking, these filters, when applied to the multi-electrode signal, we get a convoluted signal.

![Capture](https://user-images.githubusercontent.com/47540320/125206077-db7e5100-e2a2-11eb-9f53-e01b2cf42d51.PNG).
