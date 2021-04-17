This repository is to show the use of autoencoders to detect anomaly in ECG signals.
An electrocardiogram (ECG or EKG) records the electrical signal from your heart to check for different heart conditions. Electrodes are placed on your chest to record your heart's electrical signals, which cause your heart to beat.

The dataset used is [ECG5000 dataset](http://www.timeseriesclassification.com/description.php?Dataset=ECG5000)

Autoencoders are a simple form of generative network and I have used them over here to reconstuct the ECG signal and find the anomolous signals if they have a large mae error.

---

| Normal ECG | Anamolous ECG|
|------------|--------------|
| ![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/NormalECG.png)         | ![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/AnomolousECG.png) |

---

## Reconstruction and error

![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/Reconstruction.png)

---

## ROC - AUC matrix

An ROC curve (receiver operating characteristic curve) is a graph showing the performance of a classification model at all classification thresholds. This curve plots two parameters 
  * True Positive Rate
  * False Positive Rate
  
  ![](https://developers.google.com/machine-learning/crash-course/images/AUC.svg)
  
  
