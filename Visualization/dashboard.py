"""
Code to visualize the algorithm solving a knapsack instance
"""

# Import Libraries
from dash import Dash, dcc, html, Input, State, Output, callback, ctx
from dash.exceptions import PreventUpdate


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
            html.Div([
                dcc.Dropdown(["Instance-1", "Instance-2"], "Instance-1", id="instance-selector")
            ], style={"width": "70%", "height": "25px", "display": "inline-block",
                      "margin-right": "0px", "margin-left": "0px"}),
            html.Div([
                html.Button("Solve", id="solve-instance", n_clicks=0, style={"fontSize":"1.25em"}),
            ], style={"width": "30%", "height": "25px", "display": "inline-block",
                      "margin-left": "0px", "margin-right": "0px"})

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

        # Step intervals
        dcc.Interval(id="counter-interval", interval=5000, n_intervals=0),
        
        # Memory section
        ## Initial data
        dcc.Store(id="initial-items-data"),
        dcc.Store(id="initial-knapsack-data"),
        dcc.Store(id="colors"),
        dcc.Store(id="weight-data"),

        ## Current data
        dcc.Store(id="available-items-data"),
        dcc.Store(id="knapsack-data"),
        dcc.Store(id="trigger-selection", data=False),
        dcc.Store(id="trigger-graphs", data=False)
    ]
)

# ------------------------------------
# Initialize variables of the instance
# ------------------------------------

@callback(
    Output("initial-items-data", "data"),
    Output("initial-knapsack-data", "data"),
    Output("colors", "data"),
    Output("weight-data", "data"),
    Input("instance-selector", "value")
)
def initialize_instance(instance_name: str):
    # After an instance is selected, load the instance and initialize variables
    print("Initializer was called")

    # Load instance
    items = [(1,10,10), (2,25,80)]

    # Empty knapsack
    knapsack = []

    # Create random colors for the item visualization
    colors = []

    # Create auxiliar variables
    min_weight = min([item[1] for item in items])
    max_weight = max([item[1] for item in items])

    return items, knapsack, colors, [min_weight, max_weight]


# ------------------------------------
# Initialize the interval
# ------------------------------------
@callback(
    Output("counter-interval", "n_intervals"),
    Output("trigger-selection", "data"),
    Input("solve-instance", "n_clicks"),
    prevent_initial_call=True
)
def reset_interval(n):
    """
    Initialize to 0 the interval, and set True to select_items
    """
    print("Interval was reset")

    return 0, True


# ------------------------------------
# Select and item by an algorithm
# ------------------------------------
@callback(
    Output("available-items-data", "data"),
    Output("knapsack-data", "data"),
    Output("trigger-graphs", "data"),
    State("available-items-data", "data"),
    State("knapsack-data", "data"),
    Input("counter-interval", "n_intervals"),
    Input("trigger-selection", "data"),
    prevent_initial_call = True,
)
def select_item(items, knapsack, counter, trigger):
    print("Selector was called")

    if trigger:
        print("RIGHT")
        return items, knapsack, True

    return items, knapsack, PreventUpdate


# ------------------------------------
# Functions to graph
# ------------------------------------

"""
Items graph
"""
@callback(
    Output("available-items-graph", "figure"),
    State("available-items-data", "data"),
    Input("trigger-graphs", "data"),
    prevent_initial_call=True
)
def update_items_graph(items, trigger):
    # Create / Update the items graph
    print("Items graph was called")



"""
Knapsack graph
"""
@callback(
    Output("knapsack-graph", "figure"),
    State("knapsack-data", "data"),
    Input("trigger-graphs", "data"),
    prevent_initial_call=True
)
def update_items_graph(items, trigger):
    # Create / Update the items graph
    print("Knapsack graph was called")
    


if __name__ == "__main__":
    app.run(debug=True)