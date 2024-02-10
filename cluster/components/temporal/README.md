curl -sSf https://temporal.download/cli.sh | sh
export PATH="\$PATH:/home/shehio/.temporalio/bin" >> ~/.bashrc

temporal workflow start  --task-queue default-task-queue  --type DummyWorkflow  --input '"World"'  --namespace default