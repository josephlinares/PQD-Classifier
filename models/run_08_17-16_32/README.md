# Experimentation results

|    | Metric      |   Value |
|---:|:------------|--------:|
|  0 | Accuracy    |    0.98 |
|  1 | Macro F1    |    0.98 |
|  2 | Weighted F1 |    0.98 | 

|                       |   precision |   recall |   f1-score |   support |
|:----------------------|------------:|---------:|-----------:|----------:|
| Flicker               |        0.97 |     1    |       0.98 |       200 |
| Flicker+Harmonics     |        1    |     1    |       1    |       200 |
| Flicker+Sag           |        0.99 |     0.96 |       0.98 |       200 |
| Flicker+Swell         |        1    |     1    |       1    |       200 |
| Harmonics             |        1    |     0.9  |       0.95 |       200 |
| Impulsive Transient   |        0.94 |     0.98 |       0.96 |       200 |
| Normal                |        0.97 |     1    |       0.99 |       200 |
| Notch                 |        0.98 |     0.94 |       0.96 |       200 |
| Oscillatory transient |        1    |     1    |       1    |       200 |
| Sag                   |        1    |     1    |       1    |       200 |
| Sag+Harmonics         |        1    |     1    |       1    |       200 |
| Spike                 |        1    |     0.98 |       0.99 |       200 |
| Swell                 |        1    |     1    |       1    |       200 |
| Swell+Harmonics       |        0.91 |     1    |       0.95 |       200 |
| micro avg             |        0.98 |     0.98 |       0.98 |      2800 |
| macro avg             |        0.98 |     0.98 |       0.98 |      2800 |
| weighted avg          |        0.98 |     0.98 |       0.98 |      2800 |
| samples avg           |        0.98 |     0.98 |       0.98 |      2800 | 

![Confusion Matrix](<confusion matrix.png>)

# Annotations

