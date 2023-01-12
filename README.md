# Linear Algebra

The book can be read at
https://dbalague.pages.ewi.tudelft.nl/openlabook

## How to add an applet to an image

Add `:class: applet-print-figure` to an image to have it only show up when the parapraph is printed. Prepend the image with an applet and give the applet the desired url. It should look something like:

````
```{applet}
:url: lines_and_planes/normal_equation_plane_origin
```


```{figure} Images/Fig-LinesAndPlanes-NormalEquationPlane.svg
:name: Fig:LinesAndPlanes:NormalEquationPlane
:class: applet-print-figure

A plane through the point $P$.
```
````

> ⚠️ It is not required to add the `base url` and `/applet`. This is handed with an environment variable name `BASE_URL`. The default base url is set to https://openla.ewi.tudelft.nl/applet/
