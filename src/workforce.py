from camel.societies.workforce import Workforce
from camel.tasks import Task
from agents import PreferenceAgent, WebAgent, JobSearchAgent

def run_workforce(task_input: str) -> str: 
  workforce = Workforce(
    "agent workforce that will facilitate the process of finding job postings"
    "relevant to user's preferences and after user approval preparing a two "
    "week interview preparation plan" 
  )

  workforce.add_single_agent_worker(
    "agent, which collects user preferences about the job", 
    worker=PreferenceAgent
  )
  workforce.add_single_agent_worker(
    "agent, which searches via API relevant job postings",
    worker=WebAgent
  )
  workforce.add_single_agent_worker(
    "agent, which use one of the search engines to find additional resources that will help in the preparation for the job interview",
    worker=JobSearchAgent
  )

  task = Task(
    content=task_input
  )

  task = workforce.process_task(task)
  return task.result

