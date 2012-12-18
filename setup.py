from setuptools import setup, find_packages


setup(
    name = "django-WYMEditor",
    version = "0.1",
    packages = find_packages(),
    include_package_data = True,
    author = "Kevin Brolly",
    author_email = "kevin.brolly@gmail.com",
    description = "A Django application that allows you to use" \
            " WYMEditor in your forms and admin.",
    license = "MIT License",
    keywords = "django widget WYMEditor",
    platforms = ['any'],
    url = "https://github.com/KevinBrolly/django-WYMEditor",
)
