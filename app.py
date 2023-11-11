import csv
import random
from openai import OpenAI
import requests
from PIL import Image, ImageDraw, ImageFont
import datetime
import telebot
import time
import os


def generate_dalle_prompt(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Transpose the data to get columns as lists
    columns = list(zip(*data))

    # Randomly select an animal, action, and location
    animal = random.choice([item for item in columns[0] if item])
    action = random.choice([item for item in columns[1] if item])
    location = random.choice([item for item in columns[2] if item])

    # Construct the DALL-E prompt
    prompt = f"a {animal} unexpectedly captured {action} in the {location}. " \
             "The perspective is from a grainy, blurry trail camera, adding a sense of the animal being " \
             "photographed doing something unusual and secretive. The {location} environment forms the backdrop " \
             "of this candid scene."

    return prompt


def generate_and_save_image(prompt, openai_key):
    client = OpenAI(api_key=openai_key)

    try:
        # Generate image URL from DALL-E 3
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url

        # Download and save the image as 'image.jpg', overwriting if it exists
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            filename = 'image.jpg'
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved as {filename}")
            return True
        else:
            print("Failed to download the image")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def add_datestamp_and_direction(input_image_path, output_path):
    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.truetype("pixelify.ttf", size=25)
    text = "NATURE'S HIDDEN MOMENTS - " + datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + " - TRAILCAM FACING " + random.choice(
        ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'SOUTHWEST'])

    # Position text at the bottom
    text_x_position = 10
    text_y_position = height - 35

    # Create the rectangle and text
    draw.rectangle([0, text_y_position - 5, width, height], fill="black")  # Adjust the Y position as needed
    draw.text((text_x_position, text_y_position), text, fill="white", font=font)
    image.save(output_path)
    return True


def post_image_to_telegram_channel(image_path, channel_url, bot_token):
    bot = telebot.TeleBot(bot_token)
    try:
        with open(image_path, 'rb') as photo:
            bot.send_photo(channel_url, photo)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        # Set your API keys and channel url
        openai_key = os.getenv('OPENAI_KEY')
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        channel_url = os.getenv('TELEGRAM_CHANNEL')

        # Generate prompt
        prompt = generate_dalle_prompt('prompt.csv')

        # Generate and save image
        if generate_and_save_image(prompt, openai_key):
            # Overlay the image
            if add_datestamp_and_direction("image.jpg", "image.jpg"):
                # Post the image
                post_image_to_telegram_channel("image.jpg", channel_url, bot_token)

        # Wait for 12 hours
        time.sleep(43200)  # 12 hours in seconds


if __name__ == "__main__":
    main()
