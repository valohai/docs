:orphan:

.. meta::
    :description: Overview of how to collect key metrics as Valohai metadata


.. _migrate-metadata:

Collect metadata
#################################################

.. seealso::

    This how-to is a part of our :ref:`new-user-guide` series.


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
