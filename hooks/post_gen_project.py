import os
import shutil


lisence = "{{cookiecutter.license}}"
jwt = "{{cookiecutter.use_jwt}}"
project_slug = "{{cookiecutter.project_slug}}"
pgadmin = "{{cookiecutter.pgadmin}}"

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if lisence == "None":
    delete_resource("LICENSE")
if jwt == "n":
    delete_resource(f"{project_slug}/authentication/")
    delete_resource(f"{project_slug}/users/")

if pgadmin == "n":  
    with open("docker-compose.dev.yml", "r") as f:
    	lines = f.readlines()
    with open("docker-compose.dev.yml", "w") as f:
    	for line in lines:
            if line.strip("\n") != "#nickname_to_delete":
            	f.write(line)


