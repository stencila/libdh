# library-template

This repository is a template for creating [Stencila][stencila-site]-compatible libraries.
We recommend using this template to anyone who would like to make their functions for data
manipulation available in Stencila. You can think of this template as a part of Stencila API.

1.  Please *do not fork this repository directly on GitHub.*
    Instead, please use GitHub's importer following [the instructions below](#creating-a-repository).

2.  Please *do your work in your repository's `master` branch*,
    the documentation for your library will be 
    automatically published as a website by GitHub from the `doc` folder.

3.  Once you are done, please also [let us know][email] 



## Creating a Repository

1.  Log in to GitHub.
    (If you do not have an account, you can quickly create one for free.)
    You must be logged in for the remaining steps to work.

2.  Go to [GitHub's importer][importer].

3.  Paste the url of this repo as the old repository to clone:
    <https://github.com/stencila/library-template>.

4.  Select the owner for your new repository.
    (This will probably be you, but may instead be an organization you belong to.)

5.  Choose a name for your library repository.
    For example, `lib-genomics`, `lib-ecology` and so on.

6.  Make sure the repository is public.

7.   You can now click "Begin Import".
    When the process is done,
    you will receive a message like
    "Importing complete! Your new repository apawlik/lib-genomics is ready."
    and you can go to the new repository by clicking on the name.

**Note:**
some people have had intermittent errors during the import process,
possibly because of the network timing out.
If you experience a problem, please re-try;
if the problem persists,
please [get in touch](#getting-and-giving-help).

## Using the template

1.  Go into your newly-created repository,
    which will be at `https://github.com/your_username/lib-domain`.
    For example,
    if your username is `apawlik`,
    the repository's URL will be `https://github.com/apawlik/lib-genomics`.

2.  
6.  Alternatively,
    if you are already familiar with Git,
    you can clone the repository to your desktop,
    write your functions and tests for them locally,
    and push your changes back to the repository.

    ~~~
    git clone https://github.com/your_username/lib-domain
    ~~~

    In order to view your changes once you are done editing,
    you must push to your GitHub repository:

    ~~~
    git push origin master
    ~~~





## Generating documentation in the `doc` folder


    go to the GitHub Pages URL for your workshop and preview your changes.
    In the example above, this is `https://apawlik.github.io/lib-genomics`.


## Getting and Giving Help

We are committed to offering a pleasant setup experience for our learners and organizers.
If you find bugs in our instructions,
or would like to suggest improvements,
please [file an issue][issues]
or [mail us][email].

