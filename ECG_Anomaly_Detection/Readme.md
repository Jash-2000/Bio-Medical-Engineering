This repository is to show the use of autoencoders to detect anomaly in ECG signals. 

The dataset used is [ECG5000 dataset](http://www.timeseriesclassification.com/description.php?Dataset=ECG5000)

Autoencoders are a simple form of generative network and I have used them over here to reconstuct the ECG signal and find the anomolous signals if they have a large mae error.

---

| Normal ECG | Anamolous ECG|
|------------|--------------|
| ![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/NormalECG.png)         | ![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/AnomolousECG.png) |

---

## Reconstruction and error

![](https://github.com/Jash-2000/Bio-Medical-Engineering/blob/main/ECG_Anomaly_Detection/Reconstruction.png)
