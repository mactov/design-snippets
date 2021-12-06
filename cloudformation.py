import boto3


class CloudFormation(object):
    def __init__(self, credentials, region):
        self.credentials = credentials
        self.region = region
        self.client = boto3.client('cloudformation', self.region)

    def deploy(self, stack_name, stack_template, stack_pamameters):
        pass

    def list_existing_stacks(self):
        return self.client.list_all_stacks()

    def stack_already_exists(self, stack_name):
        return stack_name in self.list_existing_stacks()

    def deploy(self, stack_name, stack_template, stack_pamameters):
        if self.stack_already_exists(stack_name):
            self.update_stack(stack_name, stack_template, stack_pamameters)
        else:
            self.create_stack(stack_name, stack_template, stack_pamameters)

    def update_stack(self, stack_name, stack_template, stack_pamameters):
        pass

    def create_stack(self, stack_name, stack_template, stack_pamameters):
        pass