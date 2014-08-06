SwampDragon fileupload
======================

File upload handler for SwampDragon


# Installation
```pip install swampdragon-fileupload```

Add ```swampdragon_upload``` to ```INSTALLED_APPS```


# Usage

Create a router and extend ```FileUploadHandler```

    class FileUpload(FileUploadHandler):
        route_name = '_sdfileupload'


In the above example, the route is set to _sdfileupload.

File post requests should be done to ```window.swampDragon.url + '/_sdfileupload/'```

The data returned by the post request will fit the file deserializer
