# Experimentation results

|    | Metric      |   Value |
|---:|:------------|--------:|
|  0 | Accuracy    |    0.86 |
|  1 | Macro F1    |    0.83 |
|  2 | Weighted F1 |    0.83 | 

|                        |   precision |   recall |   f1-score |   support |
|:-----------------------|------------:|---------:|-----------:|----------:|
| Flicker                |        0.98 |     0.99 |       0.98 |    213    |
| Flicker+Harmonics      |        1    |     1    |       1    |    212    |
| Flicker+Sag            |        1    |     0.99 |       0.99 |    212    |
| Flicker+Swell          |        1    |     0.99 |       0.99 |    213    |
| Harmonics              |        0.98 |     1    |       0.99 |    212    |
| Impulsive Transient    |        0.97 |     0.96 |       0.96 |    213    |
| Interruption           |        0.49 |     0.9  |       0.63 |    212    |
| Interruption+Harmonics |        0.43 |     0.17 |       0.24 |    212    |
| Normal                 |        0.87 |     0.98 |       0.92 |    213    |
| Notch                  |        1    |     0.95 |       0.97 |    213    |
| Oscillatory transient  |        1    |     0.99 |       1    |    212    |
| Sag                    |        0.43 |     0.06 |       0.11 |    213    |
| Sag+Harmonics          |        0.49 |     0.78 |       0.6  |    213    |
| Spike                  |        1    |     0.96 |       0.98 |    213    |
| Swell                  |        0.99 |     1    |       0.99 |    212    |
| Swell+Harmonics        |        1    |     0.99 |       0.99 |    212    |
| accuracy               |        0.86 |     0.86 |       0.86 |      0.86 |
| macro avg              |        0.85 |     0.86 |       0.83 |   3400    |
| weighted avg           |        0.85 |     0.86 |       0.83 |   3400    | 

![Confusion Matrix](<confusion matrix.png>)

# Annotations

