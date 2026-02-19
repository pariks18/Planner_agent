from planner_agent.llm.llm_interface import LLMInterface

class TaskDecomposer:

    def __init__(self):
        self.llm = LLMInterface()

    def decompose(self, goal):
        raw_output = self.llm.generate_tasks(goal)

        # Convert text into clean task list
        tasks = []
        for line in raw_output.split("\n"):
            line = line.strip()
            if line and line[0].isdigit():
                clean_task = line.split(".", 1)[1].strip()
                tasks.append(clean_task)

        return tasks
