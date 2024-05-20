from ArtifactDictionaries import (
    ARTIFACT_SUBSTAT_KEYS,
    ARTIFACT_SUBSTAT_ROLLVALUE_KEYS
)

from Artifact import (
    Artifact,
    Substat
)

import random

def level_up_artifact(artifact: Artifact):
    """Level up the artifact by adding 4 levels and adjusting substats."""
    artifact.level += 4
    if len(artifact.substats) < 4:
        available_substats = list(set(ARTIFACT_SUBSTAT_KEYS) - set(substat.key for substat in artifact.substats) -set([artifact.mainStatKey]))
        new_substat_key = random.choice(available_substats)
        new_substat_value = random.choice(ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[new_substat_key])
        artifact.substats.append(Substat(key=new_substat_key, value=new_substat_value))
    else:
        chosen_substat = random.choice(artifact.substats)
        chosen_substat.value += random.choice(ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[chosen_substat.key])

