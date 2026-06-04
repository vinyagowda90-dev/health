def dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum()
    }

    return summary


def bmi_insight(df):

    avg_bmi = round(df["BMI"].mean(), 2)

    if avg_bmi < 18.5:
        status = "Underweight Population"

    elif avg_bmi < 25:
        status = "Healthy Population"

    elif avg_bmi < 30:
        status = "Overweight Population"

    else:
        status = "Obese Population"

    return avg_bmi, status


def diabetes_percentage(df):

    diabetic = (
        (df["Diabetes_012"] > 0).sum()
        / len(df)
    ) * 100

    return round(diabetic, 2)
