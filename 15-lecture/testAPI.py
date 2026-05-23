

import os

from dotenv import load_dotenv

 

# Load environment variables from the .env file

load_dotenv()

 

def get_api_key(key_name):

    """

    Retrieve an API key from environment variables by its name.

 

    Args:

        key_name (str): The name of the environment variable.

 

    Returns:

        str or None: The API key if found, else None.

    """

    try:

        key = os.getenv(key_name)

        if key:

            print(f"{key_name} loaded successfully.")

        else:

            print(f"{key_name} not found. Please check your .env file.")

        return key

    except Exception as error:

        print(f"Something went wrong while loading {key_name}: {error}")

        return None

 

# Editable section: Add your API key environment variable names here

openai_api_key = get_api_key("OPENAI_API_KEY")