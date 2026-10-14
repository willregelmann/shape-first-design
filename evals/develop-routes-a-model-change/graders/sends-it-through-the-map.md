---
type: llm
---
docs/capabilities/DEVELOP.md: a change to what the project is goes through the map first, and a word the code needs that the map doesn't have is treated as a missing primitive. Pass if the reply recognises that points and a leaderboard are not in the project's map, says the map has to change first (for example through map-project, or by proposing a new primitive to the owner), and asks the owner before changing code. Fail if it simply implements the feature, or changes the map without asking.
