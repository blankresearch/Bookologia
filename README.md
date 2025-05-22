# Bookologia

Bookologia is a specialized search engine that provides you access to any book pdf, within seconds.

![Home](./img/1-welcome-page.png)

## Why Bookologia?

Books today are solely used by white-collar professionals, whose job demands access to a technical literature, weither it's accounting or engineering. The people who read books for entertainment and recreation constitutes the minority. 

Yet, as vast as the internet, the projects that targets professionals who requires access, recommendation and organization of books for work are few if not inexistent. This is where Bookologia comes to the picture. 

Bookologia is a specialized version of Google/DuckDuckGo, that focuses only on books. Those are the links we index, and provide access to, and since we deal only with books, presenting them in a pleasing and aesthetic matter is within our reach. 

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

To install and run Bookologia, ensure you have Python installed on your system.

1. Clone the repository:

   ```sh
   git clone https://github.com/blankresearch/bookologia.git
   cd bookologia
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run bookologia:
   ```sh
   ./start.sh
   ```

4. Stop bookologia:
   ```sh
   ./start.sh
   ```

The app will start running locally, allowing you to access it via your browser.

## Running with Docker

Alternatively, you can run Memory using Docker.

1. Build the Docker image:

   ```sh
   docker build -t memory .
   ```

2. Run the Docker container:

   ```sh
   docker run -p 5000:5000 memory
   ```

Now, the app is running inside Docker, and you can access it at:

```sh
http://localhost:5000
```

or

```sh
http://127.0.0.1:5000

```

## Contributing

Memory is open-source, and contributions are welcome. If you have ideas or improvements, feel free to submit a pull request.

## Connect

For feedback or contributions, reach out to me:

- [LinkedIn](https://www.linkedin.com/in/yousbot/)
- [GitHub](https://github.com/yousboot)

Made with ❤️ by Youssef.

```

```