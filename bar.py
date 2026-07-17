import plotly.express as px

data = {
    "fruit": ["apples", "oranges", "bananas", "apples", "oranges", "bananas"],
    "amount": [4, 1, 2, 2, 4, 5],
    "city": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
}

fig = px.bar(
    data,
    x="fruit",
    y="amount",
    color="city",
    barmode="group",
    title="Fruit Consumption by City"
)

fig.update_layout(template="plotly_dark")

fig.show()
