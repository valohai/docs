.. meta::
    :description: Link your Azure Storage Account Blob Container for data science experiments on Valohai. You can also add multiple data stores, even across cloud providers.

Connecting to Azure Storage Account
===================================

In this guide, we'll link a private Azure storage account blob container to a Valohai project.

On Azure, you create storage accounts that have multiple services attached. One of those services is blob container,
which is Valohai's main interface on Azure-based installations.

.. contents::
   :backlinks: none
   :local:

.. container:: alert alert-warning

   Data Stores can be either configured on project level, or shared across your organization.
   
   This guide will show you how to configure a Data Store for a single project, but you can follow the same steps to configure a shared Data Store under your settings.
   
   You can also promote a previously created Data Store from a project owned by your organization to a shared store.

..

1. Requirements
~~~~~~~~~~~~~~~

For this tutorial you will need:

* Azure account you can administer
* a Valohai project which to link the Azure storage account blob container to

2. Create an Azure storage account and a blob container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Naturally, skip this step if you already have a storage account and a blob container.

.. thumbnail:: azure-01-storage-list.png
   :alt: Azure portal storage account listing.

Create an Azure Storage Account through the Azure portal (https://portal.azure.com) by navigating to `Storage accounts > + Add`.

2.1 Select storage account name and location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: azure-02-create-storage.png
   :alt: Azure portal storage account creation page.

Throughout this guide, we will assume the name of the storage account name is ``tensorflow``; *be sure to replace this with the actual name of your storage account* when copying in any example configuration!

Create the storage account in the location you'll be running your work to reduce transfer costs.

2.2 Create a blob container
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: azure-03-create-container.png
   :alt: How to navigate to Blob Container creation page.

You will have to create a blob container inside the storage account to host your files.

Navigate to `Blobs > + Container`.

2.3 Name your blob container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. thumbnail:: azure-04-name-container.png
   :alt: Configuration options of your blog container.

You can name your container anything you want. In this guide, we assume it is ``mnisty``.

Make sure that the public access level is ``Private``.

3. Configure CORS for the blob container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to be able to upload files to the store using the `app.valohai.com` web UI, you will need to
add a CORS policy document to the blob container.

.. thumbnail:: azure-05-cors.png
   :alt: Azure storage account CORS settings page.

Navigate `Settings > CORS > Blob service` and add the following 2 lines of configuration:

+---------------------------+---------------+-----------------------+---------------------+-----------+
| Origins                   | Methods       | Allowed Headers       | Exposed Headers     | Max Age   |
+===========================+===============+=======================+=====================+===========+
| `*`                       | GET,OPTIONS   | content-type,x-ms-*   | x-ms-meta-*         |   3000    |
+---------------------------+---------------+-----------------------+---------------------+-----------+
| `https://app.valohai.com` | POST,PUT      | content-type,x-ms-*   | x-ms-meta-*         |   3000    |
+---------------------------+---------------+-----------------------+---------------------+-----------+

Now your blob container allows uploads through `https://app.valohai.com` web application.

4. Record access key for later usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: azure-06-access-keys.png
   :alt: Azure storage account access key page.

Using the Azure portal, find and save access key under storage account `Access keys` tab.
This will be added to Valohai in the next step.


5. Link the store to Valohai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: azure-07-vh-add-store.png
   :alt: Valohai data store listing page.

Navigate to `Project > Settings > Data Stores > Add Azure Blob Storage Store`

.. thumbnail:: azure-08-vh-store-config.png
   :alt: Valohai data store creation page.

Paste in the blob container name, storage account name and storage account access key.
Store name can be anything that helps you to identify the store but it is common just to use the blob container name.

When you create the store, the provided access key will be validated.

.. thumbnail:: azure-09-vh-default-store.png
   :alt: Valohai default project upload store configuration.

Once set up, you can set the store as your project's default upload store in the `Settings > General` view.
This ensures uploaded outputs will be stored in the blob container.
