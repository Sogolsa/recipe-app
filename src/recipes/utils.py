from recipes.models import Recipe
from io import BytesIO
import base64  # encode and decode method on object
import matplotlib.pyplot as plt


def get_graph():
    """Take care of low level image handling details"""
    buffer = BytesIO()  # create a BytesIO buffer(empty box) to store the image
    plt.savefig(buffer, format="png")  # Save the image in png format
    buffer.seek(0)  # Rewind to the beginning to see the image
    image_png = buffer.getvalue()  # Take the image as a bunch of bytes
    graph = base64.b64encode(
        image_png
    )  # Turn the bytes to special code using base64 encoding to send it over internet.
    graph = graph.decode(
        "utf-8"
    )  # Convert the code into string, so it's easier to send

    # free up the memory of buffer
    buffer.close()

    # return the image/graph
    return graph


# data: panda dataframe
def get_chart(chart_type, data, **kwargs):
    """The get_chart() function helps us draw these charts and then uses get_graph()
    to turn them into internet-friendly codes."""

    # AGG is preferred solution to write PNG files
    plt.switch_backend("AGG")  # set up the image

    """We create a space where we can draw, This space is 6 inches wide and 3 inches tall."""
    fig = plt.figure(figsize=(6, 3))

    # select chart_type based on user input from the form
    if chart_type == "#1":
        plt.bar(data["name"], data["cooking_time"], color="skyblue")
        plt.xlabel("Recipes")
        plt.ylabel("Cooking Time (minutes)")
        plt.title("Recipe by Cooking Time")
        plt.xticks(rotation=45, ha="right")  # set the angle of recipe names
        plt.gca().spines["right"].set_visible(
            False
        )  # make right side of frame invisible
        plt.gca().spines["top"].set_visible(False)  # make top side of frame invisible

    # We make sure everything fits nicely within the space.
    plt.tight_layout()

    # We use the get_graph() function to turn our drawing into a code that can be shared over the internet.
    chart = get_graph()
    return chart
