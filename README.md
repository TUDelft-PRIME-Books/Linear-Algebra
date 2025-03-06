# Linear Algebra

The book can be read at
https://prime.pages.ewi.tudelft.nl/openlabook

# Setup

Clone the repository:

```bash
git clone --recursive https://gitlab.ewi.tudelft.nl/prime/openlabook.git
```
Then install the packages:

```bash
pip install -r requirements.txt
```

# Usage

To run once and see the result:

```bash
jupyter-book build .
```

To run with local applets once:

```bash
BASE_URL=http://localhost:5173/applet/ jupyter-book build .
# Or some other port
```

To run the book with 'hot-reload':

```bash
watchexec -e py,md -- jupyter-book build --all .

# Or with local applets
watchexec -e py,md -- BASE_URL=http://localhost:5173/applet/ jupyter-book build .
jupyter-book build --all .
```