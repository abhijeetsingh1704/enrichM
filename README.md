<p align="center">
<img src="logo/logo.png">
</p>

[![Build Status](https://travis-ci.com/geronimp/enrichM.svg?branch=master)](https://travis-ci.com/geronimp/enrichM)
[![version status](https://img.shields.io/pypi/v/enrichm.svg)](https://pypi.python.org/pypi/enrichm)

EnrichM is a set of comparative genomics tools for large sets of metagenome assembled genomes (MAGs). The current functionality includes:

1. A basic annotation pipeline for MAGs.
2. A pipeline to determine the metabolic pathways that are encoded by MAGs, using KEGG modules as a reference (although custom pathways can be specified)
3. A pipeline to identify genes or metabolic pathways that are enriched within and between user-defined groups of genomes (groups can be genomes that are related functionally, phylogenetically, recovered from different environments, etc).
4. To construct metabolic networks from annotated population genomes.
5. Construct random forest machine learning models from the functional composition of either MAGs, metagenomes or transcriptomes.
6. Apply these random forest machine learning models to classify new MAGs metagenomes.

EnrichM is under active development, so there is no guaratee that master is stable. It's recommended that EnrichM is downloaded either via pypi or conda (see below).

# Installation
## Dependencies
EnrichM is written in python 3, and required >v3.6 to run. EnrichM requires the following non-python dependencies:
* [hmmer](http://hmmer.org/) >= 3.1b
* [diamond](https://github.com/bbuchfink/diamond) == 0.9.22
* [prodigal](http://prodigal.ornl.gov/) >= 2.6.3
* [parallel](https://www.gnu.org/software/parallel/) >= 20180222
* [mmseqs](https://github.com/soedinglab/MMseqs2) >= 2-23394
* [R](https://www.r-project.org/) >= 3.0.1
* [mcl](https://micans.org/mcl/) >= 14-137

## PyPi
Install from PyPi like this:
```
sudo pip3 install enrichm
```

## conda (recommended)
Install the conda package like so:
```
# Create a python3 environment for EnrichM. Replace "X.X.X" with the EnrichM version number
conda create -c bioconda -n enrichm_X.X.X enrichm=X.X.X
```
After this, you'll need to set up EnrichM to run by downloading its back end databases.

# Setup
## Loading EnrichM's database
Before running EnrichM, you'll need to download the back-end database. This file is large (5.7G) and contains all the reference databases EnrichM needs to annotate and compare your genomes. This includes Pfam-A HMMs, TIGRfam HMMs, a DIAMOND database of the sequences in uniref100 with EC and KO annotations, and KoFamKOALA HMMs. By default the database will be installed in your home directory. This is done using a command in EnrichM:
```
enrichm data
```
This should take approximately 15 minutes. To check for updates and install updates, simply run the same command. You can uninstall the database, using:
```
enrichm data --uninstall
```

## Sepcifying the location of the EnrichM database
If you would like to store the EnrichM database outside of your home directory, move you need to tell EnrichM where to look. To do this, export a BASH variable named "ENRICHM_DB":

```
export ENRICHM_DB=/path/to/database/
```

After which EnrichM should be able to find the database. It may be worthwhile putting this in your .bashrc so you dont have to re-run it every time you open a terminal.

# Subcommands
## annotate
Annotate is a function that allows you to annotate your population genomes with [KO](http://www.kegg.jp/kegg/ko.html), [PFAM](http://pfam.xfam.org/), [TIGRFAM](http://www.jcvi.org/cgi-bin/tigrfams/index.cgi), and CAZY using [dbCAN](cys.bios.niu.edu/dbCAN2). The result will be a .gff file for each genome, and a frequency matrix for each annotation type where the rows are annotation IDs and the columns are genomes.

See the [annotate help page](https://github.com/geronimp/enrichM/wiki/annotate) for more

## classify
Classify quickly reads in KO annotations in the form of a matrix (KO IDs as rows, genomes as columns) and determines which [KEGG modules](http://www.kegg.jp/kegg/module.html) are complete. Annotation matrices can be generated using the annotate function.

See the [classify help page](https://github.com/geronimp/enrichM/wiki/classify) for more

## enrichment
Enrichment will read in KO or PFAM annotations in the form of a matrix (IDs as rows, genomes as columns) and a metadata file that separates genomes into groups to compare, and will run some basic stats to determine the enrichment of modules or pfam clans between and within the groups.

See the [enrichment help page](https://github.com/geronimp/enrichM/wiki/enrichment) for more

## pathway
Pathway reads in a KO matrix and generates a Cytoscape-readable metabolic network and metadata file. Only reactions that are possible given the KOs present in the input matrix are shown, and the modules and reactions that are included in the output can be customized.

See the [pathway help page](https://github.com/geronimp/enrichM/wiki/pathway) for more

## explore
Explore is similar to pathway, but rather than generating a specified pathway it will start from a given query compound ID, and explore the possible reactions that use that compound given the enzymes present in the input KO matrix.

See the [explore help page](https://github.com/geronimp/enrichM/wiki/explore) for more

# Contact
If you have any feedback about EnrichM, drop an email to the [SupportM](https://groups.google.com/forum/?hl=en#!forum/supportm) public help forum. Software by [Joel A. Boyd](https://ecogenomic.org/personnel/mr-joel-boyd) (@geronimp) at the Australian Centre for Ecogenomics (ACE).

# License
EnrichM is licensed under the GNU GPL v3+. See LICENSE.txt for further details.

# Contributing 
I want EnrichM to be as useful as possible, so please feel free to leave feature requests and bug reports.

# Citation
A manuscript is in the final stages of preparation and a bioRxiv pre-print will be up shortly. If you find EnrichM useful and use it in your work, please cite it as follows:
```
Comparative genomics using EnrichM. Joel A Boyd Ben J Woodcroft Gene W Tyson. 2019. In preparation.
```
