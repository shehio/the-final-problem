# AWS

### Prerequisite
Run Setup scripts.

### Create AWS Profile
Run `aws configure`.

### Alias the Account
- Change the name of `the-final-problem` inside of the `aliasing_aws.sh` script.
- Run `./aliasing_aws.sh`.

### Nuke all Resources
Enter the account id in nuke-config.yaml
Run `aws-nuke -c nuke-config.yaml --no-dry-run`.
Do you want to continue? Enter account alias to continue. >> Enter the alias.
