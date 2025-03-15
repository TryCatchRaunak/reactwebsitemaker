from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()


input_file_read = FileReadTool("/home/trycatchraunak/PycharmProjects/websitemaker/src/websitemaker/SDD.txt")
input_file_read2 = FileReadTool("/home/trycatchraunak/PycharmProjects/websitemaker/src/websitemaker/components.txt")
code_search_tool = ScrapeWebsiteTool("https://react.dev/")



@CrewBase
class Websitemaker():
	"""Websitemaker crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	"""AGENTS"""
	@agent
	def sdd_reader(self) -> Agent:
		return Agent(
			config=self.agents_config['sdd_reader'],
			tools=[input_file_read],
			verbose=True
		)
	
	@agent
	def website_components_decider(self) -> Agent:
		return Agent(
			config=self.agents_config['website_components_decider'],
			tools=[FileWriterTool()],
			verbose=True
		)
	
	@agent
	def frontend_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['frontend_developer'],
			tools=[input_file_read2, FileWriterTool()],
			verbose=True
		)
	
	@agent
	def invoker_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['invoker_agent'],
			tools=[input_file_read2, FileWriterTool()],
			verbose=True
		)
	
	@agent
	def reviewer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['reviewer_agent'],
			tools=[code_search_tool, FileWriterTool()],
			verbose=True
		)



	"""TASKS"""
	@task
	def sdd_reading_task(self) -> Task:
		return Task(
			config=self.tasks_config['sdd_reading_task'],
		)
	
	@task
	def website_components_deciding_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_components_deciding_task'],
			output_file='components.txt',
		)
	
	@task
	def frontend_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['frontend_development_task'],
		)
	
	@task
	def invoking_task(self) -> Task:
		return Task(
			config=self.tasks_config['invoking_task'],
		)
	
	@task
	def reviewing_task(self) -> Task:
		return Task(
			config=self.tasks_config['reviewing_task'],
			output_file='review.txt',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Websitemaker crew"""

		return Crew(
			agents=[
				self.sdd_reader(),
				self.website_components_decider(),
				self.frontend_developer(),
				self.invoker_agent(),
				self.reviewer_agent(),
			],
			tasks=[
				self.sdd_reading_task(),
				self.website_components_deciding_task(),
				self.frontend_development_task(),
				self.invoking_task(),
				self.reviewing_task(),
			],
			process=Process.sequential,
			verbose=True,
		)
