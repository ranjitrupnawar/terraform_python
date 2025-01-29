provider "aws" {
  region = "us-east-1"
}

module "ec2" {
  source         = "./modules/ec2"
  ami_id         = "ami-0c55b159cbfafe1f0"
  instance_type  = "t2.micro"
  instance_name  = "TerraformInstance"
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = "my-terraform-s3-bucket"
}
