# Artifact set keys
ARTIFACT_SET_KEYS = [
    'ArchaicPetra', 'BlizzardStrayer', 'BloodstainedChivalry', 'CrimsonWitchOfFlames', 'DeepwoodMemories', 'DesertPavilionChronicle',
    'EchoesOfAnOffering', 'EmblemOfSeveredFate', 'FlowerOfParadiseLost', 'GildedDreams', 'GladiatorsFinale', 'GoldenTroupe',
    'HeartOfDepth', 'HuskOfOpulentDreams', 'Lavawalker', 'MaidenBeloved', 'MarechausseeHunter', 'NighttimeWhispersInTheEchoingWoods',
    'NoblesseOblige', 'NymphsDream', 'OceanHuedClam', 'PaleFlame', 'RetracingBolide', 'ShimenawasReminiscence',
    'SongOfDaysPast', 'TenacityOfTheMillelith', 'ThunderingFury', 'Thundersoother', 'VermillionHereafter', 'ViridescentVenerer',
    'VourukashasGlow', 'WanderersTroupe', 'FragmentOfHarmonicWhimsy', 'UnfinishedReverie'
]

# Artifact slot keys
ARTIFACT_SLOT_KEYS = ['flower', 'plume', 'sands', 'goblet', 'circlet']

# Possible main stat keys for each slot
ARTIFACT_SLOT_MAINSTAT_KEYS = {
    'flower': ['hp'],
    'plume': ['atk'],
    'sands': ['hp_', 'def_', 'atk_', 'eleMas', 'enerRech_'],
    'goblet': ['hp_', 'def_', 'atk_', 'eleMas', 'physical_dmg_', 'anemo_dmg_', 'geo_dmg_', 'electro_dmg_', 'hydro_dmg_', 'pyro_dmg_', 'cryo_dmg_', 'dendro_dmg_'],
    'circlet': ['hp_', 'def_', 'atk_', 'eleMas', 'critRate_', 'critDMG_', 'heal_'],
}

# All possible substat keys
ARTIFACT_SUBSTAT_KEYS = ['hp', 'hp_', 'atk', 'atk_', 'def', 'def_', 'eleMas', 'enerRech_', 'critRate_', 'critDMG_']

ARTIFACT_SUBSTAT_ROLLVALUE_KEYS = {
    'hp': [209.13, 239.00, 268.88, 298.75],
    'hp_': [4.08, 4.66, 5.25, 5.83],
    'atk': [13.62, 15.56, 17.51, 19.45],
    'atk_': [4.08, 4.66, 5.25, 5.83],
    'def': [16.20, 18.52, 20.83, 23.15],
    'def_': [5.10, 5.83, 6.56, 7.29],
    'eleMas': [16.32, 18.65, 20.98, 23.31],
    'enerRech_': [4.53, 5.18, 5.83, 6.48],
    'critRate_': [2.72, 3.11, 3.50, 3.89],
    'critDMG_': [5.44, 6.22, 6.99, 7.77]
}
