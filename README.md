
# Sensor Data Modelling and Validation

## Overview
This project simulates time-dependent sensor data and applies validation, cleaning, and modelling techniques to reflect realistic experimental conditions.

## Methods
- Simulated sensor measurements with Gaussian noise
- Introduced missing values and outliers
- Data cleaning using interpolation and statistical outlier detection
- Rolling-window modelling for trend estimation
- Model evaluation using RMSE

## Results
The model achieved an RMSE of approximately 1.26, indicating good agreement with the underlying signal given the noise level.

## Limitations
- Simple rolling mean model
- Simulated data rather than experimental measurements
- No uncertainty propagation

## Future Improvements
- Compare multiple modelling approaches
- Apply to real experimental sensor data
- Extend to uncertainty quantification




