# dev_animalsbot
DEV - Animals bot


build:
docker build -t img_name .

run:
docker run -d --env OPENAI_KEY=your_openai_key --env TELEGRAM_BOT_TOKEN=your_telegram_bot_token --env TELEGRAM_CHANNEL=@your_telegram_channel your_image_name
