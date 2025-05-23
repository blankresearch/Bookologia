# Bookologia

Bookologia is a specialized search engine, to find any book within seconds. 
It is open source, and can be self-hosted easily on Docker.

![welcome](./img/1-welcome-page.png)

See all screenshots and details at : [http://www.blankresearch.com/Bookologia/](http://www.blankresearch.com/Bookologia/) 

## Why Bookologia?

We believe there was a misunderstanding of the book market online, and a proof of that, none of the book platforms in the last 20 years were successful. They were shaped around the idea that people would read books and talk about them with others. Yet, every time a new project was launched, it was met with an insufficient market for growth.

That is because they targeted the wrong audience. People who read books for entertainment, are not the ones who search for them. The people who search for books are called: Knowledge workers. Engineers, doctors, lawyers, marketers... they use bits of information from here and there to find solutions to problems they have in hand. Most of the books they deal with are technical and specialized. They do not read the books, they browse them.

In such a market, you cannot simply sell books, yet these people are the total majority of those consuming them. Hence why profitability in this market is not possible, and only a public library model would work. 

## Features

- Simple UI with no unnecessary buttons—just press `<enter>` to submit.
- Search millions of books by "Title".
- Create collections and manage collections.
- Like books, to inform the recommendation system of your taste.
- General recommended books based on user likes/collections.
- Recommendation of similar books, more books written by the author, more editions of the same book.
- Links to any book, labeled "pdf" or "not pdf".

And for advanced users : 
- Scraping engine to collect books metadata from GoodReads, using one command. 

## Installation

There are 2 ways to host Bookologia locally: through Docker or manually. 

### Docker Deployment

   ```sh
   wget https://raw.githubusercontent.com/blankresearch/Bookologia/refs/heads/main/docker-compose.yml 
   docker compose up
   ```

### Manual Deployment


1. Host Elastic Search database on Docker 

   ```sh
   docker run -d --name bookologia-es -p 9200:9200 \ 
      -e discovery.type=single-node \ 
      -e xpack.security.enabled=false \ 
      yousb0t/bookologia-elastic
   ```

2. Download and run backend application
   ```sh
   git clone https://github.com/blankresearch/Bookologia.git
   cd Bookologia 
   pyenv install 3.10.7  
   pyenv local 3.10.7  
   python -m venv venv && source venv/bin/activate && pip install -r requirements.txt 
   cd Backend 
   python app.py &
   ```

The app will start running locally, allowing you to access it via your browser at : http://localhost:5001 or http://127.0.0.1:5001


## Contributing

The project is currently on hold from future development, but fixes will be made.

## Connect

For feedback or contributions, reach out to me:

- [LinkedIn](https://www.linkedin.com/in/yousbot/)
- [GitHub](https://github.com/yousbot)
- [Blank Research page](https://blankresearch.com/)

Made with ❤️ by Youssef.

```

```