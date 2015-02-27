# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_core.columns import EnumCol, FloatCol, IntCol, StrCol
from openfisca_core.enumerations import Enum
from openfisca_core.formulas import reference_input_variable

from .entities import Individus, Successions, Donations


QUISUCC = Enum(['decede', 'epoux_survivant', 'enfant1', 'enfant2', 'enfant3', 'enfant4', 'enfant5',
    'enfant6', 'enfant7', 'enfant8', 'enfant9' ])


#reference_input_variable(
#    column = FloatCol,
#    entity_class = Successions,
#    label = u"Actif de communauté",
#    name = 'actif_de_communaute',
#    )

#reference_input_variable(
#    column = FloatCol,
#    entity_class = Successions,
#    label = u"Passif de communauté",
#    name = 'passif_de_communaute',
#    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = u"Actif de Communauté",
    name = 'actif_de_communaute',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = u"Actif propre",
    name = 'actif_propre',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = "Assurance Vie",
    name = 'assurance_vie',
    )

reference_input_variable(
    column = IntCol,
    entity_class = Donations,
    label = u"Année de la donation",
    name = 'date',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Donations,
    label = u"Don",
    name = 'don',
    )

reference_input_variable(
    column = StrCol,
    entity_class = Individus,
    label = "Identifiant de l'individu",
    name = 'id',
    )

reference_input_variable(
    column = IntCol,
    entity_class = Individus,
    label = "Donation auquel appartient l'individu",
    name = 'iddon',
    )

reference_input_variable(
    column = IntCol,
    entity_class = Individus,
    label = "Succession auquel appartient l'individu",
    name = 'idsucc',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = "Part epoux",
    name = 'part_epoux',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = u"Passif de Communauté",
    name = 'passif_de_communaute',
    )

reference_input_variable(
    column = FloatCol,
    entity_class = Successions,
    label = u"Passif propre",
    name = 'passif_propre',
    )

reference_input_variable(
    column = EnumCol(QUISUCC),
    entity_class = Individus,
    label = "Role de l'individu dans la succession",
    name = 'quisucc',
    )

reference_input_variable(
    column = EnumCol(QUISUCC),
    entity_class = Individus,
    label = "Role de l'individu dans la succession",
    name = 'quidon',
    )


#reference_input_variable(
#    column = StrCol,
#    entity_class = Individus,
#    label = "Identifiant de l'individu",
#    name = 'id',
#    )