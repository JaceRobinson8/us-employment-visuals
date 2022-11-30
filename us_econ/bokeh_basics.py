#!/usr/bin/env python
from bokeh.plotting import figure, show
from bokeh.models.tools import PanTool, WheelZoomTool


def main():
    x = list(range(1,6))
    y1 = [6, 7, 2, 4, 5]
    y2 = list(range(2,7))
    y3 = [4, 5, 5, 7, 2]

    plot = figure(title="Multi-line Ex", x_axis_label="x", y_axis_label="y",
                  active_drag="pan", active_scroll="wheel_zoom")

    plot.line(x, y1, legend_label="Temp.", color="aqua", line_width=2)
    plot.line(x, y2, legend_label="Rate", color="coral", line_width=2)
    plot.circle(x, y3, legend_label="Objects", color="black", line_width=2)

    show(plot)


if __name__ == "__main__":
    main()
