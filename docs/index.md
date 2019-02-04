# Overview

Here we describe the different steps when developing a Python plugin for ImJoy.

!!! question "What will be develop in the demo project?"
    We will implement a ImJoy plugin that uses the Python plugin engine to perform some
    calculations (a sine function with a user defined number of data-points).
    The results will then we plotted in the ImJoy interface. The code is hosted on GitHub,
    the plugin is explained in a dedicated documentation, and the plugin code will be
    distributed with a dedicated ImJoy link. This allows easy installation for the end user.

The scope of this tutorial is not to provide a complete guide for software engineering,
but to illustrate some of the important concepts to consider when developing
an ImJoy plugin from scratch. We will also cross-reference important section
of the ImJoy documentation and other resources, for further reading.

Throughout this tutorial, we will provide **code fragments**, but also **links
the complete files** for further inspection. To open the files, you can simply click
the indicated file-name on top of the notes.

!!! note "<a href="https://github.com/muellerflorian/ImJoy-demo-project/blob/master/pkgcode/outils.py#L21" target="_blank"> Click on the names indicated here to open the files.</a>"
    This will contain some code examples, screen shots or other relevant information.

**Disclaimer 1**: this is not intended to be a comprehensive introduction for software
development, but rather a hands-on tutorial to see the complete workflow for a
typical ImJoy plugin.

**Disclaimer 2**: a number of different tools exist for the different steps presented
here. We focus on tools that are widely used and easily accessible.

**Disclaimer 3**: the implemented computational task is intentionally kept
very simply to allow focusing on the actual workflow and the different elements.
