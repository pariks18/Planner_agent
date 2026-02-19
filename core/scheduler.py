class Scheduler:
    def generate_schedule(self, tasks):
        return [{"task": task, "day": i + 1} for i, task in enumerate(tasks)]