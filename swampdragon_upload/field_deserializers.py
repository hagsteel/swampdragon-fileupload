from django.core.files import File
from django.core.files.base import ContentFile
from swampdragon.serializers.field_deserializers import BaseFieldDeserializer, register_field_deserializer
from swampdragon_upload.file_upload_handler import get_file_location


class FileDeserializer(BaseFieldDeserializer):
    def __call__(self, model_instance, key, val):
        if not val:
            return
        if isinstance(val, str):
            return
        if isinstance(val, list):
            val = val[0]
        file_id = int(val['file_id'])
        if not file_id > 0:
            return
        path = get_file_location(val['file_name'], val['file_id'])
        uploaded_file = File(open(path, 'rb'))
        setattr(model_instance, key, val['file_name'])
        getattr(model_instance, key).save(
            val['file_name'],
            ContentFile(uploaded_file.read()),
            save=False
        )


class ImageDeserializer(FileDeserializer):
    pass


register_field_deserializer('FileField', FileDeserializer)
register_field_deserializer('ImageField', ImageDeserializer)
