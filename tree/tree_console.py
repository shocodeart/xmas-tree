import click
from tree.tree import Tree


@click.command()
def draw():
    tree = Tree(
        top_height=15,
        bottom_height=2,
        top_simbol=".",
    )
    tree.draw()


if __name__ == "__main__":
    draw()
