"""
Code to visualize the algorithm solving a knapsack instance
"""

# Import Libraries
from dash import Dash, dcc, html, Input, Output


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
            html.H2("0/1 Knapsack", style={"textAlign": "center"})
        ]),

        
        # Body
        html.Div(
            children=[

                # Left side: Items Available
                html.Div([
                    html.H4("Available Items", id="available-title", style={"textAlign": "center"}),
                    # Put graph here
                
                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"}),
            
                
                # Middle: Actions
                html.Div([
                    html.H4("Heuristics", style={"textAlign": "center"})
                ], style={"width":"10%", "display": "inline-block", "padding": "0 20"}),


                # Right side: Packed Items
                html.Div([
                    html.H4("Packed Items", id="knapsack-title", style={"textAlign": "center"}),
                    # Put graph here
                ], style={"width":"45%", "display": "inline-block", "padding": "0 20"})

            ]
        )


    ]


)

if __name__ == "__main__":
    app.run()