import random

from ArtifactDictionaries import (
    ARTIFACT_SET_KEYS,
    ARTIFACT_SLOT_KEYS,
    ARTIFACT_SLOT_MAINSTAT_KEYS,
    ARTIFACT_SUBSTAT_KEYS,
    ARTIFACT_SUBSTAT_ROLLVALUE_KEYS
)

from Artifact import (
    Artifact,
    Substat
)
  # Importing the Artifact class from your main script

def generate_random_substat(mainStatKey, used_substats):
    """Generate a random substat, excluding the mainstat and already used substats."""
    # Exclude mainstat key and used substats from the available substats
    available_substats = list(set(ARTIFACT_SUBSTAT_KEYS) - set([mainStatKey]) - set(used_substats))
    key = random.choice(available_substats)
    value = random.choice(ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[key])
    
    return Substat(key, value)

def generate_random_artifact():
    setKey = random.choice(ARTIFACT_SET_KEYS)
    rarity = 5
    level = 0
    slotKey = random.choice(ARTIFACT_SLOT_KEYS)
    mainStatKey = random.choice(ARTIFACT_SLOT_MAINSTAT_KEYS[slotKey])
    num_substats = random.choices([3, 4], weights=[0.75, 0.25])[0]
    substats = []
    used_substats = []
    while len(substats) < num_substats:
        substat = generate_random_substat(mainStatKey, used_substats)
        substats.append(substat)
        used_substats.append(substat.key)

    return Artifact(setKey, rarity, level, slotKey, mainStatKey, substats)