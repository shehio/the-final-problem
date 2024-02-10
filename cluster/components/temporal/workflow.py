from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import dummy_activity

@workflow.defn
class DummyWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            dummy_activity,
            name,
            schedule_to_close_timeout=timedelta(seconds=5),
        )
