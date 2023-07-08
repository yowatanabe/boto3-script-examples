# Stop all EC2s that are running.
import boto3

ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    if instance.state["Name"] == "running":
        instance.stop()
        print(f"Stopped instance: {instance.id}")
