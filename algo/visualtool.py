import numpy as np
from matplotlib.colors import colorConverter, Colormap, Normalize
from matplotlib.patches import FancyArrowPatch



def drawArrows(ax, edgelist, pos):
    def to_marker_edge(marker_size, marker):
        if marker in "s^>v<d":  # `large` markers need extra space
            return np.sqrt(2 * marker_size) / 2
        else:
            return np.sqrt(marker_size) / 2

    ## func argumuments ##
    edge_color = '#055a8c'

    node_size = 300
    node_shape = "o"

    # Edge line style (default='solid') (solid|dashed|dotted,dashdot)
    style = "solid"

    # size of the arrow head head's length and width  (default=10)
    arrowsize = 10

    # For directed graphs, choose the style of the arrowsheads.
    arrowstyle = "-|>"

    # min_source_margin minimum margin (gap) at the begining of the edge at the source.  (default=0)
    min_source_margin = 0

    # min_target_margin The minimum margin (gap) at the end of the edge at the target. (default=0)
    min_target_margin = 0

    # Line width of edges (default=1.0)
    width = 1.0

    connectionstyle = None

    ########

    edge_pos = np.asarray([(pos[e[0].idx], pos[e[1].idx]) for e in edgelist])

    line_width = width

    # Draw arrows with `matplotlib.patches.FancyarrowPatch`

    arrow_collection = []
    mutation_scale = arrowsize  # scale factor of arrow head

    # FancyArrowPatch doesn't handle color strings
    arrow_colors = colorConverter.to_rgba_array("#008081")

    for i, (src, dst) in enumerate(edge_pos):

        x1, y1 = src
        x2, y2 = dst
        shrink_source = 0  # space from source to tail
        shrink_target = 0  # space from  head to target

        shrink_source = shrink_target = to_marker_edge(node_size, node_shape)

        if shrink_source < min_source_margin: shrink_source = min_source_margin

        if shrink_target < min_target_margin: shrink_target = min_target_margin

        if len(arrow_colors) == len(edge_pos):
            arrow_color = arrow_colors[i]

        elif len(arrow_colors) == 1:
            arrow_color = arrow_colors[0]

        else:  # Cycle through colors
            arrow_color = arrow_colors[i % len(arrow_colors)]

        arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=arrowstyle, shrinkA=shrink_source, shrinkB=shrink_target,
                                mutation_scale=mutation_scale, color=arrow_color, linewidth=line_width,
                                connectionstyle=connectionstyle, linestyle=style, zorder=1, )  # arrows go behind nodes

        arrow_collection.append(arrow)
        ax.add_patch(arrow)

    if len(edge_pos) > 0:
        # update view
        minx = np.amin(np.ravel(edge_pos[:, :, 0]))
        maxx = np.amax(np.ravel(edge_pos[:, :, 0]))
        miny = np.amin(np.ravel(edge_pos[:, :, 1]))
        maxy = np.amax(np.ravel(edge_pos[:, :, 1]))

        w = maxx - minx
        h = maxy - miny

        padx, pady = 0.05 * w, 0.05 * h
        corners = (minx - padx, miny - pady), (maxx + padx, maxy + pady)

        ax.update_datalim(corners)
    ax.autoscale_view()

    ax.tick_params(axis="both", which="both", bottom=False, left=False, labelbottom=False, labelleft=False, )


def addLablesAndNodes(ax, frames, pos):
    labels = dict((frame.idx, frame.value) for frame in frames)
    xy = np.asarray([pos[frame.idx] for frame in frames])
    color = [frame.color for frame in frames]

    kwds = {}
    horizontalalignment = kwds.get('horizontalalignment', 'center')
    verticalalignment = kwds.get('verticalalignment', 'center')

    text_items = {}

    for n, label in labels.items():
        (x, y) = pos[n]

        if not isinstance(label, str):
            label = str(label)

        t = ax.text(x, y, label, size=10, color="k", family='sans-serif', weight="normal",
                    horizontalalignment=horizontalalignment, verticalalignment=verticalalignment,
                    transform=ax.transData, clip_on=True, )

        text_items[n] = t

    if len(xy) > 0:
        ax.scatter(xy[:, 0], xy[:, 1], s=300, edgecolor="#055a8c", c=color, marker="o", )  # label=text_items)
    ax.set_zorder(2)
    ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)


kwds = {}
horizontalalignment = kwds.get('horizontalalignment', 'center')
verticalalignment = kwds.get('verticalalignment', 'center')


def drawarr(ax, frames):
    data = [frame.value for frame in frames]
    x = [i * 1 for i in range(len(data))]
    y = [2 for _ in range(len(x))]
    color = [frame.color for frame in frames]

    for idx, ele in enumerate(data):
        ax.text(idx, 2, ele, color="k", family='sans-serif', weight="normal",
                horizontalalignment=horizontalalignment, verticalalignment=verticalalignment,
                transform=ax.transData, clip_on=True, )

    ax.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    ax.scatter(x, y, c=color, edgecolor="#008081", linewidths=1, marker="s", s=26 ** 2)
    ax.set_anchor("SW")
    #ax.set_aspect(aspect=5 ** 2)
    ax.margins(x=0.03, y=0.03)
    # ax2.set_aspect(aspect="auto", adjustable="box", anchor="N")
    ax.set_frame_on(False)