
.. meta::
    :description: Save complex graphics and visualizations from executions

.. _executions-graphs:

Save graphs from executions
################################

Collecting `metadata </topic-guides/executions/metadata/>`_ allows you to easily visualize your key performance metrics as a time series graph or a scatter plot.

You can also generate more complex graphs inside your execution and save them as Valohai outputs.

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,14,15

    import matplotlib.pyplot as plt
    import numpy as np
    import valohai

    np.random.seed(19680801)
    data = np.random.randn(2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].hist(data[0])
    axs[1, 0].scatter(data[0], data[1])
    axs[0, 1].plot(data[0], data[1])
    axs[1, 1].hist2d(data[0], data[1])

    save_path = valohai.outputs().path('myplot.png')
    plt.savefig(save_path)

    plt.show()
    plt.close()

..

.. video:: /_static/videos/savegraph.mp4
    :autoplay:
    :width: 600
