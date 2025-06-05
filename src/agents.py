from turtle import mode
from camel.agents import ChatAgent
from camel.messages import BaseMessage


class PreferenceAgent(ChatAgent):
  """
    A preference agent, which collects the preferences of the user regarding jobs
  """
  agent_role = BaseMessage.make_assistant_message(
    role_name="preference_agent",
    content="You are a preference agent, which collects the preferences of the user regarding jobs."
  )

  def __init__(self, model, message_window_size: int = 20):
    super().__init__(model=model, system_message=self.agent_role, message_window_size=message_window_size)

