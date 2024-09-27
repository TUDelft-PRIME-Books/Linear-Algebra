# Linear Algebra

The book can be read at
https://prime.pages.ewi.tudelft.nl/openlabook

# Setup

Clone the repository:

```bash
git clone --recursive https://gitlab.ewi.tudelft.nl/prime/openlabook.git
```

Or if the repository is already cloned, download the Grasple submodule like this:

```bash
git submodule init
git submodule update
```

&nbsp;

Then install the packages:

```bash
pip install -r requirements.txt
pip install sphinx-grasple/
```

(^ Don't forget the trailing slash)

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

## Applet directive

````md
```{applet}
:url: lines_and_planes/normal_equation_plane_origin
:fig: Images/image_shown_in_print_version.svg
:name: name_that_is_used_to_refer_to_this_figure
:title: This title is shown when you full-screen the applet

A plane through the point $P$.
```
````

> ⚠️ The `url` parameter should be the part of the URL after `/applet/`. So if the full URL is `https://openla.ewi.tudelft.nl/applet/lines_and_planes/normal_equation_plane_origin`, you should set the parameter to `lines_and_planes/normal_equation_plane_origin`.

## Parameters for an applet

Some parameters can be set for an applet. Only the `url`, `fig` and `name` parameters are required; the rest is optional. It is recommended to add a `status` to the applet, which can be `unreviewed`, `in-review` or `reviewed`.

````md
```{applet}
:url: lines_and_planes/normal_equation_plane_origin # Required url
:fig: Images/lines_and_planes/normal_equation_plane_origin.svg  # Image shown in print version
:status: reviewed # default is "unreviewed". Other options are "in-review" and "reviewed"
:name: Fig:InnerProduct:ProjectionVectorLine

A title that describes the applet
```
````

### Optional parameters

| Parameter                                                                                                                           | Description                                                                                  | Default      |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| `iframe`                                                                                                                            | This parameter is added by default and set to true for each applet in this book.             |
| \ Therefore, this parameter is not configurable for this book. When using an applet in different context will change the bahaviour. | false                                                                                        |
| `title`                                                                                                                             | A string that will be shown as the title of the applet when the applet is in fullscreen mode | ""           |
| `status`                                                                                                                            | The status of the applet. Can be `unreviewed`, `in-review` or `reviewed`                     | `unreviewed` |
| `width`                                                                                                                             | The width of the applet in pixels                                                            | 100%         |
| `height`                                                                                                                            | The height of the applet in pixels                                                           | 400px        |

### Control parameters

> [!WARNING]
> Work in progress

### 2D Specific parameters

> [!TIP]
> You should add split-\* before the parameter to make it apply to the right scene

| Parameter  | Description                                  | Default |
| ---------- | -------------------------------------------- | ------- |
| position2D | The position of the applet in the 2D plane   | 0,0     |
| zoom2D     | The zoom level of the applet in the 2D plane | 1       |

### 3D Specific parameters

> [!TIP]
> You should add split-\* before the parameter to make it apply to the right scene

| Parameter  | Description                                  | Default |
| ---------- | -------------------------------------------- | ------- |
| position3D | The position of the applet in the 3D plane   | 0,0,0   |
| zoom3D     | The zoom level of the applet in the 3D plane | 1       |
