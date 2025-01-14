<div id="top"></div>

# BERT based Aspect-Based Sentiment Analysis with LDA topic model for stock price prediction

観点感情分析結果を利用したトピックモデルによる株価推定

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
      <ul>
        <li><a href="#development-enviroment">Development Enviroment</a></li>
        <li><a href="#data">Data</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>
</br>
</br>

## Overview

stock price prediction
&nbsp;
</br>
</br>

### Development Enviroment

> #### Software
>
> - Windows 10
> - Python 3.10.8
> - pip3

> #### Library
>
> - transformers
> - yfinance
> - pandas
> - numpy
> - matplotlib
>   &nbsp;

### Dataset

> #### Text Data : [Headlines related to U.S. businesses (Kaggle)](https://www.kaggle.com/datasets/notlucasp/financial-news-headlines)
>
> 1.  CNBC (2017/12/22 - 2020/7/17)
> 2.  The Guardian (2017/12/17 - 2020/7/18)
> 3.  Reuters (2018/3/20 - 2020/7/18)

> #### Stock Price Data : [3 Major U.S. Stock Indexes (Yahoo! Finance)](https://finance.yahoo.com/)
>
> 1.  S&P 500 (^GSPC)
> 2.  NASDAQ Composite (^IXIC)
> 3.  Dow Jones Industrial Average (^DJI)

I prepared preprocessed-data in shared directory.
You can download below link.

[How to Download the Dataset?](DATASET.md)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

_You need to install all._

- npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app._


1. Clone the repo
   ```sh
   git clone http://133.2.208.93/kim/absa-lda-stock-prediction.git
   ```
2. Install packages
   ```sh
   pip3 install -r requirements.txt
   ```
3. Download dataset
  [Download from this link](DATASET.md)

  

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space.
</br></br>

### 1. Morphological analysis

Move to <code>/src</code>

   ```sh
   cd src
   ```

Excute <code>Morphological_Analysis.py</code>

   ```sh
   python Morphological_Analysis.py
   ```
output file: <code>output_morphological.py</code>

</br></br>

### 2. LDA model
Move to <code>/long</code>
   ```sh
   cd long
   ```

Excute <code>LDA_data.py</code>

: Make folder for training data

   ```sh
   python LDA_data.py
   ```

Excute <code>LDA_train.py</code>

: train LDA
   ```sh
   python LDA_train.py
   ```


Excute <code>LDA_inference.py</code>

: make topic vector by using LDA
   ```sh
   python LDA_inference.py
   ```

</br></br>

### 3. LSTM model

Excute <code>LSTM_train.py</code>

   ```sh
   python LSTM_train.py
   ```

Excute <code>LSTM_test.py</code>

&nbsp;&nbsp;: test LSTM

   ```sh
   python LSTM_test.py
   ```

result file: <code>data\result\long</code>

<p align="right">(<a href="#top">back to top</a>)</p>
