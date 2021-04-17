# Control of a simplee robot using Brainwave - EEG signals

This repository contins my keras implementation of signal analysis of EEG waves for control a simple differential drive robot. 
An electroencephalogram (EEG) is a test that detects electrical activity in your brain using small, metal discs (electrodes) attached to your scalp. Your brain cells communicate via electrical impulses and are active all the time, even when you're asleep.

---

## Data

The data is present in "Data.mat" which contains 4 other files. If opened with spicy, it will contain 4 other dictionaries and the data would be present in **S1_nolabel6** dictionary. The following commands would be useful while extracting data:

```python
     import spicy.io as sc
     feature = sc.loadmat("C:/Users/Jash Shah/Desktop/data.mat") # Dictionary named loader created. 
     loader = feature['S1_nolabel6']            # Converted to numpy array
```

It contains 29738 rows, with per row is one EEG sample has 65 elements. The first 64 elements are the 64 channels EEG raw data collected by BCI2000 system, and the last element is the label of the sample in this row.  The EEG database comes from an open database eegmmidb, see the details [here](http://www.physionet.org/pn4/eegmmidb/).

The following table briefs about the labels used :

|   Action   | Label |
| ---------- | ----- |
| Eye Closed |   1   |
| Left Fist  |   2   |
| Right Fist |   3   |
| Both Fist  |   4   |
| Both Feet  |   5   |

---

## Description of files





---

A lot of motivation was taken from the following source but I have not copied their model. Their model has also been implemented and added in the repository seperately.

```
Xiang Zhang, Lina Yao, Chaoran Huang, QuanZheng Sheng and Xianzhi Wang. Intent Recognition in Smart Living Through Deep Recurrent Neural Networks. The 24th International Conference On Neural Information Processing (ICONIP 2017). Guangzhou, China, Nov 14 - Nov 18, 2017.
```

---

## Tasks remaining

     1. Converting the model to an edge AI architecture using TinyML.
     2. Developing the Hardware.
