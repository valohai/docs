.. admonition:: A short introduction inputs
    :class: seealso

    * Valohai will download data files from your private cloud storage. Data can come from for example AWS S3, Azure Storage, GCP Cloud Storage, or a public source (HTTP/HTTPS).
    * Valohai handles authentication with your cloud storage, downloading and uploading, and caching data.
      
      * This means that you don't need to manage keys, authentication, and use tools like ``boto3``, ``gsutils``, or ``BlobClient`` in your code. Instead you should always treat the data as local data.
    
    * All Valohai machines have a local directory ``/valohai/inputs/`` where all your datasets are downloaded to. Each input will have it's own directory, for example ``/valohai/inputs/images/`` and ``/valohai/inputs/model/``.
    * Each step in your ``valohai.yaml`` can contain one or multiple input definitions and each input can contain one or multiple files. For example, in a batch inference step you could have a trained model file and a set of images you want to run the inference on.
    * Each input in ``valohai.yaml`` can have a default value. These values can be overriden any time you run a new execution to for example change the set of images you want to run batch inference on. 
