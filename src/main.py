from dotenv import load_dotenv
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import FunctionTool, HumanToolkit
from humanlayer.core.approval import HumanLayer

from agents import JobSearchAgent, SampleAgent


load_dotenv(override=True)

hl = HumanLayer(verbose=True)
human_toolkit = HumanToolkit()


def main() -> None: 
  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O
  )

  agent = JobSearchAgent(model=model)

  response = agent.step("What are currently available job posting for a Senior Python developer in Warsaw with salaray more than 16k PLN per month")
  

  print(response.msgs[-1].content)


if __name__ == "__main__": 
  main()
