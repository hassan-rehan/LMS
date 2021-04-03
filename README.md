General objectives:
1. Allow searching of new books by using titles or authors
2. Keep track of the current status of the book whether available or not
3. Adding new members to library
4. Determine the exact location of the book

Specific objectives:
1. Recommend books to users based on their preference
2. Send notifications of book availability to users based on their preference

Implementation:
1. Expert systems (ESs), is a computer based system that simulate human behavior in terms of decision making by asking questions to users and use the answers as input that facilitate the decision making process.

2. The system has two main elements:
    a. knowledge base ( information used by human librarian experts to make decision) the knowledge base rule is formed of (If) phase for condition and (Then) phase for result
    b. Inference engine (simulation of human decision making)


# Initializing the project

First install the python 3.8 or 3.9 and then run following commands in cmd

1. For checking python version and it is successfully installed in previous step

python --version

2. For checking pip version and it is successfully installed.

pip --version
(Note: If pip is not manually installed with python installation, you have to manually download it)

After that run the following commands:
    pip install django
    pip install pillow
    pip install pandas
    pip install regex
    pip install sklearn
    pip install nltk
    pip intall tables (if command give error, try to install this package from whl file)
    python -m nltk.downloader stopwords

To run the project:
    1. Open cmd inside project folder and run the following command.
        python manage.py runserver

To create 1st superuser (admin), run the following command in cmd inside project folder
    python manage.py runserver
    