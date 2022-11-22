Example Jupyter Book website using GitLab Pages.

Learn more about GitLab Pages at https://about.gitlab.com/stages-devops-lifecycle/pages/ and the official
documentation https://docs.gitlab.com/ce/user/project/pages/.

---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [GitLab CI](#gitlab-ci)
- [Building locally](#building-locally)
- [GitLab User or Group Pages](#gitlab-user-or-group-pages)
- [Did you fork this project?](#did-you-fork-this-project)
- [Troubleshooting](#troubleshooting)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## GitLab CI

This project's static Pages are built by [GitLab CI/CD][ci], following the steps
defined in [`.gitlab-ci.yml`](.gitlab-ci.yml):

```bash
# Full project: https://gitlab.com/pages/jupyterbook

stages:
  - build
  - deploy

jupyter-build:
  stage: build
  image: python:slim
  script:
    - pip install -U jupyter-book
    - jupyter-book clean .
    - jupyter-book build .
  artifacts:
    paths:
      - _build/

pages:
  stage: deploy
  image: busybox:latest
  script:
    - mv _build/html public
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. [Install JupyterLab](https://jupyter.org/install) JupyterLab
1. [Install Jupyter Book](https://jupyterbook.org/start/overview.html#install-jupyter-book)
1. Fork, clone or download this project
1. `cd jupyter-book-example` -- the repository contains already an example of a
   book's source files, as described at [Jupyter Book > Create your book’s source files](https://jupyterbook.org/start/create.html#create-your-books-source-files)
1. Work on it... see for example [Jupyter Book > Structure and organize your content](https://jupyterbook.org/basics/organize.html)
1. Make a commit
1. See the book published online at 

Read more at Jupyter Book's [Introduction](https://jupyterbook.org/intro.html).

## GitLab User or Group Pages

To use this project as your user/group website, you will need one additional
step: just rename your project to `namespace.gitlab.io`, where `namespace` is
your `username` or `groupname`. This can be done by navigating to your
project's **Settings**.

## Did you fork this project?

If you forked this project for your own use, please go to your project's
**Settings** and remove the forking relationship, which won't be necessary
unless you want to contribute back to the upstream project.

## Troubleshooting

1. CSS is missing! That means two things:

    Either that you have wrongly set up the CSS URL in your templates, or
    your static generator has a configuration option that needs to be explicitly
    set in order to serve static assets under a relative URL.

[ci]: https://about.gitlab.com/gitlab-ci/
[jupyter-book]: http://jupyterbook.org
[install]: https://jupyterbook.org/start/overview.html#install-jupyter-book
[documentation]: https://jupyterbook.org/intro.html

----

Forked from @NikosAlexandris -- Thank you @stingrayza
