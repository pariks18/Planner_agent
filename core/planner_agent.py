from planner_agent.core.task_decomposer import TaskDecomposer
from planner_agent.core.dependency_manager import DependencyManager
from planner_agent.tools.resource_validator import ResourceValidator
from planner_agent.core.scheduler import Scheduler
from planner_agent.data.config import ROLE_GOAL_MAP


class PlannerAgent:

    def __init__(self):
        self.decomposer = TaskDecomposer()
        self.dep_manager = DependencyManager()
        self.validator = ResourceValidator()
        self.scheduler = Scheduler()

    def plan(self, role: str, goal: str):

        # Step 1: Role Authorization Check
        if goal not in ROLE_GOAL_MAP.get(role, []):
            raise PermissionError("Unauthorized role for this goal")

        # Step 2: Break goal into tasks
        tasks = self.decomposer.decompose(goal)

        max_iterations = 10  # NEW: Prevent infinite loop
        iteration = 0

        while iteration < max_iterations:
            iteration += 1

            ordered = self.dep_manager.order_tasks(tasks)

            invalid = []

            # FIXED: Properly unpack validation result
            for t in ordered:
                is_valid, details = self.validator.validate(t)

                if not is_valid:
                    invalid.append((t, details))

            # If no invalid tasks, break loop
            if not invalid:
                break

            # Move invalid tasks to end (simple retry strategy)
            for t, _ in invalid:
                ordered.remove(t)
                ordered.append(t)

            tasks = ordered

        else:
            raise Exception("Unable to resolve resource conflicts")

        return self.scheduler.generate_schedule(ordered)
