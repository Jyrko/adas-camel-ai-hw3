from camel.agents import ChatAgent, EmbodiedAgent
from dotenv import load_dotenv
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType, RoleType
from camel.generators import SystemMessageGenerator
from camel.toolkits import FunctionTool, HumanToolkit, SearchToolkit
from camel.toolkits.async_browser_toolkit import AsyncBrowserToolkit
from camel.interpreters import InternalPythonInterpreter

from linkup import LinkupClient

load_dotenv(override=True)

default_model = ModelFactory.create(
  model_platform=ModelPlatformType.OPENAI,
  model_type=ModelType.GPT_4O
)


class PreferenceAgent(ChatAgent):
  """
    A preference agent, which collects (asks) and stores the preferences of the user regarding jobs
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="preference_agent",
    content=(
      "You are a preference agent, which collects (asks) and stores the preferences of the user regarding jobs." \
      " No more than 10 questions. Ask about revelant skills."
    )
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
    response_linkup = self.linkup_client.search(
      query=f"Find job postings for the given skills/preferences, give direct links in your output. Skills/preferences: {input}",
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
    content="You are a web search agent, which use one of the search engines to find additional resources that will help "
    "in the preparation for the job interview. Provide at least 5 helpful resources. Make a 2 week preparation plan based on your search." \
  )


  def __init__(self, model=default_model, message_window_size: int = 20):
    search_tools = [
      FunctionTool(SearchToolkit(timeout=5000).search_google),
      *AsyncBrowserToolkit(headless=True, channel="chrome", web_agent_model=model, planning_agent_model=model).get_tools()
    ]

    super().__init__(
      model=model,
      system_message=self.agent_role,
      message_window_size=message_window_size,
      tools=search_tools
    )

class CodingAgent(EmbodiedAgent):
    """
    a coding agent that will develop a HTML website to summarize the results from workforce
    """
    role = 'Programmer'
    task = (
      'Summarize the workforce results by presenting it on a HTML page in Flask framework.'
      ' Output only valid python code without any explanations at all, so the output can be directly run by the interpreter.'
    )

    agent_spec = dict(role=role, task=task)
    role_tuple = (role, RoleType.EMBODIMENT)

    agent_msg = SystemMessageGenerator().from_dict(meta_dict=agent_spec, role_tuple=role_tuple)

    def __init__(self, model = default_model):
        super().__init__(system_message=self.agent_msg, 
                         model=model, 
                         tool_agents=None, 
                         code_interpreter=None,
                         verbose=True
                         )
