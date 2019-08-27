import os
from django.conf import settings
import datetime
from rest_framework import status
from ..library.exceptions import CustomAPIException

class FileService(object):
    @staticmethod
    def upload(file_obj, folder):
        
        if not file_obj:
            raise CustomAPIException(
                detail="File object is None.",
                status_code=status.HTTP_400_BAD_REQUEST)

        if file_obj.size > settings.ATT_SIZE_LIMIT:
            raise CustomAPIException(
                detail="Oops, the file is too large ({0})".format(file_obj.size),
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        folder_path = os.path.join(settings.FILE_PATH, folder)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        sep_index = file_obj.name.rfind(os.sep)
        file_origin_name = file_obj.name if sep_index < 0 else file_obj.name[
            sep_index + 1:]
        ext_index = file_origin_name.rfind('.')
        ext_name = file_origin_name[ext_index:].lower()

        if ext_name not in settings.ATT_TYPES:
            raise CustomAPIException(
                detail="Oops, we do NOT support this type ({0})".format(ext_name),
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)            

        file_name = "{0}_{1}{2}".format(
            file_origin_name[: ext_index],
            datetime.datetime.now().timestamp(),
            ext_name)
        full_name = os.path.join(folder_path, file_name)

        with open(full_name, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        return file_name
        
    @staticmethod
    def clear(folder):
        folder_path = os.path.join(settings.FILE_PATH, folder)

        if not os.path.exists(folder_path):
            return

        for the_file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                raise CustomAPIException(
                    detail=repr(e))