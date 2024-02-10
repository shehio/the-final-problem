from temporalio import activity

@activity.defn
async def dummy_activity(name) -> str:
    return f"Hello {name}!"
