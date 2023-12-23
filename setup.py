from cx_Freeze import setup, Executable

setup(
    name="watch_scraper",
    version="1.0",
    description="Description of your project",
    executables=[Executable("watch_scraper.py")],
)
