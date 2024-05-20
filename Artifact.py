from ArtifactDictionaries import (
    ARTIFACT_SET_KEYS,
    ARTIFACT_SLOT_KEYS,
    ARTIFACT_SLOT_MAINSTAT_KEYS,
    ARTIFACT_SUBSTAT_KEYS,
    ARTIFACT_SUBSTAT_ROLLVALUE_KEYS
)
class Substat:
    def __init__(self, key:str, value:float):
        # Validate inputs
        if key not in ARTIFACT_SUBSTAT_KEYS:
            raise ValueError(f"Invalid key. Choose from: {ARTIFACT_SUBSTAT_KEYS}")
        if value not in ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[key]:
             raise ValueError(f"Invalid substat value for {key} slot. Choose from: {ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[key]}")
        
        self.key = key
        self.value = value

    def __str__(self):
        return f"key: {self.key}, value: {self.value}"

class Artifact:
    def __init__(self, setKey:str, rarity:int, level:int, slotKey:str, mainStatKey:str, substats:list):
        self._setKey = None
        self._rarity = None
        self._level = None
        self._slotKey = None
        self._mainStatKey = None
        self._substats = None

        # Set attributes using setter methods to perform validation
        self.setKey = setKey
        self.rarity = rarity
        self.level = level
        self.slotKey = slotKey
        self.mainStatKey = mainStatKey
        self.substats = substats

    @property
    def setKey(self):
        return self._setKey

    @setKey.setter
    def setKey(self, value):
        if value not in ARTIFACT_SET_KEYS:
            raise ValueError(f"Invalid set key. Choose from: {ARTIFACT_SET_KEYS}")
        self._setKey = value

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        if value < 1 or value > 5:
            raise ValueError("Rarity must be between 1 and 5")
        self._rarity = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0 or value > 20:
            raise ValueError("Level must be between 0 and 20")
        self._level = value

    @property
    def slotKey(self):
        return self._slotKey

    @slotKey.setter
    def slotKey(self, value):
        if value not in ARTIFACT_SLOT_KEYS:
            raise ValueError(f"Invalid slot key. Choose from: {ARTIFACT_SLOT_KEYS}")
        self._slotKey = value

    @property
    def mainStatKey(self):
        return self._mainStatKey

    @mainStatKey.setter
    def mainStatKey(self, value):
        if value not in ARTIFACT_SLOT_MAINSTAT_KEYS[self.slotKey]:
            raise ValueError(f"Invalid main stat for {self.slotKey} slot. Choose from: {ARTIFACT_SLOT_MAINSTAT_KEYS[self.slotKey]}")
        self._mainStatKey = value

    @property
    def substats(self):
        return self._substats

    @substats.setter
    def substats(self, value):
        for substat in value:
            if substat.key not in ARTIFACT_SUBSTAT_KEYS:
                raise ValueError(f"Invalid substat key. Choose from: {ARTIFACT_SUBSTAT_KEYS}")
            if substat.value not in ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[substat.key]:
                raise ValueError(f"Invalid substat value for {substat.key} slot. Choose from: {ARTIFACT_SUBSTAT_ROLLVALUE_KEYS[substat.key]}")
        self._substats = value

    def __str__(self):
        substats_str = []
        for substat in self.substats:
            if substat.key in ['atk', 'def', 'hp', 'eleMas']:
                value_str = str(round(substat.value))
            else:
                value_str = str(round(substat.value,1))
            substats_str.append(f"{substat.key}: {value_str}")
        substats_output = ", ".join(substats_str)
        return f"Set: {self.setKey}, Rarity: {self.rarity}, Level: {self.level}, Slot: {self.slotKey}, Mainstat: {self.mainStatKey}, Substats: {substats_output}"
