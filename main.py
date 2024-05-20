from GenerateArtifact import(
    generate_random_artifact
)

from levelup import(
    level_up_artifact
)

artifact = generate_random_artifact()
print("Created random artifact:", artifact)
level_up_artifact(artifact)
print("After leveling up to 4:", artifact)
level_up_artifact(artifact)
print("After leveling up to 8:", artifact)
level_up_artifact(artifact)
print("After leveling up to 12:", artifact)
level_up_artifact(artifact)
print("After leveling up to 16:", artifact)
level_up_artifact(artifact)
print("After leveling up to 20:", artifact)
