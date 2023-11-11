FROM python:alpine

# Set work directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Set environment variables (set these values when running the container)
ENV OPENAI_KEY=your_openai_key_here
ENV TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
ENV TELEGRAM_CHANNEL=@your_telegram_channel_here

# Run the application
CMD [ "python", "./app.py" ]
