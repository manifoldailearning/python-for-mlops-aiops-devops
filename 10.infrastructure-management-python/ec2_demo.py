import pulumi
import pulumi_aws as aws

# Select the latest Amazon Linux AMI in the current region
ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[aws.ec2.GetAmiFilterArgs(
        name="name",
        values=["amzn2-ami-hvm-*-x86_64-ebs"]
    )]
)

# Create a Security Group that permits HTTP ingress and all egress
security_group = aws.ec2.SecurityGroup('web-server-sg',
    description='Enable HTTP access',
    egress=[aws.ec2.SecurityGroupEgressArgs(
        protocol='-1',
        from_port=0,
        to_port=0,
        cidr_blocks=['0.0.0.0/0'],
    )],
    ingress=[aws.ec2.SecurityGroupIngressArgs(
        protocol='tcp',
        from_port=80,
        to_port=80,
        cidr_blocks=['0.0.0.0/0'],
    )]
)

# Create an EC2 instance
web_server_instance = aws.ec2.Instance('web-server-instance',
    instance_type='t2.micro',
    ami=ami.id,
    associate_public_ip_address=True,
    vpc_security_group_ids=[security_group.id],
    user_data="""#!/bin/bash
echo 'Hello, World from Manifold AI Learning' > index.html
nohup python -m SimpleHTTPServer 80 &
""",
    tags={
        'Name': 'web-server-instance'
    }
)

# Export the public IP to access the web server
pulumi.export('public_ip', web_server_instance.public_ip)
