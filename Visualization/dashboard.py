"""
Code to visualize the algorithm solving a knapsack instance
"""

# Import Libraries
from dash import Dash, dcc, html, Input, Output, callback


# Initialize app
app = Dash(__name__)

# Set colors
colors = {"Items":"#fdfb7e", "Item-Selected":"#bafd7e",
          "Actions":"#ebffd8", "Action-used":"#ff745e",
          "Background":"#fffce7"}


# Create layout
app.layout = html.Div(
    style={"backgroundColor": colors["Background"]},
    children=[

        # Title and header
        html.Div([
            html.H2("0/1 Knapsack", style={"textAlign": "center"}),
            html.Br(),
        ]),

        # Select Instance to solve
        html.Div([
            html.H3("Select instance to solve:"),
            dcc.Dropdown(["Instance-1", "Instance-2"], "Instance-1", id="instance-selector")
        ], style={"width": "33%", "textAlign": "center", "margin-left": "auto", "margin-right": "auto"}),

        
        # Body
        html.Div(
            children=[

                # Left side: Items Available
                html.Div([
                    html.H4("Available Items", id="available-items-title", style={"textAlign": "center"}),
                    dcc.Graph(id="available-items-graph")
                
                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"}),
            
                
                # Middle: Actions
                html.Div([
                    html.H4("Heuristics", style={"textAlign": "center"})
                ], style={"width":"10%", "display": "inline-block", "padding": "0 20"}),


                # Right side: Packed Items
                html.Div([
                    html.H4("Packed Items", id="knapsack-title", style={"textAlign": "center"}),
                    dcc.Graph(id="knapsack-graph")

                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"})

            ]
        ),

        
        # Memory section
        dcc.Store(id="available-items-data"),
        dcc.Store(id="knapsack-data"),
        dcc.Store(id="colors"),
        dcc.Store(id="weight-data"),


    ]
)

# ------------------------------------
# Initialize variables of the instance
# ------------------------------------

@callback(
    Output("available-items-data", "data"),
    Output("knapsack-data", "data"),
    Output("colors", "data"),
    Output("weight-data", "data"),
    Input("instance-selector", "value")
)
def initialize_instance(instance_name: str):
    # After an instance is selected, load the instance and initialize variables
    print("Initializer was called")

    # Load instance
    items = [(1, 10, 10), (2,25,80)]

    # Empty knapsack
    knapsack = []

    # Create random colors for the item visualization
    colors = []

    # Create auxiliar variables
    min_weight = min([item[1] for item in items])
    max_weight = max([item[1] for item in items])

    return items, knapsack, colors, [min_weight, max_weight]


# ------------------------------------
# Functions to graph
# ------------------------------------

"""
Items graph
"""
@callback(
    Output("available-items-graph", "figure"),
    Input("available-items-data", "data")
)
def update_items_graph(items):
    # Create / Update the items graph
    print("Items graph was called")
    pass


"""
Knapsack graph
"""
@callback(
    Output("knapsack-graph", "figure"),
    Input("knapsack-data", "data")
)
def update_items_graph(items):
    # Create / Update the items graph
    print("Knapsack graph was called")
    pass



if __name__ == "__main__":
    app.run(debug=True)