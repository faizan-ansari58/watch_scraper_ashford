import subprocess

def run_spider(spider_name, output_file):
    command = [
        "scrapy",
        "crawl",
        spider_name,
        "-o",
        output_file,
    ]
    subprocess.run(command)

if __name__ == "__main__":
    print("Choose a spider to run:")
    print("1. Men Watch Spider")
    print("2. Women Watch Spider")
    print("3. Both Spiders")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        output_file = 'men_watch_output.csv'
        run_spider("men_watch_spider", output_file)
    elif choice == "2":
        output_file = 'women_watch_output.csv'
        run_spider("women_watch_spider", output_file)
    elif choice == "3":
        men_output_file = 'men_watch_output.csv'
        women_output_file = 'women_watch_output.csv'
        run_spider("men_watch_spider", men_output_file)
        run_spider("women_watch_spider", women_output_file)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
