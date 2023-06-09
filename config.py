from dotenv import dotenv_values

config = dotenv_values(".env")


# Add any other environment variable 
if __name__ == "__main__":
    print(config)
    url = config.get('DATABASE_URL')
    print(url)
