# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import glob
import hashlib
import os
from typing import Dict, List

from packaging.version import parse

import linearmodels

# -- Project information -----------------------------------------------------

project = "linearmodels"
copyright = "2021, Kevin Sheppard"
author = "Kevin Sheppard"

# More warnings
nitpicky = True

# The short X.Y version
full_version = parse(linearmodels.__version__)
short_version = version = linearmodels.__version__
if full_version.is_devrelease:
    release = f"v{full_version.base_version} (+{full_version.dev})"
else:
    release = short_version

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.githubpages",
    # "numpydoc",
    # "sphinx_autodoc_typehints",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "nbsphinx",
    "sphinx_immaterial",
]

try:
    import sphinxcontrib.spelling  # noqa: F401
except ImportError as err:  # noqa: F841
    pass
else:
    extensions.append("sphinxcontrib.spelling")

spelling_word_list_filename = ["spelling_wordlist.txt", "names_wordlist.txt"]
spelling_ignore_pypi_package_names = True

suppress_warnings = ["ref.citation"]

# TODO: Check this
# add_module_names = False

# Copy over notebooks from examples to docs for build
files = glob.glob("../../examples/*.ipynb") + glob.glob("../../examples/*.png")
for file_to_copy in files:
    full_name = os.path.split(file_to_copy)[-1]
    folder, file_name = full_name.split("_")
    if not file_name.endswith("ipynb"):
        file_name = "_".join((folder, file_name))
    out_dir = os.path.join(folder, "examples")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, file_name)
    existing_hash = ""
    with open(file_to_copy, "rb") as example:
        example_file = example.read()
        example_hash = hashlib.sha512(example_file).hexdigest()
    if os.path.exists(out_file):
        with open(out_file, "rb") as existing:
            existing_hash = hashlib.sha512(existing.read()).hexdigest()
    if existing_hash != example_hash:
        print(f"Copying {file_to_copy} to {out_file}")
        with open(out_file, "wb") as out:
            out.write(example_file)

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = [".rst", ".md"]
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns: list[str] = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "colorful"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Adds an HTML table visitor to apply Bootstrap table classes
html_theme = "sphinx_immaterial"
html_title = f"{project} {release}"

# sphinx_immaterial theme options
html_theme_options = {
    "icon": {"repo": "fontawesome/brands/github"},
    "site_url": "https://bashtage.github.io/linearmodels/",
    "repo_url": "https://github.com/bashtage/linearmodels/",
    "repo_name": "linearmodels",
    "palette": {"primary": "blue", "accent": "orange"},
    "globaltoc_collapse": True,
    "toc_title": "Contents",
    "version_dropdown": True,
    "version_info": [
        {
            "version": "https://bashtage.github.io/linearmodels",
            "title": "Release",
            "aliases": [],
        },
        {
            "version": "https://bashtage.github.io/linearmodels/devel",
            "title": "Development",
            "aliases": [],
        },
    ],
    "toc_title_is_page_title": True,
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/bashtage/linearmodels",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/linearmodels/",
        },
        {
            "icon": "fontawesome/solid/quote-left",
            "link": "https://doi.org/10.5281/zenodo.2591973",
        },
    ],
}

html_favicon = "images/favicon.ico"
html_logo = "images/bw-logo.svg"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/small_fixes.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don"t match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``["localtoc.html", "relations.html", "sourcelink.html",
# "searchbox.html"]``.
#
# html_sidebars = {}
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "searchbox.html", "localtoc.html"]
}

# If false, no module index is generated.
html_domain_indices = True

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "linearmodels"

# -- Options for LaTeX output ------------------------------------------------
# latex_elements: dict[str, str] = {
# The paper size ("letterpaper" or "a4paper").
#
# "papersize": "letterpaper",
# The font size ("10pt", "11pt" or "12pt").
#
# "pointsize": "10pt",
# Additional stuff for the LaTeX preamble.
#
# "preamble": '',
# Latex figure (float) alignment
#
# "figure_align": "htbp",
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "linearmodels.tex",
        "linearmodels Documentation",
        "Kevin Sheppard",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "linearmodels", "linearmodels Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "linearmodels",
        "linearmodels Documentation",
        author,
        "linearmodels",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "statsmodels": ("https://www.statsmodels.org/dev/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "np": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pd": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
}

extlinks = {"issue": ("https://github.com/bashtage/linearmodels/issues/%s", "GH%s")}


doctest_global_setup = """
import numpy as np
import pandas as pd

entities = ['entity.{0}'.format(i) for i in range(100)]
time = list(range(10))
mi = pd.MultiIndex.from_product((entities,time), names=('entities','time'))
panel_data = pd.DataFrame(np.random.randn(1000,5), index=mi, columns=['y','x1','x2','x3','x4'])
y = panel_data.y
x = panel_data.x1
"""

napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_preprocess_types = True
napoleon_use_param = True
napoleon_type_aliases = {
    "array-like": ":term:`array-like <array_like>`",
    "array_like": ":term:`array_like`",
    "Figure": "matplotlib.figure.Figure",
    "Axes": "matplotlib.axes.Axes",
    "AxesSubplot": "matplotlib.axes.Axes",
    "DataFrame": "pandas.DataFrame",
    "Series": "pandas.Series",
    "BetweenOLS": "linearmodels.panel.model.BetweenOLS",
    "FamaMacBeth": "linearmodels.panel.model.FamaMacBeth",
    "FirstDifferenceOLS": "linearmodels.panel.model.FirstDifferenceOLS",
    "IV2SLS": "linearmodels.iv.model.IV2SLS",
    "IV3SLS": "linearmodels.system.model.IV3SLS",
    "IVGMM": "linearmodels.iv.model.IVGMM",
    "IVGMMCUE": "linearmodels.iv.model.IVGMMCUE",
    "IVLIML": "linearmodels.iv.model.IVLIML",
    "IVSystemGMM": "linearmodels.system.model.IVSystemGMM",
    "LinearFactorModel": "linearmodels.asset_pricing.model.LinearFactorModel",
    "LinearFactorModelGMM": "linearmodels.asset_pricing.model.LinearFactorModelGMM",
    "OLS": "linearmodels.iv.model.OLS",
    "PanelOLS": "linearmodels.panel.model.PanelOLS",
    "PooledOLS": "linearmodels.panel.model.PooledOLS",
    "RandomEffects": "linearmodels.panel.model.RandomEffects",
    "SUR": "linearmodels.system.model.SUR",
    "TradedFactorModel": "linearmodels.asset_pricing.model.TradedFactorModel",
    "AbsorbingLSResults": "linearmodels.iv.absorbing.AbsorbingLSResults",
    "FirstStageResults": "linearmodels.iv.results.FirstStageResults",
    "IVGMMResults": "linearmodels.iv.results.IVGMMResults",
    "IVModelComparison": "linearmodels.iv.results.IVModelComparison",
    "IVResults": "linearmodels.iv.results.IVResults",
    "InvalidTestStatistic": "linearmodels.shared.InvalidTestStatistic",
    "OLSResults": "linearmodels.iv.results.OLSResults",
    "WaldTestStatistic": "linearmodels.shared.hypotheses.WaldTestStatistic",
    "LinearConstraint": "linearmodels.system.model.LinearConstraint",
    "PanelEffectsResults": "linearmodels.panel.results.PanelEffectsResults",
    "PanelModelComparison": "linearmodels.panel.results.PanelModelComparison",
    "PanelResults": "linearmodels.panel.results.PanelResults",
    "RandomEffectsResults": "linearmodels.panel.results.RandomEffectsResults",
    "GMMSystemResults": "linearmodels.system.results.GMMSystemResults",
    "Summary": "linearmodels.compat.statsmodels.Summary",
    "SystemEquationResult": "linearmodels.system.results.SystemEquationResult",
    "SystemResults": "linearmodels.system.results.SystemResults",
    "GMMFactorModelResults": "linearmodels.asset_pricing.results.GMMFactorModelResults",
    "LinearFactorModelResults": "linearmodels.asset_pricing.results.LinearFactorModelResults",
    "PanelData": "linearmodels.panel.data.PanelData",
    "IVData": "linearmodels.iv.data.IVData",
    "AttrDict": "linearmodels.shared.utility.AttrDict",
    "csc_matrix": "scipy.sparse.csc_matrix",
    "DataArray": "xarray.DataArray",
    "PanelModelData": "linearmodels.panel.utility.PanelModelData",
    "ndarray": "numpy.ndarray",
    "np.ndarray": "numpy.array",
    "pd.Series": "pandas.Series",
}

# Create xrefs
numpydoc_use_autodoc_signature = True
numpydoc_xref_param_type = True
numpydoc_class_members_toctree = False
numpydoc_xref_aliases = {
    "Figure": "matplotlib.figure.Figure",
    "Axes": "matplotlib.axes.Axes",
    "AxesSubplot": "matplotlib.axes.Axes",
    "DataFrame": "pandas.DataFrame",
    "Series": "pandas.Series",
    "BetweenOLS": "linearmodels.panel.model.BetweenOLS",
    "FamaMacBeth": "linearmodels.panel.model.FamaMacBeth",
    "FirstDifferenceOLS": "linearmodels.panel.model.FirstDifferenceOLS",
    "IV2SLS": "linearmodels.iv.model.IV2SLS",
    "IV3SLS": "linearmodels.system.model.IV3SLS",
    "IVGMM": "linearmodels.iv.model.IVGMM",
    "IVGMMCUE": "linearmodels.iv.model.IVGMMCUE",
    "IVLIML": "linearmodels.iv.model.IVLIML",
    "IVSystemGMM": "linearmodels.system.model.IVSystemGMM",
    "LinearFactorModel": "linearmodels.asset_pricing.model.LinearFactorModel",
    "LinearFactorModelGMM": "linearmodels.asset_pricing.model.LinearFactorModelGMM",
    "OLS": "linearmodels.iv.model.OLS",
    "PanelOLS": "linearmodels.panel.model.PanelOLS",
    "PooledOLS": "linearmodels.panel.model.PooledOLS",
    "RandomEffects": "linearmodels.panel.model.RandomEffects",
    "SUR": "linearmodels.system.model.SUR",
    "TradedFactorModel": "linearmodels.asset_pricing.model.TradedFactorModel",
    "AbsorbingLSResults": "linearmodels.iv.absorbing.AbsorbingLSResults",
    "FirstStageResults": "linearmodels.iv.results.FirstStageResults",
    "IVGMMResults": "linearmodels.iv.results.IVGMMResults",
    "IVModelComparison": "linearmodels.iv.results.IVModelComparison",
    "IVResults": "linearmodels.iv.results.IVResults",
    "InvalidTestStatistic": "linearmodels.shared.InvalidTestStatistic",
    "OLSResults": "linearmodels.iv.results.OLSResults",
    "WaldTestStatistic": "linearmodels.shared.hypotheses.WaldTestStatistic",
    "LinearConstraint": "linearmodels.system.model.LinearConstraint",
    "PanelEffectsResults": "linearmodels.panel.results.PanelEffectsResults",
    "PanelModelComparison": "linearmodels.panel.results.PanelModelComparison",
    "PanelResults": "linearmodels.panel.results.PanelResults",
    "RandomEffectsResults": "linearmodels.panel.results.RandomEffectsResults",
    "GMMSystemResults": "linearmodels.system.results.GMMSystemResults",
    "Summary": "linearmodels.compat.statsmodels.Summary",
    "SystemEquationResult": "linearmodels.system.results.SystemEquationResult",
    "SystemResults": "linearmodels.system.results.SystemResults",
    "GMMFactorModelResults": "linearmodels.asset_pricing.results.GMMFactorModelResults",
    "LinearFactorModelResults": "linearmodels.asset_pricing.results.LinearFactorModelResults",
    "PanelData": "linearmodels.panel.data.PanelData",
    "IVData": "linearmodels.iv.data.IVData",
    "AttrDict": "linearmodels.shared.utility.AttrDict",
    "csc_matrix": "scipy.sparse.csc_matrix",
    "DataArray": "xarray.DataArray",
    "PanelModelData": "linearmodels.panel.utility.PanelModelData",
    "ndarray": "numpy.ndarray",
    "np.ndarray": "numpy.array",
    "pd.Series": "pandas.Series",
}

autosummary_generate = True
autoclass_content = "class"
