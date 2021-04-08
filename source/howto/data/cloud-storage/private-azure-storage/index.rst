.. meta::
    :description: Link your Azure Blob storage for data science experiments on Valohai. You can also add multiple data stores, even across cloud providers.

.. _cloud-storage-azure:

Add Azure Blob Storage
########################

In this guide, we'll link a private Azure storage account blob container to a Valohai project.

On Azure, you create storage accounts that have multiple services attached. One of those services is blob container,
which is Valohai's main interface on Azure-based installations.

.. admonition:: Requirements
   :class: attention

   * An Microsoft Azure subscription you can administer
   * A Valohai project which to link the Azure Blob Storage to
..


Create an Azure storage account and a blob container
--------------------------------------------------------

.. admonition:: Using an existing Azure Blob storage
   :class: tip

   You can skip this part and go directly to the next section, if you're using an existing Storage container


* **Create an Azure Storage Account** in your Microsoft Azure subscription.
* **Select storage account name and location.** Create the storage account in the location you'll be running your work to reduce transfer costs.
* Click on **Containers** on the navigation bar on the right side.
* Click on **+ Container**
* Give the container a name like ``valohai-sample`` and keep the public access level as ``Private``.
* Click **Create**


Configure CORS for the blob container
-------------------------------------------

.. admonition:: What is CORS?
   :class: seealso

   CORS is an HTTP feature that enables a web application running under one domain (app.valohai.com) to access resources in another domain (your storage).
   `Read more at Microsoft Docs <https://docs.microsoft.com/en-us/rest/api/storageservices/cross-origin-resource-sharing--cors--support-for-the-azure-storage-services>`_


If you wish to be able to upload files to the store using the `app.valohai.com` web UI, you will need to
add a CORS policy document to the blob container.

* Click on **CORS** on the navigation bar on the right side.
* Make sure the **Blob service** tab is elected
* Add the following 2 lines of configuration:

+---------------------------+---------------+-----------------------+---------------------+-----------+
| Origins                   | Methods       | Allowed Headers       | Exposed Headers     | Max Age   |
+===========================+===============+=======================+=====================+===========+
| `*`                       | GET,OPTIONS   | content-type,x-ms-*   | x-ms-meta-*         |   3000    |
+---------------------------+---------------+-----------------------+---------------------+-----------+
| `https://app.valohai.com` | POST,PUT      | content-type,x-ms-*   | x-ms-meta-*         |   3000    |
+---------------------------+---------------+-----------------------+---------------------+-----------+

Now your blob container allows uploads through `https://app.valohai.com` web application.

.. thumbnail:: _images/azure-data-cors.png
   :alt: Azure storage account CORS settings page.

Record access key for later usage
-------------------------------------------

Using the Azure portal, find and save access key under storage account `Access keys` tab.
This will be added to Valohai in the next step.

.. thumbnail:: _images/azure-data-key.png
   :alt: Azure storage account access key page.

Add the store to Valohai
-------------------------------------------

Data Stores can be either configured on the project level, or shared across your organization.

.. tab:: Default data store for project

   * Open a project in the web application
   * Click on the **Data Store** table
   * Click on **Add Azure Blob Storage Store** 
   * Add in the details you created in the Azure portal
   * The store name is the name that will be visible on Valohai. Make it something you recognie (e.g. <organization-name>-store)
   * (optional) Click on **Make project default store** to make it the default upload location for this project.

   When you create the store, the provided access key will be validated.

   .. thumbnail:: _images/azure-data-add-store.png
      :alt: Valohai data store listing page.


.. tab:: Default data store for organization

   for orgs

   