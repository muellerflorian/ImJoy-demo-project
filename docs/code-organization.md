# Organise your code
To get started, we created the project folder called `ImJoy-demo-project`

Below we show how this folder was populated during the development described
in this tutorial. It contains files and folders for GitHub, the documentation,
and the actual Python and ImJoy code.

This might look daunting at the beginning, but we will explain in detail
all steps that eventually results in this organisation.



!!! note "<a href="https://github.com/muellerflorian/ImJoy-demo-project" target="_blank"> ImJoy-demo-project</a>"
      ```
      .
      ├─ dev/                        # Step 4: Folder containing code for development
      │  ├─ dev-calc-sine.ipynb        # Jupyter notebook
      │
      ├─ docs/                        # Step 3: Folder containing documentation
      │  ├─ code-organization.md        # smFISH image (channel 1)
      │  ├─ img/                        # Folder containing images of docs
      │  │  ├─ screenshot....png        # Screenshot of plugin
      │
      ├─ imjoy-plugins/               # Step 5:Folder containing ImJoy plugins
      │  ├─ plugin1.imjoy.html          # ImJoy plugin 1
      │  ├─ plugin2.imjoy.html          # ImJoy plugin 2
      │
      ├─ imjoydemoproject/            # Step 4: Folder containing actual python code
      │  ├─ __init__.py                 # File needed for packacking of module
      │  ├─ outils.py                   # Module containing functions.
      │
      ├─ site/                        # Step 3: Folder web-site of documentation (auto created)
      │  ├─ ...
      │
      ├─ .gitignore                   # Step 2: File specifying files and folders that are ignored by git
      ├─ LICENCE                      # Step 6: Licence file
      ├─ manifest.imjoy               # Step 6: Manifest specifying ImJoy plugin repo
      ├─ mkdocs.yaml                  # Step 3: File defining how documentation is created
      ├─ ReadMe.md                    # Step 3: ReadMe file rendered on GitHub
      ├─ setup.py                     # Step 6: File specifying pip package
      ├─ update_manifest.js           # Step 6: Node script to generate ImJoy plugin repository
      .
      ```

  You can also find an empty template project
  "<a href="https://github.com/oeway/ImJoy-Project-Template" target="_blank"> here</a>"
