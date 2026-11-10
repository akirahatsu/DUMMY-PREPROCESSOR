                        ╔══════════════════════════════════════════════════════════════════════╗
                        ║                                                                      ║
                        ║                                                                      ║
                        ║          ██████╗ ██╗   ██╗███╗   ███╗███╗   ███╗██╗   ██╗            ║
                        ║          ██╔══██╗██║   ██║████╗ ████║████╗ ████║╚██╗ ██╔╝            ║
                        ║          ██║  ██║██║   ██║██╔████╔██║██╔████╔██║ ╚████╔╝             ║
                        ║          ██║  ██║██║   ██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝              ║
                        ║          ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║               ║
                        ║          ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝               ║
                        ║                                                                      ║
                        ║                 D U M M Y   P R E P R O C E S S O R                  ║
                        ║                                                                      ║
                        ║                                                                      ║
                        ╚══════════════════════════════════════════════════════════════════════╝



# Overview

DUMMY PREPROCESSOR is a Python data preprocessing library designed to simplify the preparation of datasets for Machine Learning and Deep Learning.

It provides automatic and manual tools for:

- Dataset inspection and AI-assisted data review.
- Missing value detection and handling.
- Date and Unix timestamp detection.
- Date feature extraction.
- Numerical normalization.
- Categorical one-hot encoding.
- Saving and reusing normalization parameters.
- Reversing target normalization for regression predictions.

The library is designed to make data preparation easier while keeping the user in control of important preprocessing decisions.

## Installation

```bash
pip install dummy-preprocessor
```

## Basic Usage

Import the library:

```python
from dummy_preprocessor import DUMMY_PI

preprocess = DUMMY_PI("YOUR_DATA_PATH")
```

You can also provide an existing Pandas DataFrame:

```python
preprocess = DUMMY_PI(input=your_dataframe)
```

> **Important: Inspect your dataset before applying automatic preprocessing.**
>
> Start by reviewing the dataset using `get_veiw()`. This helps you understand missing values, detected date columns, data types, and the general structure of your data before making changes.

```python
preprocess.get_veiw()
```

You can also read the instructions below to understand the available preprocessing methods and their parameters.

---

# 1. Missing Value Handling

Missing values are one of the most common problems in real-world datasets. DUMMY PREPROCESSOR provides automatic and manual methods for handling missing numerical and non-numerical values.

### `get_fill_missing()`

```python
preprocess.get_fill_missing()
```

**Parameters**

| Parameter | Default | Description |
|---|---|---|
| `operations` | `"auto"` | `"auto"` processes detected missing-value columns automatically. `"custom"` allows specific columns to be selected. |
| `columns` | `None` | A list of column names to process when using custom operations. |
| `inter` | `True` | Enables interaction, allowing users to choose between mean, median, or stopping the process. |
| `norma` | `False` | If enabled, numerical normalization is performed after missing-value handling. |

### How does automatic missing-value handling work?

For numerical columns, the library considers the percentage of missing values and the distribution of the data.

It also uses the Interquartile Range (IQR) to help decide whether the mean or median is more appropriate.

**Understanding IQR**

The Interquartile Range measures the spread of the middle 50% of the data.

\[
IQR = Q_3 - Q_1
\]

Where:

- \(Q_1\) is the 25th percentile.
- \(Q_3\) is the 75th percentile.

The library calculates the lower and upper boundaries:

\[
Lower = Q_1 - 1.5(IQR)
\]

\[
Upper = Q_3 + 1.5(IQR)
\]

Values outside these boundaries are considered potential outliers.

The outlier percentage helps identify whether a numerical distribution may be affected by extreme values.

**Mean vs Median**

- Mean is useful when numerical data is relatively balanced and does not contain many extreme values.
- Median is more robust when data contains outliers or is strongly skewed.

For non-numerical columns, the library uses the mode (the most frequent value) to fill missing values.

**Date columns are treated differently.** Missing date values are not automatically filled. Users should decide how to handle missing dates because replacing them with arbitrary values can introduce incorrect time information.

---

# 2. Date and Unix Timestamp Handling

Time-related information can contain useful patterns for Machine Learning models.

For example, a model may learn different patterns depending on the month, day of the week, or hour of the day.

DUMMY PREPROCESSOR can detect datetime columns and Unix timestamps, then extract useful numerical features.

### `get_data_extract()`

```python
preprocess.get_data_extract()
```

**Default parameters**

The `date_extract` parameter accepts a dictionary that controls which date features should be extracted.

```python
date_extract = {
    "year": None,
    "month": None,
    "day_of_week": None,
    "day_of_month": None,
    "week_of_year": None,
    "day_of_year": None,
    "hour_of_week": None,
    "second": None,
    "minute": None,
    "millisecond": None,
    "hour": None
}
```

To enable specific features:

```python
preprocess.get_data_extract(
    date_extract={
        "year": True,
        "month": True,
        "day_of_week": True,
        "day_of_month": True,
        "week_of_year": True,
        "day_of_year": False,
        "hour_of_week": False,
        "second": False,
        "minute": False,
        "millisecond": False,
        "hour": False
    }
)
```

### Supported time formats

**Datetime format:**

```text
2026-11-05 14:35:20
```

**Unix timestamp (seconds):**

```text
1325376060
```

The library detects supported Unix timestamps and converts them into datetime information before feature extraction.

### Why is date extraction useful?

Instead of giving a model a raw date string, you can provide numerical features such as:

- Month: seasonal patterns.
- Day of week: weekday vs weekend patterns.
- Hour: intraday patterns.
- Week of year: recurring weekly patterns.
- Year: long-term temporal trends.

This can be useful for financial datasets, Forex candle data, sales forecasting, freight-rate prediction, and other time-dependent Machine Learning tasks.

---

# 3. Numerical Normalization

Numerical features can have very different scales.

For example:

- Distance: 0–5,000.
- Weight: 0–100,000.
- Temperature: -20–50.

Features with very different numerical ranges can make optimization more difficult for some Machine Learning models.

### `normalize()`

```python
preprocess.normalize(train=True)
```

DUMMY PREPROCESSOR uses Min-Max normalization:

\[
X_{norm} = \frac{X-X_{min}}{X_{max}-X_{min}}
\]

This transforms numerical values using their minimum and maximum values.

**Parameters**

| Parameter | Default | Description |
|---|---|---|
| `train` | `True` | If `True`, saves minimum and maximum values from training data. If `False`, reuses previously saved training values. |

### Training and validation data

A consistent normalization process is important.

```python
# Training data
train_preprocess = DUMMY_PI("train.csv")
train_preprocess.normalize(train=True)

# Validation data
validation_preprocess = DUMMY_PI("validation.csv")
validation_preprocess.normalize(train=False)
```

The validation data reuses the minimum and maximum values learned from training data.

This helps prevent data leakage.

Values in validation data can fall outside the range [0, 1]. This is normal when they are outside the training data's original range.

---

# 4. Categorical One-Hot Encoding

Machine Learning models generally require numerical inputs.

One-hot encoding converts categorical values into binary columns.

### `one_hot_encode()`

```python
preprocess.one_hot_encode()
```

**Parameters**

| Parameter | Default | Description |
|---|---|---|
| `exclude` | `None` | A list of columns to exclude from encoding. |
| `max_categories` | `100` | Maximum number of unique categories allowed per column. |

### Example

Original data:

| Equipment |
|---|
| Truck |
| Van |
| Truck |
| Trailer |

After one-hot encoding:

| Equipment_Truck | Equipment_Van | Equipment_Trailer |
|---:|---:|---:|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 0 | 0 | 1 |

**High-cardinality warning**

Some columns contain hundreds or thousands of unique values.

For example, an ID column with 2,000 unique values could create 2,000 additional columns if one-hot encoded.

This can unnecessarily increase memory usage and model complexity.

DUMMY PREPROCESSOR can skip columns that exceed the configured `max_categories` limit.

Skipped columns remain in their original format.

---

# 5. Automatic Preprocessing

If you prefer to handle the main preprocessing tasks through one method, you can use `get_auto_fix()`.

### `get_auto_fix()`

```python
preprocess = DUMMY_PI("YOUR_DATA_PATH")

# Always inspect your dataset first
preprocess.get_veiw()

# Run automatic preprocessing
X = preprocess.get_auto_fix()
```

**Parameters**

| Parameter | Default | Description |
|---|---|---|
| `interactive` | `False` | Enables manual interaction for missing-value decisions. |
| `normalisation` | `False` | Enables numerical normalization. |
| `train` | `True` | Saves training min/max values or reuses previously saved values. |
| `encoding` | `False` | Enables one-hot encoding when supported by the implementation. |

The automatic pipeline handles:

1. Dataset review.
2. Missing numerical and non-numerical values.
3. Date and Unix timestamp processing.
4. Date feature extraction.
5. Optional numerical normalization.
6. Optional categorical encoding.

You can enable normalization and encoding when needed:

```python
X = preprocess.get_auto_fix(
    interactive=False,
    normalisation=True,
    train=True,
    encoding=True
)
```

For manual decisions:

```python
X = preprocess.get_auto_fix(
    interactive=True,
    normalisation=True
)
```

---

# 6. Target Normalization for Regression

In regression problems, the target variable (`y`) can have a very different scale from the input features.

DUMMY PREPROCESSOR provides separate methods for normalizing target values and converting predictions back to their original scale.

### `normalize_y()`

```python
y_train = preprocess.normalize_y(y_true)
```

The target values are normalized using their own minimum and maximum values.

### `back_norm()`

```python
original_predictions = preprocess.back_norm(prediction)
```

This converts normalized predictions back to the original target scale:

\[
y_{original} = y_{normalized}(y_{max}-y_{min})+y_{min}
\]

This is particularly useful when training regression models that predict real-world values, such as:

- House prices.
- Freight rates.
- Financial values.
- Energy consumption.
- Sales and demand.

---

# 7. AI-Assisted Data Review

DUMMY PREPROCESSOR also provides optional AI-assisted dataset review.

### `get_veiw()`

```python
preprocess.get_veiw(ai_review=True, describe=True)
```

**Parameters**

| Parameter | Default | Description |
|---|---|---|
| `ai_review` | `True` | Enables AI-assisted dataset review. Requires an internet connection. |
| `describe` | `True` | Controls whether the Pandas descriptive statistics are displayed. |

The review can help identify unusual distributions, suspicious values, and potential data-quality issues.

AI review is an additional feature, not a replacement for statistical checks or user judgment.

If you do not want to use the AI service:

```python
preprocess.get_veiw(ai_review=False)
```

---

# Intended Use Cases

DUMMY PREPROCESSOR is designed for general tabular data preparation and can be useful in projects involving:

- **Financial data:** preparing numerical and categorical features for financial Machine Learning.
- **Forex and time-series data:** extracting temporal features from candle timestamps.
- **Regression:** preparing target values and numerical input features.
- **Business analytics:** handling missing values and inspecting real-world datasets.
- **Forecasting:** extracting useful date and time information.
- **General Machine Learning:** preparing Pandas DataFrames before model training.

The library handles preprocessing, not financial prediction or trading decisions. The quality of the resulting model still depends on the dataset, feature selection, validation strategy, and model architecture.

## Important Notes

- Always inspect your dataset before applying automatic preprocessing.
- Review skipped categorical columns before passing the data to a model.
- Missing dates are not automatically filled.
- Normalization parameters should be learned from training data and reused for validation and test data.
- One-hot encoding can increase the number of features significantly.
- AI review requires an internet connection and is optional.
- Preprocessing does not guarantee better model performance; always evaluate your model on unseen data.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
