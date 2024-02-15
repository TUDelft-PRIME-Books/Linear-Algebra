# Linear Algebra

The book can be read at
https://prime.pages.ewi.tudelft.nl/openlabook

# Setup

Clone the repository:

```bash
git clone --recursive https://gitlab.ewi.tudelft.nl/prime/openlabook.git
```

Or if the repository is already cloned, download the grasple submodule like this:

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
BASE_URL=http://localhost:3000/applet/ jupyter-book build .
# Or some other port
```

To run the book with 'hot-reload':

```bash
watchexec -e py,md -- jupyter-book build --all .
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

Some parameters can be set for an applet. Only the `url` and `fig` parameters are required; the rest is optional.

````md
```{applet}
:url: lines_and_planes/normal_equation_plane_origin # Required url
:fig: Images/lines_and_planes/normal_equation_plane_origin.svg  # Image shown in print version
:title: hello # a string that will be shown as the title of the applet when the aplet is in fullscreen mode
:status: reviewed # default is "unreviewed". Other options are "in-review" and "reviewed"
:width: 100% # the width of the applet
:height: 500px # the height of the applet
:background: #ffffff # the background color of the applet
:autoPlay: enabled # if the applet should start playing automatically
:isPerspectiveCamera: disabled # if the camera should be a perspective or orthographic camera
:position: 1,1,1 # the position of the camera related to the origin. Spaces not allowed
:enablePan: disabled # if the user can pan the camera (right mouse drag on desktop, two finger drag on mobile)
:distance: 30 # the distance of the camera from the origin for a *perspective* camera. Distance is a linear value, *higher* is further away.
:zoom: 30 # the distance of the camera from the origin for a *orthographic* camera. Zoom is a logarithmic value, *lower* is further away.
```
````
