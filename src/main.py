import asyncio
import nest_asyncio
import webbrowser
from dotenv import load_dotenv
from camel.toolkits import HumanToolkit
from camel.messages import BaseMessage
from humanlayer.core.approval import HumanLayer

from workforce import run_workforce
from agents import CodingAgent

nest_asyncio.apply()

load_dotenv(override=True)

hl = HumanLayer(verbose=True)
human_toolkit = HumanToolkit()


async def main() -> None: 
  result = await run_workforce("I am looking for a job, ask me questions if needed")
  coding_agent = CodingAgent()
  code_prompt = BaseMessage.make_user_message(
        role_name="user",
        content=f"Write and run a Flask program based on the following workforce's results, use port 6066 for the flask app. Results: {result} ",
    )

  response = coding_agent.step(code_prompt)
  print(response.msg.content)
  
  url = 'http://localhost:6066'
  webbrowser.open(url)
  print(f"\nOpened browser with the Flask app at {url}")


if __name__ == "__main__": 
  asyncio.run(main())
