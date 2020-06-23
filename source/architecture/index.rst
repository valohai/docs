.. meta::
    :description: Valohai deep learning management platform architecture diagram and installation flavors.

Architecture Overview
=====================

Valohai can be deployed in numerous ways; here are the four most common configurations:

**Valohai Cloud Installation** (`pdf </_static/Valohai_Architecture_SaaS.pdf>`__)
  * Run workloads under Valohai owned AWS, Google Cloud and Azure accounts.
  * You're billed depending on how much resources use use. You can also purchase credits in advance.
  * Works out of the box without any setup.

**Private Cloud Worker Installation:** (`pdf </_static/Valohai_Architecture_PrivateWorker.pdf>`__)
  * The virtual machines (worker nodes) that handle the data processing, training and inference are all deployed within your own AWS, Google Cloud or Azure.
  * No input or output data leaves your account perimeter.

**On-premises Worker Installation:**
  * The worker nodes are deployed to your persistent on-premises hardware.
  * This allows for additional features like `directory mounting </on-premises/>`_ unavailable for the cloud installations.

**Full Private Installation:** (`pdf </_static/Valohai_Architecture_FullPrivate.pdf>`__)
  * All components (inc. app.valohai.com) are deployed inside your own cloud provider account or data center.
  * This allows a self-contained installation that is managed and updated separately from the global Valohai installation.

.. note::

    Valohai technical team will go through customer requirements before each non-"Valohai Cloud" installation and
    set everything up in collaboration with the customer's infrastructure team.

    Valohai engineers spend between 1 hour and 2 days per installation, depending on the agreed configuration.
    After the installation, Valohai team will keep on maintaining and updating the software per a signed contract.

    Valohai Cloud installations don't require the above preparation as they don't have a separate technical setup.
    They work out of the box.

Components of a private cloud worker installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The private cloud worker installation is the most common installation method for Valohai. 

.. raw:: html

  <div id="architecture-map-container" style="width:100%">
      <img id="architecture" src="/_static/valohai-architecture-privateworker.png" usemap="#image-map" class="map" width="100%">

      <map name="image-map" id="image-map">
        <area target="_blank" alt="External code repositories for the data science projects (e.g. GitHub, GitLab, BitBucket or other Git repository)." title="External code repositories for the data science projects (e.g. GitHub, GitLab, BitBucket or other Git repository)." href="https://docs.valohai.com/tutorials/code-repository/" coords="1456,31,1664,243" shape="rect">
        <area  alt="The Valohai master node is the core component that manages all the other resources such as scheduling executions and managing scaling of CPU/GPU machines across cloud providers." title="The Valohai master node is the core component that manages all the other resources such as scheduling executions and managing scaling of CPU/GPU machines across cloud providers." href="https://docs.valohai.com/core-concepts/what-is-valohai/" coords="1035,851,1226,1038" shape="rect">
        <area target="" alt="Valohai users are managed inside Valohai and can be integrated with 3rd party identity managers (e.g. Azure Active Directory)" title="Valohai users are managed inside Valohai and can be integrated with 3rd party identity managers (e.g. Azure Active Directory)" href="" coords="1035,53,1219,244" shape="rect">
        <area target="" alt="Once you've published your endpoint you'll receive an HTTPS address that you can use for inference. This can be either public or limited to certain users." title="Once you've published your endpoint you'll receive an HTTPS address that you can use for inference. This can be either public or limited to certain users." href="" coords="3523,53,3710,244" shape="rect">
        <area alt="Contains user data and details of the executions ran on Valohai (e.g. which machine type, commands, input data was used)" title="Contains user data and details of the executions ran on Valohai (e.g. which machine type, commands, input data was used)" href="" coords="466,851,647,1042" shape="rect">
        <area  alt="Valohai stores store Git commit snapshots in binary storage (AWS S3, Azure Blob Storage, etc.) to maintain reproducibility. Worker machines load the user code archives from this storage." title="Valohai stores store Git commit snapshots in binary storage (AWS S3, Azure Blob Storage, etc.) to maintain reproducibility. Worker machines load the user code archives from this storage." href="" coords="1025,1597,1205,1784" shape="rect">
        <area alt="Stores the worker release binaries and configuration scripts that each worker machine uses to download inputs (e.g. training data), start the configured Docker image, report real-time logs and upload outputs (e.g. trained models)" title="Stores the worker release binaries and configuration scripts that each worker machine uses to download inputs (e.g. training data), start the configured Docker image, report real-time logs and upload outputs (e.g. trained models)" href="" coords="466,1890,654,2077" shape="rect">
        <area target="" alt="Real-time logs are moved to a persistent storage after the target execution finishes." title="Real-time logs are moved to a persistent storage after the target execution finishes." href="" coords="466,1402,650,1586" shape="rect">
        <area target="" alt="In-memory database instance that hosts execution/build queues and acts as temporary storage for user logs so they can be shown on the Valohai web app and API in real-time." title="In-memory database instance that hosts execution/build queues and acts as temporary storage for user logs so they can be shown on the Valohai web app and API in real-time." href="" coords="1802,1378,1986,1561" shape="rect">
        <area target="" alt="There is one worker group per instance type (e.g. g2.2xlarge on AWS) per region (e.g. AWS Ireland)." title="There is one worker group per instance type (e.g. g2.2xlarge on AWS) per region (e.g. AWS Ireland)." href="" coords="2569,1346,2951,1710" shape="rect">
        <area target="" alt="Workers are the servers that execute user code. The Valohai Master manages these auto-scaling groups. Workers can also be a non-scaling cluster of on-premises machines. Worker groups can be backed by local hardware, AWS, Azure, GCP or OpenStack." title="Workers are the servers that execute user code. The Valohai Master manages these auto-scaling groups. Workers can also be a non-scaling cluster of on-premises machines. Worker groups can be backed by local hardware, AWS, Azure, GCP or OpenStack." href="" coords="2237,1342,2558,1713" shape="rect">
        <area target="" alt="Workers are the servers that execute user code. The Valohai Master manages these auto-scaling groups. Workers can also be a non-scaling cluster of on-premises machines. Worker groups can be backed by local hardware, AWS, Azure, GCP or OpenStack." title="Workers are the servers that execute user code. The Valohai Master manages these auto-scaling groups. Workers can also be a non-scaling cluster of on-premises machines. Worker groups can be backed by local hardware, AWS, Azure, GCP or OpenStack." href="" coords="2954,1342,3276,1717" shape="rect">
        <area target="_blank" alt="Execution inputs are downloaded from and outputs are uploaded to a file storage (e.g. AWS S3, Azure Blob Storage, GCP Bucket)" title="Execution inputs are downloaded from and outputs are uploaded to a file storage (e.g. AWS S3, Azure Blob Storage, GCP Bucket)" href="https://docs.valohai.com/core-concepts/data-stores/" coords="3604,1363,3816,1561" shape="rect">
        <area target="_blank" alt="Each Valohai execution runs inside a Docker container. The configured Docker image is downloaded from a private or public Docker registry. Docker Hub is the most common one but you can also host a Docker registry inside your cloud provider account." title="Each Valohai execution runs inside a Docker container. The configured Docker image is downloaded from a private or public Docker registry. Docker Hub is the most common one but you can also host a Docker registry inside your cloud provider account." href="https://docs.valohai.com/docker-images/" coords="2654,1890,2859,2091" shape="rect">
        <area target="" alt="Before hosting your model for inference, we build a Docker image to make deployments fast and reliable. This image contains all the files required for the deployment so endpoint can be easily scaled." title="Before hosting your model for inference, we build a Docker image to make deployments fast and reliable. This image contains all the files required for the deployment so endpoint can be easily scaled." href="" coords="1806,579,1993,756" shape="rect">
        <area target="" alt="The inference Docker images used are uploaded to a private Docker registry, usually hosted under the inference provider account (e.g. AWS ECR, Azure Container Registry, GCP)" title="The inference Docker images used are uploaded to a private Docker registry, usually hosted under the inference provider account (e.g. AWS ECR, Azure Container Registry, GCP)" href="" coords="2664,579,2848,756" shape="rect">
        <area target="_blank" alt="The Kubernetes cluster that hosts the inference request/response endpoints. It downloads the used images from private inference registry and exposes them for clients. Hosted either by Valohai or in your own cloud service (e.g. AWS EKS, Azure AKS, GKE)" title="The Kubernetes cluster that hosts the inference request/response endpoints. It downloads the used images from private inference registry and exposes them for clients. Hosted either by Valohai or in your own cloud service (e.g. AWS EKS, Azure AKS, GKE)" coords="3527,576,3714,759" shape="rect" href="https://docs.valohai.com/core-concepts/deployments/">
      </map>
  </div>

  <script type="text/javascript">

  $(function() {
      // Show highlight and tooltip on hover
      $('area').hover(function(){
          // Disable clicking if there is no link
          if($(this).attr('href') == '') {
            $(this).click(false);
            $(this).css('cursor', 'default');
          }
          var text = $(this).attr('title');
          $(this).data('tipText', text).removeAttr('title');
          coords = $(this).attr("coords").toString().split(',')
          offset = $("#architecture-map-container").position()

          // Place highlight on the coordinates of the selected area
          $('<div class="architecture-highlight"></div>')
          .css({ 
              top: parseInt(coords[1]) + offset.top,
              left: parseInt(coords[0]) + offset.left,
              height: parseInt(coords[3]) - parseInt(coords[1]), 
              width: parseInt(coords[2]) - parseInt(coords[0]) })
          .appendTo('#architecture-map-container')
          .show();

          // Place tooltip below the coordinates of the selected area
          $('<p class="architecture-tooltip"></p>')
          .text(text)
          .css({ top: parseInt(coords[3]) + offset.top + 5, left: parseInt(coords[0])  + offset.left + 5 })
          .appendTo('#architecture-map-container')
          .show();
      },
      function() {
          // Remove tooltip and highlight on hoverout
          $(this).attr('title', $(this).data('tipText'));
          $('.architecture-tooltip').remove();
          $('.architecture-highlight').remove();
      })

  })

  window.onload = function () {
      var ImageMap = function (map, img) {
              var n,
                  areas = map.getElementsByTagName('area'),
                  len = areas.length,
                  coords = [],
                  previousWidth = 4000;
              for (n = 0; n < len; n++) {
                  coords[n] = areas[n].coords.split(',');
              }
              this.resize = function () {
                  var n, m, clen,
                      x = img.offsetWidth / previousWidth;
                  for (n = 0; n < len; n++) {
                      clen = coords[n].length;
                      for (m = 0; m < clen; m++) {
                          coords[n][m] *= x;
                      }
                      areas[n].coords = coords[n].join(',');
                  }
                  previousWidth = img.width;
                  return true;
              };
              window.onresize = this.resize;
          },
          imageMap = new ImageMap(document.getElementById('image-map'), document.getElementById('architecture'));
      imageMap.resize();
      return;
  }


  </script>

..


Here are descriptions of the individual components:

**Valohai Master:**
  Valohai master node that runs the web application and the API.
  The master is the core component that manages all the other resources such as scheduling executions and
  managing individual worker groups' scale across cloud providers.

**Valohai Database:**
  A relational database that contains user data and saves execution details such as which worker type was used,
  what commands were run, what Docker image was used, which inputs where used and what was the launch configuration.

**Git Repositories:**
  External code repositories for the data science projects.
  Usually a private GitHub repository but can be any Git repository
  such as GitLab, BitBucket or GitHub Enterprise as long as the Valohai Master can access it.

**User Code Archive:**
  We store Git commit snapshots in binary storage (AWS S3, Azure Blob Storage, etc.) to maintain reproducibility.
  Worker machines load the user code archives from this storage.

**Worker Binary Storage:**
  Worker machines have an executable that downloads inputs (e.g. training data),
  starts the configured Docker image, reports real-time logs and uploads outputs (e.g. trained models).
  Worker release binaries and configuration scripts are stored in this binary storage.

**Log Storage:**
  Real-time logs are moved to a persistent storage after the target execution finishes.

**Queues and Cache:**
  In-memory database instance that hosts execution/build queues and acts as temporary storage for
  user logs so they can be shown on the Valohai web app and API in real-time.

**Workers Groups:**
  Workers are the servers that execute user code.
  There is one worker group per instance type (e.g. g2.2xlarge on AWS) per region (e.g. AWS Ireland).
  The Valohai Master manages these auto-scaling groups.
  Workers can also be a non-scaling cluster of on-premises machines.
  Worker groups can be backed by local hardware, AWS, Azure, GCP or OpenStack.

**Artifact Stores:**
  Execution inputs are downloaded from and outputs are uploaded to a file storage.
  Valohai supports various storage backends but an AWS S3 bucket is the most commonly used artifact store.

**Docker Registries:**
  The Docker images used are downloaded from a private or public Docker registry.
  Docker Hub is the most common one but you can also host a Docker registry inside your cloud provider account.

**Inference Builders:**
  Before hosting your model for inference, we build a Docker image to make deployments fast and reliable.
  It will prebuild all files required for deployment so endpoint can be easily scaled.

**Inference Registry:**
  The inference Docker images used are uploaded to a private Docker registry,
  usually hosted under the inference provider account like AWS, GCP or Azure.

**Inference Cluster:**
  The Kubernetes cluster that hosts the inference request/response endpoints.
  It downloads the used images from private inference registry and exposes them for clients.
