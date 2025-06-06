from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import FunctionTool, HumanToolkit
from humanlayer.core.approval import HumanLayer
from linkup import LinkupClient

from agents import SampleAgent


load_dotenv(override=True)

hl = HumanLayer(verbose=True)
human_toolkit = HumanToolkit()


def main() -> None: 
  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O
  )

  agent = SampleAgent(model=model)


  response = agent.step("Ask me some question and wait for my input, do not stop unless expicitly said to do so")

  print(response.msgs[-1].content)


if __name__ == "__main__": 
  main()
