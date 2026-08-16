# Experimentation results

|    | Metric      |   Value |
|---:|:------------|--------:|
|  0 | Accuracy    |     0.8 |
|  1 | Macro F1    |     0.8 |
|  2 | Weighted F1 |     0.8 | 

|                        |   precision |   recall |   f1-score |   support |
|:-----------------------|------------:|---------:|-----------:|----------:|
| Flicker                |        0.94 |     0.65 |       0.77 |        48 |
| Flicker+Harmonics      |        1    |     1    |       1    |        48 |
| Flicker+Sag            |        0.96 |     0.94 |       0.95 |        48 |
| Flicker+Swell          |        0.73 |     0.98 |       0.84 |        48 |
| Harmonics              |        0.92 |     1    |       0.96 |        48 |
| Impulsive Transient    |        1    |     0.69 |       0.81 |        48 |
| Interruption           |        0.52 |     0.5  |       0.51 |        48 |
| Interruption+Harmonics |        0.44 |     0.48 |       0.46 |        48 |
| Normal                 |        0.83 |     1    |       0.91 |        48 |
| Notch                  |        0.98 |     0.98 |       0.98 |        48 |
| Oscillatory transient  |        1    |     0.92 |       0.96 |        48 |
| Sag                    |        0.49 |     0.35 |       0.41 |        48 |
| Sag+Harmonics          |        0.5  |     0.35 |       0.41 |        48 |
| Spike                  |        0.92 |     0.94 |       0.93 |        48 |
| Swell                  |        0.81 |     1    |       0.9  |        48 |
| Swell+Harmonics        |        1    |     0.96 |       0.98 |        48 |
| micro avg              |        0.82 |     0.8  |       0.81 |       768 |
| macro avg              |        0.82 |     0.8  |       0.8  |       768 |
| weighted avg           |        0.82 |     0.8  |       0.8  |       768 |
| samples avg            |        0.8  |     0.8  |       0.8  |       768 | 

# Annotations

Created from '06 Log Evaluation'
Loaded model weights from run_08_15-13_56/model.weights.h5 \
Then tested a new evalueate script for README generation and output metrics
