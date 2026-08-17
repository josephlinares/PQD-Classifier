# Experimentation results

|    | Metric      |   Value |
|---:|:------------|--------:|
|  0 | Accuracy    |    0.86 |
|  1 | Macro F1    |    0.85 |
|  2 | Weighted F1 |    0.85 | 

|                        |   precision |   recall |   f1-score |   support |
|:-----------------------|------------:|---------:|-----------:|----------:|
| Flicker                |        0.98 |     0.98 |       0.98 |       213 |
| Flicker+Harmonics      |        1    |     1    |       1    |       212 |
| Flicker+Sag            |        1    |     0.98 |       0.99 |       212 |
| Flicker+Swell          |        1    |     1    |       1    |       213 |
| Harmonics              |        0.98 |     1    |       0.99 |       212 |
| Impulsive Transient    |        1    |     0.96 |       0.98 |       213 |
| Interruption           |        0.5  |     0.32 |       0.39 |       212 |
| Interruption+Harmonics |        0.47 |     0.5  |       0.49 |       212 |
| Normal                 |        0.87 |     1    |       0.93 |       213 |
| Notch                  |        1    |     0.95 |       0.97 |       213 |
| Oscillatory transient  |        1    |     0.99 |       1    |       212 |
| Sag                    |        0.5  |     0.66 |       0.57 |       213 |
| Sag+Harmonics          |        0.47 |     0.42 |       0.44 |       213 |
| Spike                  |        1    |     0.96 |       0.98 |       213 |
| Swell                  |        0.99 |     1    |       0.99 |       212 |
| Swell+Harmonics        |        1    |     0.99 |       1    |       212 |
| micro avg              |        0.86 |     0.86 |       0.86 |      3400 |
| macro avg              |        0.86 |     0.86 |       0.85 |      3400 |
| weighted avg           |        0.86 |     0.86 |       0.85 |      3400 |
| samples avg            |        0.86 |     0.86 |       0.86 |      3400 | 

![Confusion Matrix](<confusion matrix.png>)

# Annotations

