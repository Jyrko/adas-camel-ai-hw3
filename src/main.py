import asyncio
import nest_asyncio
from dotenv import load_dotenv
from camel.toolkits import HumanToolkit
from humanlayer.core.approval import HumanLayer

from workforce import run_workforce

nest_asyncio.apply()

load_dotenv(override=True)

hl = HumanLayer(verbose=True)
human_toolkit = HumanToolkit()


async def main() -> None: 
  await run_workforce("I am looking for a job, ask me questions if needed")


if __name__ == "__main__": 
  asyncio.run(main())
