from rest_framework.views import exception_handler
# from config.settings import logger
from datetime import datetime
from rest_framework import exceptions, status
from rest_framework.response import Response
#기본적으로 error는 view에서 처리하지만 view에서 걸러지지 않은 에러들은 exception_handler를 통해
#정해진 설정대로 return한다.
def custom_exception_handler(exc, context):
    # logger.error(f"[CUSTOM_EXCEPTION_HANDLER_ERROR]")
    # logger.error(f"[{datetime.now()}]")
    # logger.error(f"> exc")
    # logger.error(f"{exc}")
    # logger.error(f"> context")
    # logger.error(f"{context}")

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['time'] = datetime.now()       
    
    return response