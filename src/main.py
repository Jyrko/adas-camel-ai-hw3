from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import FunctionTool
from humanlayer.core.approval import HumanLayer

load_dotenv(override=True)

hl = HumanLayer(verbose=True)

@hl.human()
def calculator(n1: int, n2: int) -> int:
  """A simple calculator, use as a tool"""
  return n1 + n2


def main() -> None: 
  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O
  )

  agent = ChatAgent(
    system_message="You are a smart agent",
    model=model,
    tools=[calculator]
  )

  response = agent.step("2 + 4123 is ?")

  print(response.msgs[-1].content)


if __name__ == "__main__": 
  main()
