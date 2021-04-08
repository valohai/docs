.. meta::
    :description: Valohai supports Azure active directory authentication and this page tells how it is done.

Integrating with Azure Active Directory
#########################################

Valohai Azure Active Directory integration allows keeping Valohai authentication and
access control on Azure, avoiding access control setting duplication.

Configure Azure AD integration for a Valohai organization
---------------------------------------------------------

You must be Valohai organization admin to enable Azure AD integration.

1. Login at https://app.valohai.com/
2. Navigate to ``Hi, <name> (the top right menu) > Manage <organization>``
3. Go to `Settings` under the organization controls.
4. Click on `Manage access grants...` in the `Access Grants` box.
5. Click on `Add new grant...`
6. Select which teams the matching users will automatically be added. Leave empty if none.
7. Add grant IDs; user or group UUIDs in Azure AD to match for.

Now, users that have or will have Azure AD login enabled and
are part of the AD group configured under access grants will
automatically be added to your Valohai organization.

**That's it; note that you don't need to send Valohai organization invitations to the users.**
Just tell them to register to Valohai and activate AD login like described in the section below.
They will be automatically added to the organization and potentially specified teams.

Join a Valohai organization using Azure AD
------------------------------------------

This assumes that the Valohai organization has been configured to integrate with your Azure AD.

1. Register/Login at https://app.valohai.com/
2. Navigate to ``Hi, <name> (the top right menu) > My profile > Authentication``.
3. Click on `Associate with Azure AD` in the `External Identity` box.
4. Follow the instructions to login to Azure AD.
5. Accept the `Valohai Login` application permission request in the Azure popup.

Now:

1. you will automatically be added to organizations and teams on Valohai
2. you can **only** login to Valohai using Azure AD

You can verify this by logging out, going to https://app.valohai.com/accounts/login/
and logging in through the `Log in using Azure AD` button.
