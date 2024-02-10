import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import dummy_activity
from workflow import DummyWorkflow

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="default-task-queue",
        workflows=[DummyWorkflow],
        activities=[dummy_activity],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
