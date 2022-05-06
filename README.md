## Instructions for cloning and deploying a docker container

Clone the repository: 
```
git clone https://github.com/Kirastel/bewise.git && cd bewise
```
Create a virtual environment: 
```
python3 -m venv venv
```
Activate the virtual environment: 
```
source venv/bin/activate
```

Create a image:
```
docker buld .
```

Build a new image and run two containers:
```
docker-compose up -d --build
```
Run the migration:

```
docker-compose exec web python manage.py migrate --noinput
```
From now local version is available at:

```http://localhost:8000```

Main app:
```
http://localhost:8000/api/v1/question/
```
