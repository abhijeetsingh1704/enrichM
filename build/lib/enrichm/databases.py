#!/usr/bin/env python3
###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

# Imports
import os
import logging
import pickle
# Local
from enrichm.data import Data

###############################################################################

class Databases:

    if os.path.isfile(os.path.join(Data.DATABASE_DIR, 'VERSION')):
        DB_VERSION = open(os.path.join(Data.DATABASE_DIR, 'VERSION'))\
                                .readline()\
                                .strip()\
                                .replace('.tar.gz', '')
        CUR_DATABASE_DIR = os.path.join(Data.DATABASE_DIR, DB_VERSION)
        PICKLE_VERSION = open(os.path.join(CUR_DATABASE_DIR, 'VERSION')).readline().strip()
        OLD_DATABASE_PATH = os.path.join(Data.DATABASE_DIR, 'old')
        IDS_DIR = os.path.join(CUR_DATABASE_DIR, 'ids')
        REF_DIR = os.path.join(CUR_DATABASE_DIR, 'databases')
        GTDB_DIR = os.path.join(CUR_DATABASE_DIR, 'gtdb')
        KO_HMM_CUTOFFS = os.path.join(CUR_DATABASE_DIR, 'ko_cutoffs.tsv')

        PICKLE = 'pickle'
        HMM_SUFFIX = '.hmm'
        DMND_SUFFIX = '.dmnd'
        KO_DB_NAME = 'uniref100.KO'
        EC_DB_NAME = 'uniref100.EC'
        PFAM_DB_NAME = 'pfam'
        KO_HMM_DB_NAME = 'ko'
        TIGRFAM_DB_NAME = 'tigrfam'
        CAZY_DB_NAME = 'cazy'
        GTDB_DB_NAME = 'GTDB_R80_DB'

        GTDB_CAZY = os.path.join(GTDB_DIR, "gtdb_cazy.tsv")
        GTDB_KO = os.path.join(GTDB_DIR, "gtdb_ko.tsv")
        GTDB_PFAM = os.path.join(GTDB_DIR, "gtdb_pfam.tsv")
        GTDB_TIGRFAM = os.path.join(GTDB_DIR, "gtdb_tigrfam.tsv")
        GTDB_EC = os.path.join(GTDB_DIR, "gtdb_ec.tsv")

        TAXONOMY = os.path.join(CUR_DATABASE_DIR, 'taxonomy_gtdb.tsv')
        M2DEF = os.path.join(CUR_DATABASE_DIR, 'module_to_definition')
        M = os.path.join(CUR_DATABASE_DIR, 'module_descriptions')
        COMPOUND_DESC = os.path.join(CUR_DATABASE_DIR, 'br08001')
        R2K = os.path.join(CUR_DATABASE_DIR, 'reaction_to_orthology')
        R2C = os.path.join(CUR_DATABASE_DIR, 'reaction_to_compound')
        R2M = os.path.join(CUR_DATABASE_DIR, 'reaction_to_module')
        M2R = os.path.join(CUR_DATABASE_DIR, 'module_to_reaction')
        M2C = os.path.join(CUR_DATABASE_DIR, 'module_to_cpd')
        R2P = os.path.join(CUR_DATABASE_DIR, 'reaction_to_pathway')
        P2R = os.path.join(CUR_DATABASE_DIR, 'pathway_to_reaction')
        C2R = os.path.join(CUR_DATABASE_DIR, 'compound_to_reaction')
        C = os.path.join(CUR_DATABASE_DIR, 'compound_descriptions')
        R = os.path.join(CUR_DATABASE_DIR, 'reaction_descriptions')
        P = os.path.join(CUR_DATABASE_DIR, 'pathway_descriptions')
        K = os.path.join(CUR_DATABASE_DIR, 'ko_descriptions')

        PFAM2CLAN = os.path.join(CUR_DATABASE_DIR, 'pfam_to_clan')
        CLAN2NAME = os.path.join(CUR_DATABASE_DIR, 'clan_to_name')
        PFAM2NAME = os.path.join(CUR_DATABASE_DIR, 'pfam_to_name')
        PFAM2DESCRIPTION = os.path.join(CUR_DATABASE_DIR, 'pfam_to_description')
        EC2DESCRIPTION = os.path.join(CUR_DATABASE_DIR, 'ec_to_description')
        TIGRFAM2DESCRIPTION = os.path.join(CUR_DATABASE_DIR, 'tigrfam_descriptions')
        CLAN2PFAM = os.path.join(CUR_DATABASE_DIR, 'clan_to_pfam')

    def __init__(self):

        self.signature_modules = set(['M00611', 'M00612', 'M00613', 'M00614',
                                      'M00617', 'M00618', 'M00615', 'M00616',
                                      'M00363', 'M00542', 'M00574', 'M00575',
                                      'M00564', 'M00660', 'M00664', 'M00625',
                                      'M00627', 'M00745', 'M00651', 'M00652',
                                      'M00704', 'M00725', 'M00726', 'M00730',
                                      'M00744', 'M00718', 'M00639', 'M00641',
                                      'M00642', 'M00643', 'M00769', 'M00649',
                                      'M00696', 'M00697', 'M00698', 'M00700',
                                      'M00702', 'M00714', 'M00705', 'M00746'])

        self.KO_DB = os.path.join(self.REF_DIR, self.KO_DB_NAME + self.DMND_SUFFIX)
        self.EC_DB = os.path.join(self.REF_DIR, self.EC_DB_NAME + self.DMND_SUFFIX)
        self.GTDB_DB = os.path.join(self.REF_DIR, self.GTDB_DB_NAME)

        self.PFAM_DB = os.path.join(self.REF_DIR, self.PFAM_DB_NAME + self.HMM_SUFFIX)
        self.KO_HMM_DB = os.path.join(self.REF_DIR, self.KO_HMM_DB_NAME + self.HMM_SUFFIX)
        self.TIGRFAM_DB = os.path.join(self.REF_DIR, self.TIGRFAM_DB_NAME + self.HMM_SUFFIX)
        self.CAZY_DB = os.path.join(self.REF_DIR, self.CAZY_DB_NAME + self.HMM_SUFFIX)
        self.PFAM_CLAN_DB = os.path.join(self.IDS_DIR, 'PFAM_CLANS.txt')

    def m2def(self):
        logging.debug("Loading module descriptions")
        return self.load_pickle(self.M2DEF)

    def m(self):
        logging.debug("Loading reaction to pathway information")
        return self.load_pickle(self.M)

    def r2p(self):
        logging.debug("Loading pathway to reaction information")
        return self.load_pickle(self.R2P)

    def p2r(self):
        logging.debug("Loading reaction to orthology information")
        return self.load_pickle(self.P2R)

    def r2k(self):
        logging.debug("Loading reaction to module information")
        return self.load_pickle(self.R2K)

    def r2m(self):
        logging.debug("Loading module to reaction information")
        return self.load_pickle(self.R2M)

    def m2r(self):
        logging.debug("Loading module to compound information")
        return self.load_pickle(self.M2R)

    def m2c(self):
        logging.debug("Loading reaction to compound information")
        return self.load_pickle(self.M2C)

    def r2c(self):
        logging.debug("Loading compound to reaction information")
        return self.load_pickle(self.R2C)

    def c2r(self):
        logging.debug("Loading compound descriptions")
        return self.load_pickle(self.C2R)

    def c(self):
        logging.debug("Loading pathway descriptions")
        return self.load_pickle(self.C)

    def p(self):
        logging.debug("Loading reaction descriptions")
        return self.load_pickle(self.P)

    def r(self):
        logging.debug("Loading ko descriptions")
        return self.load_pickle(self.R)

    def k(self):
        logging.debug("Loading compound classifications")
        return self.load_pickle(self.K)

    def compound_desc_dict(self):
        logging.debug("Loading pfam to clan information")
        return self.load_pickle(self.COMPOUND_DESC)

    def pfam2clan(self):
        logging.debug("Loading clan descriptions")
        return self.load_pickle(self.PFAM2CLAN)

    def clan2name(self):
        logging.debug("Loading pfam names")
        return self.load_pickle(self.CLAN2NAME)

    def pfam2name(self):
        logging.debug("Loading pfam descriptions")
        return self.load_pickle(self.PFAM2NAME)

    def pfam2description(self):
        logging.debug("Loading ec descriptions")
        return self.load_pickle(self.PFAM2DESCRIPTION)

    def ec2description(self):
        logging.debug("Loading pfam hierarchy")
        return self.load_pickle(self.EC2DESCRIPTION)

    def clan2pfam(self):
        logging.debug("Loading tigrfam descriptions")
        return self.load_pickle(self.CLAN2PFAM)

    def tigrfamdescription(self):
        logging.debug("Loading reference db paths")
        return self.load_pickle(self.TIGRFAM2DESCRIPTION)

    def taxonomy(self):
        # Oh, circular dependencies.
        # Local imports suck but making another parser class would suck more
        from enrichm.parser import Parser
        return Parser.parse_taxonomy(self.TAXONOMY)

    def k2r(self):
        k2r = dict()
        for reaction, kos in self.r2k().items():
            for ko in kos:
                if ko not in k2r:
                    k2r[ko] = list()
                k2r[ko].append(reaction)
        return k2r

    def c2m(self):
        c2m = dict()

        for module, compounds in self.m2c().items():
            substrates = compounds[0]
            for substrate in substrates:
                if substrate in c2m:
                    c2m[substrate].append(module)
                else:
                    c2m[substrate] = [module]
        return c2m

    def load_pickle(self, file):

        with open('.'.join([file, self.PICKLE_VERSION, self.PICKLE]), 'rb') as file_io:
            loaded_pickle = pickle.load(file_io)

        return loaded_pickle

    def parse_ko_cutoffs(self):
        cut_ko = dict()
        out_io = open(self.KO_HMM_CUTOFFS)
        _ = out_io.readline()

        for line in out_io:
            sline = line.strip().split('\t')

            if sline[1] == '-':
                cut_ko[sline[0]] = [0.0, "NA"]
            else:
                cut_ko[sline[0]] = [float(sline[1]), sline[2]]

        return cut_ko
