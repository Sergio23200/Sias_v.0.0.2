from cel.assistants.router.agentic_router import AgenticRouter
from service.stateless_timeout import StatelessTimeout
from cel.assistants.router.logic_router import LogicRouter
from cel.gateway.request_context import RequestContext
from cel.message_enhancers.smart_message_enhancer_openai import SmartMessageEnhancerOpenAI
from cel.gateway.message_gateway import MessageGateway, StreamMode
from cel.connectors.telegram import TelegramConnector
from pathlib import Path
import sys
import os
from loguru import logger as log
from dotenv import load_dotenv
load_dotenv()
# Add parent directory to path
path = Path(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(path.parents[1]))


timeout_manager = StatelessTimeout(redis_url=os.environ.get("STATE_REDIS_URL"))
assistants = [build_libranza(), build_cobranza()]


ast = AgenticRouter(assistants=assistants)


@ast.event('message')
async def handle_message(session, ctx: RequestContext):
    log.critical(f"Got message event in the balancer for logic!")
    try:
        msg = ctx.message.metadata
        lead = ctx.lead.metadata
        valid_disabled_ai = lead["raw"]["conversation"]["custom_attributes"][
            "disabled_ai"] if lead["raw"]["conversation"]["custom_attributes"] != None else False

        if valid_disabled_ai != True:
            print('Estas entrando a validar donde lo necesitas')
        elif valid_disabled_ai == True:
            print('Elimina el tiempo de reenganche y despedida')
            return RequestContext.cancel_ai_response()
    except Exception as e:
        print("Error en la session", e)
gateway = MessageGateway(
    assistant=ast,
    host="127.0.0.1", port=5004
)

conn = TelegramConnector(
    token=os.environ.get("TELEGRAM_TOKEN"),
    stream_mode=StreamMode.FULL
)

gateway.register_connector(conn)

gateway.run(enable_ngrok=True)
