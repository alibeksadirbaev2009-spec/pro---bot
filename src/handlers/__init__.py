from aiogram import Router

from .commands import router as cmd_router
from .text import router as txt_router
from .callbacks import router as call_router
from .contact import router as cont_router

routers = Router()

routers.include_routers(cmd_router, txt_router, call_router, cont_router)