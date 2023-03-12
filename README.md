# multiverse-devops-assessment-2
Repository containing technical requirements for DevOps assessment 2. Below are instructions for running the application & tests.  

## Running python-survey-app

## Running Automated Tests

1. In bash activate the python-survey-app folder with
  
```(bash)
cd python-survey-app
```

2. In bash enter

```(bash)
pytest
```

3. To run a coverage report enter

```(bash)
pytest --cov
```

## Docker Instructions

Below are instructions for setting up and using Docker.
### Docker Terraform Tool

1. Build docker file

```(bash)
docker build --rm -t tf-tool -f tf-tool.Dockerfile .
```

2. Run container in terminal

```(bash)
docker run --rm -it --mount type=bind,target=//root/code,source=/"$(pwd)" tf-tool
```

3. Exit container

```(bash)
exit
```

## Terraform Terminal Commands

These commands should be entered into the tf-tool Docker container terminal.

1. Navigate to the terraform folder

```(bash)
cd code/terraform
```

```(bash)
terraform init
```

```(bash)
terraform plan
```