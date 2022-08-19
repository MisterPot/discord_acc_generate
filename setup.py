from setuptools import setup, find_packages


setup(
    version="1.0",
    name="discord_bot",
    install_requires=[
        "requests",
        "2captcha-python"
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": ["generate=discord_bot.entry_point:main"]
    }
)
