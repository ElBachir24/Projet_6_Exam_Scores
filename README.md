# Project 6: Exam Scores of a Class

## Description
This project is a Python-based data analysis tool created collaboratively by a team of 5 students. It processes and compares academic examination scores from two distinct groups (`Class A` and `Class B`), each consisting of 20 students. All calculations are built from scratch using pure Python control structures and data types, without importing external statistical modules.

## Team Members
- **Leader / Member 5**: Diouf Mouhamed El Bachir
- **Member 1**: Ousseynou Sow
- **Member 2**: MINGANE GRACIA
- **Member 3**: Dlamini Sandziso Siyabonga
- **Member 4**: Nusaiba Alrasheed Osman Alfaki

## Features
- **Core Statistics**: Custom calculation of `mean`, `median`, `mode`, and `standard deviation`.
- **Outlier Detection**: Automated identification of anomalous scores defined by $|x - \mu| > 2\sigma$.
- **Class Comparison**: Evaluation of performance levels and score dispersion across groups.
- **Grade Distribution**: Visual representation of grade breakdown using star histograms.



## Statistical Analysis & Answers

### 1. Impact of Outliers (Class A: Mean vs. Median)
- **With Outlier (95)**: Mean = `63.35` | Median = `62.50`
- **Without Outlier (95)**: Mean = `61.68` | Median = `62.00`

**Explanation**: 
When the outlier (`95`) is removed, **the mean changes much more significantly than the median**. 
- The **mean** sums all scores and divides by the total count; therefore, an extreme value pulls the sum upwards.
- The **median** depends only on the middle position of the sorted list, making it robust and resilient against extreme values.

### 2. Class Comparison (Class A vs. Class B)
- **Class A**: Higher average ($\approx 63.35$), but significantly wider score variability ($\sigma \approx 10.13$).
- **Class B**: Slightly lower average ($\approx 60.10$), but extremely consistent scores clustered closely around 60 ($\sigma \approx 1.22$).
