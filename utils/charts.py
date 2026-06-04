import plotly.express as px

def bmi_histogram(df):

    fig = px.histogram(
        df,
        x="BMI",
        nbins=30,
        title="BMI Distribution"
    )

    return fig


def diabetes_pie(df):

    counts = df["Diabetes_012"].value_counts()

    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Diabetes Distribution"
    )

    return fig


def correlation_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=False,
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig


def age_diabetes_chart(df):

    fig = px.box(
        df,
        x="Diabetes_012",
        y="Age",
        title="Age vs Diabetes"
    )

    return fig
