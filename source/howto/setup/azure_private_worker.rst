:orphan:

.. meta::
    :description: How to prepare your Microsoft Azure environment for a Valohai Private Workers installation


Preparing your Azure subscription for Valohai Worker Setup
############################################################################

This document prepares your Microsoft Azure subscription for a Valohai private worker installation.


Creating a Subscription (optional)
----------------------------------------

This document prepares your Microsoft Azure account for Valohai worker installation. You can either use an existing Microsoft Azure subscription, or setup a new subscription for the Valohai resources.

If you wish to create a separate subscription for Valohai, navigate to Subscriptions panel and click "Add" at the top left of the screen to get started.


Creating a Resource Group
----------------------------------------

You need to create a resource group to host the Valohai-managed resources.

Navigate to `Resource Group Management <https://portal.azure.com/#blade/HubsExtension/Resources/resourceType/Microsoft.Resources%2Fsubscriptions%2FresourceGroups>`_ and select "Add".

Select the Subscription you'd like the resources to be created within, then name the Resource Group.

If you're not feeling creative, name the group ``valohai`` for simplicity. However, *take a note of the name*, as Valohai engineers will need this.

Also select the appropriate region for the resources:

* When selecting your region, remember that regions have different collections of available GPU types.
    * For US customers, we recommend **East US** or **West US 2** as they have the widest array of GPU machine types in the United States.
    * For EU customers, we recommend **West Europe** as it has the widest array of GPU machine types in the Europe.
    * Check Azure product availability page for more details.
* Consider using the same region where your data is located to reduce data transfer times.
* Consider using the regions where you've already acquired GPU quota from Microsoft.

Creating an App Registration
----------------------------------------

Next, create an app registration in your Azure AD to allow Valohai programmatic access to your resource group:

* This can done at `the App Registration management panel <https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps>`_ 
* Click ``New registration``
* Any name for the application will do – "Valohai" is a good choice.
* The "Supported Account Type" option should be left at "Accounts in this organizational directory only (Your Organization Name Here)".
* The Redirect URI can be left empty.

Once the App Registration is created, **take a note of the Application (client) and Directory (tenant) ID values** displayed.

Then navigate to the new app registration and select "Certificates & Secrets", then "New client secret".

* Any Description will do – "Valohai Secret", for instance, is fine.
* The Expiry time should preferably be "Never". Otherwise Valohai's access to manage your resources will expire and another secret will need to be created.

Once the Secret is created, copy the Value from the table and **take a note of it** –
this is the only time you'll be able to see it.

Adding permissions for the App Registration
----------------------------------------------------------------

Once the App Registration has been created, you will need to grant it access to manage resources.

Navigate to the `Subscriptions panel <https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade>`_, select the subscription you chose for your resource group.

**Take a note** of the subscription ID.

Now select "Access Control (IAM)", we'll need two role assignments:

* "Virtual Machine Contributor", for scaling workers up and down
* "Network Contributor", to configure worker network

To add these,

* Select "Add > Add Role Assignment".
* Choose the role required – see above.
* Type in the start of the name of the App Registration in the "Select" field until the app appears in the
  list below, then select it.
* Click "Save".

Repeat this until the roles have been added.

Please note that this will grant Valohai access to all virtual machines within that subscription or resource group. More granular permissions ([custom roles][custom-roles]) are supported by Azure, but they can not be created within the portal.azure.com user interface and as such are out of scope for this guide.

Registering Resource Providers for the Subscription
------------------------------------------------------

Registering a resource provider configures your subscription to work with the given resource provider. Essentially registering a provider means "enabling" the related services on your subscription.

Valohai uses the following resource providers:

* Microsoft.Compute
* Microsoft.Network

To verify that the above resource providers are registered:

* Navigate to "Azure Portal > Subscriptions".
* Select the subscription that will be used for Valohai.
* Navigate to "Resource providers" through the menu on the left.
* Register the following providers if they aren't already:
    * Microsoft.Compute
    * Microsoft.Network

Requesting more virtual machine quota (optional)
------------------------------------------------------------

Azure quotas limit how many resources you can utilize in parallel. Some resources like high-end GPU virtual machines might have no quota by default.

To check your current quotas and request for more:

* Navigate to "Home" > "Subscriptions" > Select subscription containing Valohai > "Usage + Quotas"
* Click "Request Increase"
* Change "Quota type" to "Compute-VM subscription limit increase"
* Click "Next"
* Click "Provide details"
* Keep the default deployment model ("Resource Manager")
* Select all the regions where you want to have your quotas increased e.g. East US, West US 2 and/or West Europe.
* Select the instance types you want to increase; for GPU workloads, you want to increase "NC Series", "NCSv2 Series" and/or "NCSv3 Series" quotas.
* Select new quota limits e.g. 96 vCPU per series is a good starting point.

Microsoft support resolves quota requests in a day or two.

Conclusion
------------

You should now have the following values:

* Region
* Subscription ID
* Resource Group Name
* Directory (tenant) ID
* Application (client) ID
* Application Secret

Share this information with your Valohai contact using the Vault credentials provided to you.