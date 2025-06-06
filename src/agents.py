from camel.agents import ChatAgent
from dotenv import load_dotenv
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.toolkits import FunctionTool, HumanToolkit, SearchToolkit, BrowserToolkit

from linkup import LinkupClient

load_dotenv(override=True)

default_model = ModelFactory.create(
  model_platform=ModelPlatformType.OPENAI,
  model_type=ModelType.GPT_4O
)

class SampleAgent(ChatAgent):
  """
    A sample agent with access to showcase calculator and human-in-the-loop
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="sample_agent",
    content=(
      "You are a sample agent."
    )
  )

  def calculator(n1: int, n2: int) -> int:
    """A simple calculator, use as a tool"""
    print("calculator is used")
    return n1 + n2
  
  def __init__(self, model=default_model, message_window_size: int = 20):
    human_toolkit = HumanToolkit()

    sample_tools = [
      FunctionTool(self.calculator),
      *human_toolkit.get_tools()
    ]

    super().__init__(
      model=model,
      system_message=self.agent_role,
      message_window_size=message_window_size,
      tools=sample_tools
    )

class PreferenceAgent(ChatAgent):
  """
    A preference agent, which collects (asks) and stores the preferences of the user regarding jobs
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="preference_agent",
    content="You are a preference agent, which collects (asks) and stores the preferences of the user regarding jobs."
  )

  human_toolkit = HumanToolkit()

  def __init__(self, model=default_model, message_window_size: int = 20):

    super().__init__(
      model=model, 
      system_message=self.agent_role, 
      message_window_size=message_window_size,
      tools=[*self.human_toolkit.get_tools()]
    )

class JobSearchAgent(ChatAgent):
  """
    A job search agent, which searches the information about related job posts
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="job_search_agent",
    content="You are a job search agent, which searches the information about related job posts"
  )

  linkup_client = LinkupClient()

  def get_job_search_data(self, input: str): 
    "Get the latest job postings data"
    print()
    print(input)
    response_linkup = self.linkup_client.search(
      query=input,
      depth="standard",
      output_type="sourcedAnswer"
    ) 
    return response_linkup.answer

  def __init__(self, model=default_model, message_window_size: int = 20):
    search_tools = [
      FunctionTool(self.get_job_search_data)
    ]

    print(search_tools[0].get_function_description())

    super().__init__(
      model=model,
      system_message=self.agent_role,
      message_window_size=message_window_size,
      tools=search_tools
    )

class WebAgent(ChatAgent):
  """
    An agent, which use one of the search engines to find additional resources that will help in the preparation for the job interview
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="preference_agent",
    content="You are a web search agent, which use one of the search engines to find additional resources that will help in the preparation for the job interview"
  )


  def __init__(self, model=default_model, message_window_size: int = 20):
    search_tools = [
      FunctionTool(SearchToolkit(timeout=5000).search_google),
      # *BrowserToolkit(headless=True, channel="chrome", web_agent_model=model, planning_agent_model=model).get_tools()
    ]

    super().__init__(
      model=model,
      system_message=self.agent_role,
      message_window_size=message_window_size,
      tools=search_tools
    )