<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/joelcalm/Formula1Prediction](https://github.com/joelcalm/Formula1Prediction)">
    <img src="f1logo.png" alt="Logo" width="80" height="80">
  </a>  

  <h3 align="center">Formula1 Outcome Prediction</h3>

  <p align="center">
    This project showcases the implementation and evaluation of machine learning algorithms, including XGBoost, Random Forest, SVM, and Logistic Regression, for predicting Formula 1 race outcomes, such as race winners and finishing groups (podium, points, no-points), using data from the 2020–2024 Formula 1 seasons.
    <br />
    <a href="https://github.com/joelcalm/Formula1Prediction"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/joelcalm/Formula1Prediction">View</a>
    ·
    <a href="https://github.com/joelcalm/Formula1Prediction/issues">Report Bug</a>
    ·
    <a href="https://github.com/joelcalm/Formula1Prediction/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#approach-and-methodology">Approach and Methodology</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#data-sources">Data Sources</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#results-and-performance">Results and Performance</a></li>
    <li><a href="#betting-analysis">Betting Analysis</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About The Project

This repository contains code and analysis for predicting Formula 1 race outcomes. The project’s core objective is to forecast the race winner and classify drivers into three performance groups—podium (top 3), points (4–10), and no-points (>10)—across multiple seasons (2020–2024).

The prediction tasks face unique constraints, such as only one winner per race and limited podium spots, making conventional metrics insufficient. Custom evaluation strategies were developed, including "race-wise accuracy," to ensure predictions adhere to real-world constraints. The project also explored the potential of regression-based approaches (predicting continuous finishing positions) and converting those predictions into groups.

### Approach and Methodology

- **Data Integration:** Historical data from Kaggle’s Formula 1 dataset (1950–2020) complemented with additional scraped data from the Ergast API for 2021–2024 seasons.
- **Feature Engineering:** Incorporation of driver age, DNF rates, constructor reliability, home-race flags, and recent performance metrics to capture nuanced factors impacting results.
- **Modeling:** Evaluation of multiple models including Logistic Regression, Random Forest, SVM, and XGBoost. Both classification and regression strategies were employed.
- **Metrics:** Custom race-wise accuracy for winner prediction, group accuracy, F1 scores, and ROC/AUC for assessing classification of podium, points, and no-points groups.
- **Temporal Cross-Validation:** TimeSeriesSplit was used to ensure future races are predicted using only historical data.

This workflow led to significant improvements in accuracy after feature engineering, hyperparameter tuning, and feature selection. XGBoost emerged as the top performer for both winner and group predictions.

### Built With

* [Scikit-Learn](https://scikit-learn.org/)
* [XGBoost](https://xgboost.readthedocs.io/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)


## Getting Started

### Data Sources

- **Kaggle F1 Dataset (1950–2020)**  
  Used as the base historical dataset containing race results, drivers, constructors, and qualifying sessions.

- **Ergast API (2021–2024)**  
  Additional data was scraped to update the dataset and include recent races up to 2024.


### Installation


First, clone the repository:
   ```sh
   git clone https://github.com/joelcalm/Formula1Prediction.git
   ```
Access to the project folder with:
  ```sh
  cd Formula1Prediction
  ```

We will create a virtual environment with `python3`
* Create environment with python 3 
    ```sh
    python3 -m venv venv
    ```
    
* Enable the virtual environment
    ```sh
    source venv/bin/activate
    ```

* Install the python dependencies on the virtual environment
    ```sh
    pip install -r requirements.txt
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
Preprocessing & Feature Engineering Scripts:
Scripts to merge datasets, clean missing values, and engineer additional features.

Model Training:
Jupyter notebooks or Python scripts for training models (Logistic Regression, Random Forest, SVM, XGBoost) on the prepared dataset.

Evaluation & Visualization:
Scripts and notebooks to evaluate the models using race-wise accuracy, group accuracy, and F1 scores. Visualizations (correlation matrices, ROC curves, confusion matrices) help interpret model performance.

Betting Analysis (Optional):
A separate module to simulate a betting strategy using predicted winners and compare returns to actual outcomes and odds.

Results and Performance
After feature engineering and hyperparameter tuning:

Winner Prediction: XGBoost improved race-wise accuracy from ~0.46 to ~0.66.
Group Classification: Significant improvements in correctly identifying podium, points, and no-points finishers.
Model Insights: Grid position, reliability metrics, and recent performance were among the most influential features.
Betting Analysis
A hypothetical betting scenario for the 2024 season was tested, using model predictions to place wagers. The resulting strategy yielded a positive ROI of 35.79%, indicating the potential real-world application of data-driven predictions for sports betting enthusiasts.

<!-- CONTACT -->
## Contact

Joel Calm  - [@joel-calm](https://www.linkedin.com/in/joel-calm/) - joelcalm44@gmail.com

Project Link: [https://github.com/joelcalm/Formula1Prediction](https://github.com/joelcalm/Formula1Prediction)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/joelcalm/RandomForest.svg?style=for-the-badge
[contributors-url]: https://github.com/joelcalm/RandomForest/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/puchee99/PytorchClassifier.svg?style=for-the-badge
[forks-url]: https://github.com/joelcalm/RandomForest/network/members
[stars-shield]: https://img.shields.io/github/stars/joelcalm/RandomForest.svg?style=for-the-badge
[stars-url]: https://github.com/joelcalm/RandomForest/stargazers
[issues-shield]: https://img.shields.io/github/issues/joelcalm/RandomForest.svg?style=for-the-badge
[issues-url]: https://github.com/joelcalm/RandomForest/issues
[license-shield]: https://img.shields.io/github/license/joelcalm/RandomForest.svg?style=for-the-badge
[license-url]: https://github.com/joelcalm/RandomForest/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/joel-calm/
