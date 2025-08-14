import plotly.graph_objects as go
import numpy as np

def create_similarities_plot(titles, similarities, links, user_query):
    similarities_percentages = [round(score * 1, 2) for score in similarities]
    # Make y-axel labels clickable links
    y_labels = [f"<a href='{link}' target='_blank'>{title}</a>" for title, link in zip(titles, links)]
        
    
    fig = go.Figure(data=[go.Bar(
        x=similarities_percentages,
        y=y_labels,
        orientation='h',
        text=titles,
        hoverinfo='text',
        marker=dict(
            color=similarities_percentages,
            colorscale='Bluered',
        ),
        
    )])

    fig.update_layout(
        title=f"Matched Titles for: {user_query}",
        xaxis_title="Relevance (%)",
        yaxis_title="Related Terms",
        yaxis=dict(autorange='reversed'),
        margin=dict(l=10),
        xaxis=dict(title="Relevance (%)", range=[0, 100]),
    )
    return fig
