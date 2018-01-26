# library-template

This repository is a template for creating [Stencila][stencila-site]-compatible libraries.
We recommend using this template to anyone who would like to make their functions for data
manipulation available in Stencila. You can think of this template as a part of Stencila API.

1.  Please *do not fork this repository directly on GitHub.*
    Instead, please use GitHub's importer following [the instructions below](#creating-your-repository).

2.  Please *do your work in your repository's `master` branch*,
    the documentation for your library will be 
    automatically published as a website by GitHub from the `doc` folder.

3.  Once you are done, please also [let us know][contact] 



## Creating Your Repository

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

**Adding your libraries directly via GitHub interface**

1.  Go into your newly-created repository,
    which will be at `https://github.com/your_username/lib-domain`.
    For example,
    if your username is `apawlik`,
    the repository's URL will be `https://github.com/apawlik/lib-genomics`.

2.  Have a look into the `function` subdirectory. It contains templates for
functions in different languages (`function.R`, `function,py`, `function.js` and so on).
Pick the template for the language your libraries are written in. Copy the contents of the template.

3. In the top right click the button "Create new file". This will open the editor on your screen.
Paste in the contents you copied from the template in. You need to give the file you created a name -
you will see the small text box at the top of the editor. Please provide a meaningful name such as:
`pearson.R` or `extract_counts.py` (note that you need to provide the correct extension!).

4. To write tests for your function, go to the `function` subdirectory. It contains templates for
function tests in different languages (`function-test.R`, `function-test,py`, `function-test.js` and so on).
Pick the relevant template and copy its contents.

5. In the top right click the button "Create new file". This will open the editor on your screen.
Paste in the contents you copied from the test template in. You need to give the file you created a name -
you will see the small text box at the top of the editor. Please provide a meaningful name such as:
`test_pearson.R` or `test_extract_counts.py` (note that you need to provide the correct extension!).

**Adding your libraries in local repository**
If you are already familiar with Git,
you can clone the repository to your desktop: 

```
 git clone https://github.com/your_username/lib-domain
```

write your functions and tests locally, and push your changes back to the repository you imported.

```
 git push origin master
```
    
 You can also create documentation automatically (in the `doc` folder) running the script on your machine.
 Please see the details below.


## Generating documentation in the `doc` folder

You can preview your changes in your GitHub pages which would be: `https://your_username.github.io/lib-domain`
In the example above, this is `https://apawlik.github.io/lib-genomics`.


## Getting and Giving Help

We are committed to offering a pleasant setup experience for our learners and organizers.
If you find bugs in our instructions,
or would like to suggest improvements,
please [file an issue][issues]
or [mail us][email].

[contact]: mailto:hello@stenci.la
[conduct]: https://github.com/stencila/policies/blob/master/CONDUCT.md
[community-forum]: https://github.com/stencila/libcore/blob/master/docs/community.stenci.la
[github]: http://github.com
[importer]: https://github.com/new/import
[issues]: https://help.github.com/articles/creating-an-issue/
[how-contribute]: https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github
[stencila-site]: http://stenci.la/
[stencila-repo]: https://github.com/stencila/stencila
[stencila-twitter]: https://twitter.com/stencila
[stencila-gitter]: https://gitter.im/stencila/stencila/
[markdown]: https://daringfireball.net/projects/markdown
[libcore-contribute]: https://github.com/stencila/libcore/blob/master/CONTRIBUTING.md
[libraries-contribute]: computation/functions.md#domain-specific-libraries
[new-functions]: computation/functions.md#adding-new-functions
[node-contribute]: https://github.com/stencila/node/CONTRIBUTING.md
[desktop-contribute]: https://github.com/stencila/desktop/blob/master/CONTRIBUTING.md
[cli-contribute]: https://github.com/stencila/cli/CONTRIBUTING.md
[hub-contribute]: https://github.com/stencila/hub/CONTRIBUTING.md
[cloud-contribute]: https://github.com/stencila/cloud/CONTRIBUTING.md
[images-contribute]: https://github.com/stencila/images/CONTRIBUTING.md
