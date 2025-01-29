import subprocess

def run_terraform(command):
    """Run a Terraform command and print output"""
    print(f"Running terraform {command}...")
    process = subprocess.run(["terraform", command], capture_output=True, text=True)
    
    if process.returncode == 0:
        print(f"Successfully ran terraform {command}:\n")
        print(process.stdout)
        return True
    else:
        print(f"Error running terraform {command}:\n")
        print(process.stderr)
        return False

def run_terraform_without_delay():
    """Run terraform init, validate, plan, apply without delay and user confirmations"""
    
    # Run terraform init
    if run_terraform("init"):
        proceed = input("Terraform init completed. Do you want to proceed with terraform validate? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Exiting the process.")
            return

    # Run terraform validate
    if run_terraform("validate"):
        proceed = input("Terraform validate completed. Do you want to proceed with terraform plan? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Exiting the process.")
            return

    # Run terraform plan
    if run_terraform("plan"):
        proceed = input("Terraform plan completed. Do you want to apply the changes to EC2? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Exiting the process.")
            return

        # Run terraform apply for EC2 only
        print("Applying changes for EC2...")
        run_terraform("apply -target=aws_instance.this -auto-approve")

if __name__ == "__main__":
    run_terraform_without_delay()
