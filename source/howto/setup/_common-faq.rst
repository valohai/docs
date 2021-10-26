General
-------

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :stub-columns: 1

   * - Question
     - Answer
   * - Can we use our on-premises machines with Valohai?
     - Yes. Most of our on-premise workers are running Ubuntu 18.04 or higher, but we support other Linux distributions also. The machine will need Python 3.6 or higher, Docker, and the Valohai agent ("Peon") installed, so it knows how to read jobs from Valohai and handle commands.

       Valohai doesn't need direct access to the on-premises machine but the on-premises machine needs outbound access to your job queue virtual machine.
   * - What are Valohai workers?
     - Valohai workers are virtual machines used to run machine learning jobs (e.g. data preprocessing, training, evaluation) that a user launches from Valohai. These machines are created and terminated according to the autoscaling rules your organization defines in the Valohai web app (e.g. min scale, max scale, shutdown grace period).
   * - What's the purpose of the static (job queue) virtual machine?
     - The Valohai queue machine keeps track of your jobs. Valohai will write a record about incoming jobs, and the workers will fetch their jobs that have been scheduled for their queue. Each worker will then write execution logs back to the queue machine, from where app.valohai.com will read them and show them in the user interface.
   * - Can we use private Docker images?
     - Yes. Valohai supports standard docker login (username/password) and the main cloud providers. See the guide: :ref:`docker-private-registries`
   * - Does Valohai support SSO login?
     - Yes. Valohai supports Okta, SSO, SAML, and AzureAD authentication.
