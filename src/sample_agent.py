from dotenv import load_dotenv
from camel.toolkits import HumanToolkit
from humanlayer.core.approval import HumanLayer
from camel.agents import EmbodiedAgent
from camel.generators import SystemMessageGenerator as sys_msg_gen
from camel.messages import BaseMessage as bm
from camel.types import RoleType

from agents import CodingAgent


load_dotenv(override=True)

def run_sample_agent() -> None: 
  user_request = bm.make_user_message(
      role_name="User",
      content="Create a Python script that generates the first 10 Fibonacci numbers and run it."
  )

  coding_agent = CodingAgent()
  response = coding_agent.step(user_request)
  print(response.msg.content)



if __name__ == "__main__": 
  run_sample_agent()
