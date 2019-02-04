# Documentation

User manual are invaluable for the user to be able to correctly use the code.
A widely used format to write such documentations is Markdown, which is
plain text language that allows formatting of documents. A introduction to Markdown
can be found <a href="https://guides.github.com/features/mastering-markdown/" target="_blank">here</a>.

For instance, the segment below

```markdown
# Define a title
+ first bullet item
+ second bullet item

some `inline code fragment` and a [link to ImJoy](https://imjoy.io/#/)
```

will yield this text


!!! note "Output"
    # Define a title
    + first bullet item
    + second bullet item

    some `inline code fragment` and a [link to ImJoy](https://imjoy.io/#/)

As another example, see the Markdown file of this <a href="https://raw.githubusercontent.com/muellerflorian/ImJoy-demo-project/master/docs/documentation.md" target="_blank"> page</a>.

Documentation can be as simple as a `ReadMe.md` in the root directory that will be
rendered on the GitHub repository page. You can also add a Wiki, as explained
<a href="https://guides.github.com/features/wikis/" target="_blank"> here</a>.

You can also create **more advanced documentations**. Many excellent tools exist that
automatically create documentation from  set of markdown files. An easy tool to get
started is
<a href="https://www.mkdocs.org/" target="_blank">**MkDocs**</a>.
For example, we created this documentation with MkDocs.

### Installing MkDocs

If you already have Anaconda, it is easy to get started.

First, you have to install MkDocs. Open an Anaconda terminal and type

```bash
pip install mkdocs
```

We used a special theme,
<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank">**Material for MkDocs**</a>,
which can be installed with:

```bash
pip install mkdocs-material
```

This package allows to integrate a number of extensions, for advanced formatting
of the documentation, for more information see
<a href="https://squidfunk.github.io/mkdocs-material/extensions/admonition/" target="_blank">here</a>.

### Writing a documentation

To initialise the documentation, go to folder containing the project folder
(`ImJoy-demo-project` in our case). Open an Anaconda terminal and run

```bash
mkdocs new ImJoy-demo-project
```

This will then create two files:

-   Configuration file: `ImJoy-demo-project\mkdocs.yml`
-   Initialize the docs: `ImJoy-demo-project\docs\index.md`

With these two files, a first version of the documentation can already be generated.

MkDocs provides a developmental server that you can use to check on your computer
how the documentation web site will look like. For this, open an Anaconda terminal
in your project folder and run

```bash
mkdocs serve
```
The website will then be available at <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a>.


We invite you to consult the excellent documentations of
<a href="https://www.mkdocs.org/" target="_blank">MkDocs</a>
and
<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank">Material for MkDocs</a>
for more details.

### Deploying your documentation

Once the documentation is finished, you can build the website with

```bash
mkdocs build
```
This will build the static website containing the documentation, which is stored
in the newly created subfolder `site`. You can then automatically deploy this site
to  GitHub pages.

```bash
mkdocs gh-deploy --clean --force
```

This will create a separate branch `gh-pages` on your GitHub repository dedicated
to the documentation. GitHub will then automatically build the website with the
documentation for you. To obtain the URL, go the `Settings` and `GitHub Pages`.
The URL for this website is
<a href="https://muellerflorian.github.io/ImJoy-demo-project/" target="_blank">https://muellerflorian.github.io/ImJoy-demo-project/</a>.


Please note that each time you **update the documentation**, you have to perform these
steps to build and deploy your documentation.
