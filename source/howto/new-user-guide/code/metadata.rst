:orphan:

.. meta::
    :description: Overview of how to collect key metrics as Valohai metadata


.. _migrate-metadata:

Collect metadata
#################################################

.. seealso::

    This how-to is a part of our :ref:`new-user-guide` series.


.. raw:: html

    <div style="position: relative; padding-bottom: 49.86149584487535%; height: 0;"><iframe src="https://www.loom.com/embed/ab2385e5b7a9408bb8527849e48d4645" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


.. include:: /_partials/_recap-metadata.rst

.. tab:: valohai-utils (Python)

    .. code-block:: python

        import valohai

        with valohai.metadata.logger() as logger:
            logger.log("epoch", epoch)
            logger.log("accuracy", accuracy)
            logger.log("loss", loss)

    ..

.. tab:: Python

    .. code-block:: python

        import json

        print()
        print(json.dumps({
            "epoch": epoch,
            "accuracy": accuracy,
            "loss": loss
        }))

    ..


.. tab:: R

    .. code-block:: r

        library(jsonlite)

        metadataEvent <- list()
        metadataEvent[["epoch"]] <- epoch
        metadataEvent[["accuracy"]] <- accuracy
        metadataEvent[["loss"]] <- loss

        write(toJSON(metadataEvent, auto_unbox=TRUE), stdout())
    ..

.. thumbnail:: /_images/compare_executions.png
    :alt: Metadata chart comparison

    
.. seealso::

    * `Creating visualizations </topic-guides/executions/metadata/>`_
    * `Compare executions </howto/executions/compare/>`_
    * `Save graphs from executions </howto/executions/complex-visualizations/>`_

.. hint:: 

    `Read more about valohai-utils </topic-guides/valohai-utils/>`_
