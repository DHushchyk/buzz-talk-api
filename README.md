# Buzz Talk API

[API link](http://buzz-talk-api.eu-west-3.elasticbeanstalk.com/)


## Installation

1. Clone the project repository:

```bash
git clone https://github.com/DHushchyk/buzz-talk-api.git
```

2. Navigate to the project directory:

```bash
cd buzz_talk_api
```

3. Create a virtual environment for the project:

```bash
python -m venv env
```

4. Activate the virtual environment:

```bash
source env/bin/activate
```

5. Install the project dependencies:

```bash
pip install -r requirements.txt
```

6. Create database.
7. Run database migrations:

```bash
python manage.py migrate
```

8. Start the development server:

```bash
python manage.py runserver
```