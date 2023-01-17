# Linear Algebra

The book can be read at
https://dbalague.pages.ewi.tudelft.nl/openlabook

## How to run

> ⚠️ This books runs on python ^3.10

```bash
pip install -U jupyter-book
pip install sphinx-proof sphinx-exercise
```

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
watchexec -e py,md -i temp.md -- 'echo -n a >> temp.md && jupyter-book build .'
```

## How to add an applet to an image

````
```{applet}
:url: lines_and_planes/normal_equation_plane_origin
:fig: Images/image_shown_in_print_version.svg
:name: name_that_is_used_to_refer_to_this_figure
:title: This title is shown when you full-screen the applet

A plane through the point $P$.
```
````

> ⚠️ It is not required to add the `base url` and `/applet`. This is handed with an environment variable name `BASE_URL`. The default base url is set to https://openla.ewi.tudelft.nl/applet/

## Parameters for an applet

Some parameters can be set for an applet. The url parameter is the only required; the rest is optional.

````bash
```{applet}
:url: lines_and_planes/normal_equation_plane_origin # Required url
:title: hello # a string that will be shown as the title of the applet when the aplet is in fullscreen mode
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
