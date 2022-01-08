<h2 align="center"><code>🏠 Structure Health Monitering 💻</code></h2>

<p align="center">
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/Architecture.jpg" 
         width="92%">
</p>

<p align="center">"<i>Look how I preprocess and analyze engineering data! </i>"</p>

<br>
<div align="center">
  <sub>Created by
  <a href="https://github.com/FelixLin99/">@Shuhui</a>
</div>

***
# Introduction
- Use Python to process and analyze the response of the bridge "浦仪夹江大桥" under typhoon condition. 
- Moniter the structure health by using visualization technique and time-frequency analysis.
<br>

# Requirements
- `Python` >= 3.7

<br>

# Structure
- [data](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/data)
    - [available](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/data/available):  Clean and integrated data can be directly used for visualization and analysis.
    - [preprocessed](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/data/preprocessed):  Preprocessed but not integrated data.
    <br>
    
- [preprocessing_pipeline](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline)
    <br>
    
- [timeFreq_analysis](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline)
    - [featureExtration.py](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline/featureExtration.py): TimeFrep analysis methods are encapsulated in this class
    - [utils.py](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline/utils.py): Class used to get data
    - [drowImages.ipynb](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline/drowImages.ipynb): An .ipynb file supported by featureExtration.py and  used to drow time-frequency images
    <br>
    
- [visualization](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/visualization)
    - [Visualization.py](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline/Visualization.py): Some visualizaiton methods are packaged in this class.
    - [Visualize&Correlation_Analysis.ipynb](https://github.com/FelixLin99/Structure-Health-Monitering/tree/main/preprocessing_pipeline/Visualize&Correlation_Analysis.ipynb): An .ipynb file supported by Visualization.py used to visualize data and do correlation analysis
    <br>

# Usage
To use time-frequency module, place the contents of this folder in your PYTHONPATH environment variable. 

- First, let's have a look at the time-frequency spectrum before typhoon, and we pay particular attention to the spectrum under 2Hz：
```python
import featureExtration
from visualization.Visualization import MidSpanData
import utils
    
midSpanData = MidSpanData(date='4.27')  # data = '4.27' or '5.4'
timePoint_1 = datetime.datetime(2021, 4, 28, 1, 0, 0) # select a timepoint before typhoon arrival
data_1 = utils.getWindowData(timePoint_1, '4.27', type='跨中横向加速度', duration=10).values
fs = 20
Freq, FFT_y1, Freq_le_2Hz, FFT_y1_le_2Hz_1 = featureExtration.featureExtration(data=data_1.reshape(-1), fs=fs).getFreqSpectrum()
```
<div align=center>
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/before_typhoon.jpg" height=300>
    </div> 
<br>
    
- Then, let's have a look at the time-frequency spectrum during typhoon 
```python
timePoint_2 = utils.getMaxWindSpedTime('4.27')
data_2 = utils.getWindowData(timePoint_2, '4.27', type='跨中横向加速度', duration=10).values
Freq, FFT_y1, Freq_le_2Hz, FFT_y1_le_2Hz_2 = featureExtration.featureExtration(data=data_2.reshape(-1), fs=fs).getFreqSpectrum()
```
<div align=center>
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/During_typhoon.jpg" height=300>
    </div> 
<br>
    
- We could also draw them in one pic:
<div align=center>
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/Comperation.jpg" height=300>
    </div> 
<br>
    <br>
    <br>
As for visualization module, there is a chinese tutorial in Visualize&Correlation_Analysis.ipynb for your reference. 
If you need an EN version, feel free to contact me.
    
- You could see how wind speed varies with time:
<div align=center>
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/visualization.jpg" height=300>
    </div> 
<br>
    
- Correlation analysis, like how wind speed influences std of acceleration:
<div align=center>
    <img src="https://github.com/FelixLin99/Structure-Health-Monitering/raw/main/tmp/img/correlation_analysis.jpg" height=300>
    </div> 
    
    
    
