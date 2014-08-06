import json
from tornado.web import RequestHandler
from swampdragon_upload.file_upload_handler import make_file_id, get_file_location, get_file_url


class FileUploadHandler(RequestHandler):
    origin_check = False

    @classmethod
    def get_name(cls):
        return cls.route_name

    def _set_access_control(self):
        origin = self.request.headers['origin']
        if self.origin_check:
            orig_test = origin.split('/')[-1]
            if ':' in orig_test:
                orig_test = orig_test.split(':')[0]
            if not self.request.host.split(':')[0] == orig_test:
                return
        self.set_header('Access-Control-Allow-Credentials', True)
        self.set_header('Access-Control-Allow-Methods', 'POST')
        self.set_header('Access-Control-Allow-Origin', origin)

    def get(self, *args, **kwargs):
        self.write('Hello!')

    def post(self, *args, **kwargs):
        self._set_access_control()
        files = self.request.files['file']
        response = {'files': []}
        for f in files:
            file_id = make_file_id(f['body'])
            file_name = f['filename']
            named_file = open(get_file_location(file_name, file_id), 'wb')
            named_file.write(f['body'])
            named_file.close()
            response['files'].append({
                'file_id': file_id,
                'file_name': file_name,
                'file_url': get_file_url(file_name, file_id)
            })
        self.write(json.dumps(response))

    def options(self, *args, **kwargs):
        self._set_access_control()

    def file_upload(self, request):
        pass
