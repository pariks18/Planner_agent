from planner_agent.core.planner_agent import PlannerAgent

if __name__ == "__main__":
    agent = PlannerAgent()

    print("=== Permit Requirements ===")
    print(agent.plan("PERMIT_MANAGER", "Permit Requirements"))

    print("\n=== Site Preparation ===")
    print(agent.plan("SITE_ENGINEER", "Site Preparation"))